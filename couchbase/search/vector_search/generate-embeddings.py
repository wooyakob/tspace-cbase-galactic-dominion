import os
import json
from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

input_path = os.getenv("INPUT_PATH")  # planets.json file path
output_path = os.getenv("OUTPUT_PATH")  # location to save planet embeddings

with open(input_path, "r", encoding="utf-8") as f:
    planets = json.load(f)

updated_planets = []

for planet in planets:
    name = planet.get("name", "").strip()
    description = planet.get("description", "").strip()
    
    if not name:
        print("Skipping planet with missing name.")
        continue

    combined_text = f"Name: {name}\nDescription: {description}"
    embedding_vector = embeddings_model.embed_documents([combined_text])[0]
    planet["embedding"] = embedding_vector
    updated_planets.append(planet)
    
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(updated_planets, f, indent=4)

print(f"Embeddings generated and saved to: {output_path}")