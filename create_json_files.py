import json
import os
import pandas as pd

# Define paths

output_dir = "./assemblies_manifest"
os.makedirs(output_dir, exist_ok=True)

# Read file
assemblies_df = pd.read_csv("assembly_manifest_all_zip.csv")

# Iterate over rows in the dataframe
for index, row in assemblies_df.iterrows():

    file=row["file"] + ".gz"
    # Create manifest JSON
    manifest = {
        "ASSEMBLYNAME": row["name"],
        "coverage": row["coverage"],
        "program": row["program"],
        "platform": row["platform"],
        "FASTA": file,
        "ASSEMBLY_TYPE": "Isolate",
        "study": row["study"],
        "sample": row["sample"],
        "description": row["description"],

    }

    # Save to JSON file
    manifest_filename = f"manifest_{row['name']}.json"
    manifest_filepath = os.path.join(output_dir, manifest_filename)

    # Open and write the manifest to a JSON file
    with open(manifest_filepath, "w") as json_file:
        json.dump(manifest, json_file, indent=2)

    print(f"Created {manifest_filename}")

print("All manifests generated.")
