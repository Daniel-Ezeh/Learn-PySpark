import json
import uuid

# Load the multi-line JSON array
with open("/Users/nombauser/Desktop/GIT/MyGitRepos/Learn-PySpark/files/sample_3.json", "r") as f:
    data = json.load(f)

# Write each JSON object on its own line in CSV
with open("output.csv", "w") as f:
    for i, record in enumerate(data, start=1):
        f.write(f"{i},'{json.dumps(record)}',{uuid.uuid4()}\n")