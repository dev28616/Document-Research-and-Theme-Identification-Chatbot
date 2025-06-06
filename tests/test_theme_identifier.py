import sys
import os


# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.services.search_query import query_index_with_themes

query = "Who is Virat Kohli and what are the key themes in his career?"
result = query_index_with_themes(query)

print("🧠 Answer:\n", result["answer"])
print("\n📚 Themes:\n", result["themes"])
