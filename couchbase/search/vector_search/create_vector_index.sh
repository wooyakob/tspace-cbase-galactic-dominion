curl -u username:'password' -XPUT \
  http://localhost:8094/api/index/planet_vector_index \
  -H "Content-Type: application/json" \
  -d @"/path/to/planet-vector-index.json"