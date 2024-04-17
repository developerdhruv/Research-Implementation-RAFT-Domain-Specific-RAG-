from llama_index.core.llama_pack import download_llama_pack

# download and install dependencies
RAFTDatasetPack = download_llama_pack("RAFTDatasetPack", "./raft_dataset_pack")

#any llama-hub loader to get documents can be used here
raft_dataset = RAFTDatasetPack(file_path)


dataset = raft_dataset.run()
