curl -u username:'password' -XPUT \
  http://localhost:8094/api/index/planet_search \
  -H "Content-Type: application/json" \
  -d @"filepath/tspace-cbase-galactic-dominion/couchbase/search/full_text_search/planet_fts.json"