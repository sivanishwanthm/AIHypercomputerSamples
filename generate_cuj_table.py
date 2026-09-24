import csv

data = [
    {
        "Workload Type": "Post training",
        "Match": "Complete Match",
        "CUJ Number": "001",
        "CUJ": "Multihost RL (GRPO) on GKE using the full Tunix, MaxText, vLLM and Pathways stack",
        "Models Used": "Llama 3 70B, Gemma 3 27B",
        "Priority": "P0",
        "Model Match": "Yes",
        "Model Type": "Dense",
        "Accelerator": "v6e",
        "Orchestrator": "GKE",
        "Software Stack": "Tunix, MaxText, vLLM, Pathways",
        "Host Type": "multihost",
        "No of chips Used": "64",
        "Topology": "8*8",
        "Surface Areas": "Github Recipes",
        "CUJ Description": "Execute a massive-scale GRPO loop on a GKE TPU cluster by orchestrating the Tunix library and MaxText trainer alongside a distributed vLLM sampling engine; this journey uses Pathways to manage high-throughput weight transfers enabling complex reasoning alignment for large-scale models (like Llama 3 70B or Gemma 3 27B) across multiple TPU slices.",
        "URL Link to the recipe": "https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/tpu/tuning/sft_tuning_gke_tpu_gcluster"
    },
    {
        "Workload Type": "Post training",
        "Match": "Complete Match",
        "CUJ Number": "002",
        "CUJ": "Multihost SFT using MaxText and Pathways on GKE",
        "Models Used": "Llama 3 70B, Gemma 4 31B",
        "Priority": "P0",
        "Model Match": "Yes",
        "Model Type": "Dense",
        "Accelerator": "v6e",
        "Orchestrator": "GKE",
        "Software Stack": "MaxText, Pathways, Tunix",
        "Host Type": "multihost",
        "No of chips Used": "32",
        "Topology": "4*8",
        "Surface Areas": "Github Recipes",
        "CUJ Description": "Scale the alignment of large-scale models (like Llama 3 70B or Gemma 4 31B) across multiple TPU nodes in a GKE cluster by using Cluster Toolkit to orchestrate a distributed MaxText SFT pipeline; this journey leverages the Tunix library and Pathways (or McJAX) to efficiently shard model parameters and datasets across a high-performance interconnect for massive-scale post-training.",
        "URL Link to the recipe": "https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/tpu/tuning/sft_tuning_gke_tpu_gcluster"
    },
    {
        "Workload Type": "Post training",
        "Match": "Complete Match",
        "CUJ Number": "003",
        "CUJ": "Singlehost SFT using MaxText",
        "Models Used": "Gemma 3 4B",
        "Priority": "P0",
        "Model Match": "Yes",
        "Model Type": "Dense",
        "Accelerator": "v6e",
        "Orchestrator": "GCE",
        "Software Stack": "MaxText, Tunix",
        "Host Type": "singlehost",
        "No of chips Used": "8",
        "Topology": "2*4",
        "Surface Areas": "Github Recipes",
        "CUJ Description": "Convert a pre-trained small model (like Llama or Gemma) from Hugging Face into MaxText format and execute a high-performance SFT pipeline on Cloud TPUs using the Tunix library to align the model with custom datasets from Hugging Face, or Grain.",
        "URL Link to the recipe": "https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/tpu/tuning/gemma3-4b-sft"
    },
    {
        "Workload Type": "Post training",
        "Match": "Complete Match",
        "CUJ Number": "004",
        "CUJ": "Singlehost RL (GRPO) using MaxText",
        "Models Used": "Llama 3.1 8B",
        "Priority": "P0",
        "Model Match": "Yes",
        "Model Type": "Dense",
        "Accelerator": "v6e",
        "Orchestrator": "GCE",
        "Software Stack": "MaxText, Tunix",
        "Host Type": "singlehost",
        "No of chips Used": "8",
        "Topology": "2*4",
        "Surface Areas": "Github Recipes",
        "CUJ Description": "Enhance the reasoning capabilities of a smaller model like Llama 3.1-8B on Trillium (v6e) by using MaxText and the Tunix library to execute a GRPO loop.",
        "URL Link to the recipe": "https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/tpu/tuning/llama3.1-8b-rl"
    }
]

columns = [
    "Workload Type",
    "Match",
    "CUJ Number",
    "CUJ",
    "Models Used",
    "Priority",
    "Model Match",
    "Model Type",
    "Accelerator",
    "Orchestrator",
    "Software Stack",
    "Host Type",
    "No of chips Used",
    "Topology",
    "Surface Areas",
    "CUJ Description",
    "URL Link to the recipe"
]

def export_csv():
    with open("cuj_dataset.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def export_markdown():
    with open("cuj_dataset.md", mode="w", encoding="utf-8") as f:
        f.write("| " + " | ".join(columns) + " |\n")
        f.write("| " + " | ".join(["---"] * len(columns)) + " |\n")
        for row in data:
            f.write("| " + " | ".join([str(row[col]) for col in columns]) + " |\n")

if __name__ == "__main__":
    export_csv()
    export_markdown()
    print("Exported CUJ dataset to cuj_dataset.csv and cuj_dataset.md successfully.")
