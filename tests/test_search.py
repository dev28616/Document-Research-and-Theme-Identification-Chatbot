import sys
import os

# Add the project root directory to sys.path (for module import)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.services.search_query import query_index, query_index_with_themes

def test_simple_query():
    query = "Who is Virat Kohli?"
    print("🔍 Query:", query)
    try:
        answer = query_index(query)
        print("\n🧠 Gemini's Answer:\n")
        print(answer)
    except Exception as e:
        print(f"\n[❌] Failed (query_index): {e}")

def test_theme_query():
    query = "Who is Virat Kohli and what are the key themes in his career?"
    print("\n🌐 Theme-based Query:", query)
    try:
        result = query_index_with_themes(query)
        print("\n🧠 Gemini's Answer:\n", result["answer"])
        print("\n🧩 Summarized Themes:\n", result["themes"])
    except Exception as e:
        print(f"\n[❌] Failed (query_index_with_themes): {e}")

if __name__ == "__main__":
    test_simple_query()
    test_theme_query()
