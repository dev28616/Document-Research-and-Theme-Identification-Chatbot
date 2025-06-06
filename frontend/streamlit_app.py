import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="Gen-AI Theme Identifier", layout="wide")
st.title("🧠 Gen-AI Theme Identifier Chatbot")

# Query input
query = st.text_input("Enter your question", placeholder="e.g., What penalties did SEBI impose?")

# Ask button
if st.button("Submit Query"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Processing your question..."):
            try:
                response = requests.post(API_URL, json={"query": query})
                if response.status_code == 200:
                    data = response.json()

                    # Display Answer
                    st.markdown("### 📌 Answer")
                    st.success(data["answer"])

                    # Display Themes
                    st.markdown("### 🧠 Synthesized Themes")
                    st.info(data["themes"])

                    # Display Source Documents
                    if data.get("sources"):
                        st.markdown("### 📂 Source Documents Used")
                        for src in data["sources"]:
                            st.markdown(f"- {src}")

                else:
                    st.error(f"API error: {response.status_code} — {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")




st.sidebar.markdown("### 📁 Upload Documents")
uploaded_file = st.sidebar.file_uploader("Upload PDF / Image / Text", type=["pdf", "png", "jpg", "txt"])

if uploaded_file:
    with st.spinner("Uploading and indexing file..."):
        try:
            response = requests.post(
                "http://localhost:8000/upload/",
                files={"file": (uploaded_file.name, uploaded_file.getvalue())}
            )
            res_json = response.json()
            if res_json.get("status") == "success":
                st.sidebar.success(f"✅ {uploaded_file.name} indexed.")
            else:
                st.sidebar.error(f"❌ {res_json.get('reason')}")
        except Exception as e:
            st.sidebar.error(f"Error: {e}")
