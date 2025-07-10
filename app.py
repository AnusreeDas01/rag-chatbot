
import streamlit as st
st.set_page_config(page_title="RAG Chatbot", layout="wide")



from main import utils, rag_engine
import os
from streamlit_lottie import st_lottie


import json
with open("assets/virtual_assistant.json", "r") as f:
    lottie_data = json.load(f)

# Layout in two columns
col1, col2 = st.columns([1, 1])  # adjust ratio if needed

with col1:
    st_lottie(lottie_data, height=350, key="virtual-assistant")


with col2:
    st.markdown("""
        <div style='padding-top: 10px;'>
            <div style='text-align:center;
                    background: -webkit-linear-gradient(45deg, #d1d5db, #9ca3af);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-size: 5rem;
                    font-weight: 900;
                    margin-bottom: 0.2rem;'>
            💬 Chatbot
            </div>
            <p style='text-align:center; color:gray; font-size: 1.5rem;'>
            Upload files ➜ Ask anything ➜ Get AI answers with sources
            </p>
            <p style='text-align:center; color:gray; font-size: 1rem;'>
            Welcome to the chatbot💬!
            Start a conversation with your documents📄.
            Upload PDFs, Word files, or plain text — and ask anything you want.
            The chatbot will search only within your uploaded content and give you accurate, source-backed answers.
            </p>
            <p style='text-align:center; color:gray; font-size: 1rem;'>
            🚀 Save time. Get clarity. Let AI read it for you.
            </p>
        </div>
    """, unsafe_allow_html=True)
    



# Init session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []


# Upload section
uploaded = st.file_uploader("📁 Upload .pdf / .txt / .docx files", type=["pdf", "docx", "txt"], accept_multiple_files=True)

if uploaded:
    for file in uploaded:
        filepath = f"main/uploads/{file.name}"
        with open(filepath, "wb") as f:
            f.write(file.getbuffer())
        if file.name not in st.session_state.uploaded_files:
            st.session_state.uploaded_files.append(file.name)
    utils.load_documents("main/uploads")
    st.success("✅ Files uploaded. ")
        

# Show current files
if st.session_state.uploaded_files:
    with st.expander("📂 Active Files", expanded=True):
        for file in st.session_state.uploaded_files:
            st.markdown(f"✔️ `{file}`", unsafe_allow_html=True)


# Chat input
query = st.text_input("💬 Ask a question:", placeholder="What does the company policy say about leave?")
if st.button("Send", use_container_width=True) and query:
    st.session_state.messages.append({"role": "user", "text": query})

    with st.spinner("🤖 Thinking..."):
        answer = rag_engine.generate_answer(query)
        st.session_state.messages.append({"role": "bot", "text": answer})

# Display chat history
if st.session_state.messages:
    for msg in st.session_state.messages:
        align = "user" if msg["role"] == "user" else "assistant"
        if msg["role"] == "user":
            bubble_color = "#1e40af"  # Deep blue
            text_color = "#ffffff"
            prefix = "🧑‍💻 <b>You</b>"
        else:
            bubble_color = "#f9fafb"  # Light gray
            text_color = "#111827"
            prefix = "🤖 <b>Bot</b>"

        st.markdown(
            f"<div style='background-color:{bubble_color}; color:{text_color}; padding:12px; border-radius:10px; margin-bottom:10px;'>"
            f"{prefix}<br>{msg['text']}</div>",
            unsafe_allow_html=True
        )
    # Scroll to bottom
    st.markdown("<script>window.scrollTo(0,document.body.scrollHeight);</script>", unsafe_allow_html=True)

        
# Download chat history
if st.session_state.messages:
    chat_text = ""
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Bot"
        chat_text += f"{role}: {msg['text']}\n\n"

    st.download_button(
        label="💾 Download Chat History",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain",
        use_container_width=True
    )
# Clear everything
if st.button("🧹 Clear chat"):
    # Delete uploaded files from folder
    for file in st.session_state.get("uploaded_files", []):
        try:
            os.remove(f"main/uploads/{file}")
        except Exception as e:
            print(f"❌ Error deleting file {file}: {e}")

    # Clear session state
    st.session_state.clear()
    st.success("✅ Chat, memory, and files are cleared.")
    st.rerun()


