import os
import fitz  # PyMuPDF for PDFs
import docx  # python-docx for DOCX
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Global in-memory FAISS index + tracking
index = faiss.IndexFlatL2(384)
chunks = []
sources = []

def load_documents(folder_path='app/uploads', chunk_size=500):
    global index, chunks, sources

    # Reset index and memory
    index = faiss.IndexFlatL2(384)
    chunks = []
    sources = []

    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)

        if filename.endswith(".pdf"):
            doc = fitz.open(path)
            text = "\n".join([page.get_text() for page in doc])

        elif filename.endswith(".docx"):
            text = "\n".join([para.text for para in docx.Document(path).paragraphs])

        elif filename.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

        else:
            continue  # Skip unsupported files

        chunk_and_store(text, filename, chunk_size)


def chunk_and_store(text, source_name, chunk_size=500, overlap=100):
    global index, chunks, sources

    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i+chunk_size].strip()
        if chunk:
            embedding = model.encode([chunk])[0]
            index.add(np.array([embedding]))
            chunks.append(chunk)
            sources.append(source_name)


def get_top_chunks(query, k=3):
    if index.ntotal == 0:
        return [("⚠️ No documents uploaded yet.", "System")]
    
    query_vec = model.encode([query])[0]
    distances, indices = index.search(np.array([query_vec]), k)

    results = []
    for i in indices[0]:
        if i < len(chunks):
            results.append((chunks[i], sources[i]))

    return results

