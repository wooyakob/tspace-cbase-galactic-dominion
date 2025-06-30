# tspace-cbase-galactic-dominion
# 🚀 Build the Future of Space Strategy Gaming with Turion, Couchbase, and AWS!

## 📂 Included in the `couchbase/` Folder
- **cluster**: Optimized for a space strategy game. 
- **data**: Example player profiles, game states and fleet compositions.
- **queries**: Ready to use example database queries.
- **indexes**: Ready to use Indexes for high performance queries.
- **eventing**: Example combat alert function for dynamic events.
- **analytics**: Analytical queries for game leaderboards and metrics.
- **search**: Full Text and Vector Search examples for finding Planets.
---

## 🧪 Run Couchbase Enterprise Edition Locally
1. **Pull the Docker image**  
   ```bash
   docker pull couchbase:7.6.6

2. **Start Container**  
docker run -d --name space-game-db \
  -p 8091-8097:8091-8097 \
  -p 9123:9123 \
  -p 11207:11207 \
  -p 11210:11210 \
  -p 11280:11280 \
  -p 18091-18097:18091-18097 \
  couchbase:7.6.6

3. **Access UI**  
@ http://localhost:8091/ui/index.html

---
## ⚙️ Set Up a New Cluster
1. **Cluster Name**:  
   `tspace-cbase-galactic-dominion`

2. **Admin Credentials**:  
   - Username: `Admin`  
   - Password: Generate a strong one using [strongpasswordgenerator.org](https://www.strongpasswordgenerator.org/)

3. **License Agreement**:  
   - Read and accept the Couchbase Enterprise Edition (EE) License Agreement  
   - Optionally enable usage statistics reporting

4. **Cluster Configuration**:  
   - See [`opt-cluster.md`](./couchbase/opt-cluster.md)  
   - Refer also to the included `.json` configuration files in the same folder.

### 📝 Licensing
The **Couchbase Enterprise Edition license** is free for **development and testing** purposes. A **paid subscription** is required for **production deployments**.