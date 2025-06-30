# Full Text Search
# https://docs.couchbase.com/server/7.1/fts/fts-creating-indexes.html
# Tokenizing and Indexing text fields to search for planets using words and phrases, not exact matches.

from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, SearchOptions
from couchbase.search import QueryStringQuery 
import os
from dotenv import load_dotenv

load_dotenv()
cluster = Cluster(
    os.getenv("COUCHBASE_ENDPOINT"),
    ClusterOptions(PasswordAuthenticator(
        os.getenv("COUCHBASE_USERNAME"),
        os.getenv("COUCHBASE_PASSWORD")
    ))
)

# Searching for the Planet Terra
query = QueryStringQuery("Terra")

#query = QueryStringQuery("a planet with flesh eating cockroaches")

result = cluster.search_query(
    "galactic-dominion.game_data.planet_search",
    query,
    SearchOptions(limit=5)
)

print("[scoped access - bucket:galactic-dominion; scope:game_data]")
matches = list(result)
print(f"{len(matches)} result(s)\n")

for row in matches:
    doc_id = row.id
    score = row.score
    doc = cluster.bucket("galactic-dominion").scope("game_data").collection("planets").get(doc_id)
    content = doc.content_as[dict]
    print(f"Document ID: {doc_id}")
    print(f"Score: {score}")
    print("Fields:")
    print(f"  name: {content.get('name', '')}")
    print(f"  description: {content.get('description', '')[:120]}...") 
    print("-" * 40)