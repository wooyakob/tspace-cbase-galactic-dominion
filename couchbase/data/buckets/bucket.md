## Buckets
A bucket is the fundamental space for storing data in Couchbase Server. 

Buckets contain a hierarchy of **scopes** and **collections** for logical data grouping.[More info](https://docs.couchbase.com/server/current/learn/data/scopes-and-collections.html). 

Minimize the number of buckets to utilize resources efficiently.
---
### Setup Buckets (Example Structure)
- **Bucket:** `galactic-dominion`
  - **Scope:** `game_data`
    - **Collections:**
      - `players`
      - `star_systems`
      - `planets`
      - `fleets`
      - `combats`
      - `resources`
      - `technologies`
      - `diplomacy`
      - `sessions`
- **Type:** Couchbase (persistent)
- **Recommended RAM Quota:** Start with **500 MiB**. Scale up as player base / data volume increases.
- **Storage Backend:** COUCHSTORE (default; great for unknown data sizes). 
- **Ejection Policy:** Value-only (recommended for performance).
- **Replication:** Disable replicas.
---
### Setup Scopes & Collections (Example)
**For `galactic-dominion` bucket:**
1. Click **Add Scope** and create `game_data`.
2. Inside the `game_data` scope, click **Add Collection** for each.
---
### Importing Data
You can import documents in two ways:
**1. CLI (`cbimport`):**
- Make sure Couchbase Server is installed.
- Find `cbimport`:
  ```
  find /Applications/Couchbase\ Server.app -name cbimport
  ```
- Add to PATH (in `~/.zshrc`):
  ```
  export PATH=$PATH:/Applications/Couchbase\ Server.app/Contents/Resources/couchbase-core/bin
  source ~/.zshrc
  ```
- Example import command (edit placeholers, update relevant bucket, scope, collection and filepath):
  ```
  cbimport json \
  --format list \
  -c http://localhost:8091 \
  -u <USERNAME> \
  -p <PASSWORD> \
  -b galactic-dominion \
  --scope-collection-exp game_data.players \
  -d "file:///path/to/players.json" \
  -g "#UUID#"
  ```
**2.UI:**
- Documents --> Select File to Import. Import JSON file e.g. players.json.
- Choose - correct Bucket, Scope and Collection.
- Use the UUID.
- Hit import.
---
> For more details, see [Couchbase documentation on buckets, memory, and storage](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html).

### Setting Up a Separate Scope for Eventing Functions
To support Couchbase Eventing functions (such as combat alerts), create a dedicated scope and collections for event-driven data:
1. In the **Couchbase Web Console**, select the `galactic-dominion` bucket.
2. Click **Add Scope** and create a new scope named `game_events`.
3. Inside the `game_events` scope, click **Add Collection** and create the following collections:
   - `alerts` (for event alerts, e.g., combat notifications)

This separation allows eventing functions to write alerts without interfering with core game data.