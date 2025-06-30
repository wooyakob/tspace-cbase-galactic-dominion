# Optimized Cluster Configuration

This configuration is designed for Couchbase Server (Enterprise Edition) to maximize game performance and resource efficiency.

---

### Service Allocations

- **Data:** 3584 MiB  
  _Fast read/write for player states, galaxy maps, fleets, and events._

- **Query:** 512 MiB  
  _Advanced filtering (fleet locations, tech trees, diplomacy lookups)._

- **Index:** 640 MiB  
  _Indexes for faction queries, planet ownership, research status._

- **Search:** 256 MiB  
  _UI search (planets, techs, anomalies)._

- **Analytics:** 1024 MiB  
  _Player economy trends, balance feedback, match telemetry._

- **Eventing:** 384 MiB  
  _Async triggers: dynamic events, tech completions, faction alerts._

- **Backup:** _Not enabled_

---

**Total Allocated:** 6400 / 6813 MiB (Under Max Allowed Quota)

_Reallocates RAM toward services that directly impact game performance._