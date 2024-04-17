#pip install llama-index  (first install dependencies)
#pip install llama-index-packs-raft-dataset (first install dependencies)

from llama_index.packs.raft_dataset import RAFTDatasetPack
import os

os.environ["OPENAI_API_KEY"] = "<YOUR OPENAI API KEY>"

raft_dataset = RAFTDatasetPack("./paul_graham_essay.txt")
dataset = raft_dataset.run()
output_path = "<output path>"
# Save as .arrow format
dataset.save_to_disk(output_path)

# Save as .jsonl format
dataset.to_json(output_path + ".jsonl")
