import os
from dotenv import load_dotenv
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Set up Gemini
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Chain: summarize multiple docs using map_reduce
summarizer_chain = load_summarize_chain(gemini_llm, chain_type="map_reduce")

def summarize_themes(retrieved_chunks, query):
    if not retrieved_chunks:
        return "No relevant content found to summarize."

    # Convert retrieved text to LangChain Document objects
    documents = [
        Document(page_content=chunk, metadata={"source": meta.get("metadata", {}).get("filename", "unknown")})
        for chunk, meta in retrieved_chunks
    ]

    summary = summarizer_chain.run(documents)

    return f"🔍 Query: {query}\n\n🧠 Synthesized Themes:\n\n{summary.strip()}"
