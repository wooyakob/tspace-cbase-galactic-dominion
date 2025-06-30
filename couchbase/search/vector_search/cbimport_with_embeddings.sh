cbimport json \
  -c couchbase://localhost \
  -u username \
  -p 'password' \
  -b galactic-dominion \
  --scope-collection-exp game_data.planets \
  -f list \
  -d "filepath/tspace-cbase-galactic-dominion/couchbase/search/vector_search/planets_with_embeddings.json" \
  -g "#UUID#"