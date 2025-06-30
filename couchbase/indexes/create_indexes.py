import os
from dotenv import load_dotenv
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

load_dotenv()

username = os.getenv("COUCHBASE_USERNAME")
password = os.getenv("COUCHBASE_PASSWORD")
couchbase_url = os.getenv("COUCHBASE_ENDPOINT")

cluster = Cluster(
    couchbase_url,
    ClusterOptions(PasswordAuthenticator(username, password))
)

index_queries = [
    "CREATE INDEX idx_planets_owner_player_id ON `galactic-dominion`.`game_data`.`planets`(owner_player_id);",
    "CREATE INDEX idx_fleets_owner_player_id ON `galactic-dominion`.`game_data`.`fleets`(owner_player_id);",
    "CREATE INDEX idx_star_systems_owner_player_id ON `galactic-dominion`.`game_data`.`star_systems`(owner_player_id);",
    "CREATE INDEX idx_players_player_id ON `galactic-dominion`.`game_data`.`players`(player_id);",
    "CREATE INDEX idx_sessions_status ON `galactic-dominion`.`game_data`.`sessions`(status);",
    "CREATE INDEX idx_combats_status ON `galactic-dominion`.`game_data`.`combats`(status);",
    "CREATE INDEX idx_star_systems_system_id ON `galactic-dominion`.`game_data`.`star_systems`(system_id);",
    "CREATE INDEX idx_planets_system_id ON `galactic-dominion`.`game_data`.`planets`(system_id);",
    "CREATE INDEX idx_resources_player_id ON `galactic-dominion`.`game_data`.`resources`(player_id);",
    "CREATE INDEX idx_players_diplomacy_allies ON `galactic-dominion`.`game_data`.`players`(DISTINCT ARRAY ally FOR ally IN diplomacy.allies END);",
    "CREATE INDEX idx_players_technology_ids ON `galactic-dominion`.`game_data`.`players`(DISTINCT ARRAY tech_id FOR tech_id IN technology_ids END);",
    "CREATE INDEX idx_technologies_tech_id ON `galactic-dominion`.`game_data`.`technologies`(tech_id);"
]

for query in index_queries:
    try:
        cluster.query(query).execute()
        print(f"Executed: {query}")
    except Exception as e:
        print(f"Error executing: {query}\n{e}")