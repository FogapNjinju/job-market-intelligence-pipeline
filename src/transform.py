from pathlib import Path
import json
import utils

# Get current file path (clean.py)
current_file = Path(__file__).resolve()

# Navigate to project root → then to data/raw/file.json
data_path = current_file.parents[1] / "data" / "raw" / "job_data.json"

# Load the JSON data
raw_data = utils.load_from_json(data_path)

