import os
from datetime import timedelta
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from dotenv import load_dotenv
load_dotenv()

# Define Credentials
username = os.getenv("COUCHBASE_USERNAME")
password = os.getenv("COUCHBASE_PASSWORD")
couchbase_url = os.getenv("COUCHBASE_ENDPOINT")

# Define Target
bucket_name = "galactic-dominion"
scope_name = "game_data"
collection_name = "players"

auth = PasswordAuthenticator(username, password)

cluster = Cluster(couchbase_url, ClusterOptions(auth))
cluster.wait_until_ready(timedelta(seconds=5))

bucket = cluster.bucket(bucket_name)
scope = bucket.scope(scope_name)
collection = scope.collection(collection_name)

# Query All Players
query_str = f"SELECT * FROM `{bucket_name}`.`{scope_name}`.`{collection_name}` LIMIT 10;"
result = cluster.query(query_str)

print("Players:")
for row in result:
    player = row.get("players", row)
    print(f"- Username: {player.get('username')}")
    print(f"  Faction: {player.get('faction')}")
    print(f"  Resources: {player.get('resources')}")
    print(f"  Allies: {player.get('diplomacy', {}).get('allies', [])}")
    print(f"  Enemies: {player.get('diplomacy', {}).get('enemies', [])}")
    print()