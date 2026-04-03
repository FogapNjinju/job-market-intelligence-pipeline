#!/usr/bin/env python3
"""
Configuration validation script for the Job Market Intelligence Pipeline.
"""

import json
import os
from pathlib import Path
from dotenv import load_dotenv

def validate_config():
    """Validate the pipeline configuration."""
    print("🔍 Validating Job Market Intelligence Pipeline Configuration")
    print("=" * 60)

    # Check project structure
    required_dirs = ['src', 'data/raw', 'data/processed', 'config', 'dags', 'tests']
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print(f"✅ Directory exists: {dir_path}")
        else:
            print(f"❌ Missing directory: {dir_path}")

    # Check required files
    required_files = [
        'src/extract.py', 'src/transform.py', 'src/load.py', 'src/utils.py',
        'config/config.json', 'dags/job_market_etl_dag.py',
        'requirements.txt', 'README.md', '.env'
    ]
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ File exists: {file_path}")
        else:
            print(f"❌ Missing file: {file_path}")

    # Validate config.json
    config_path = Path('config/config.json')
    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)

            required_keys = ['query', 'locations', 'max_retries', 'base_delay']
            for key in required_keys:
                if key in config:
                    print(f"✅ Config key present: {key}")
                else:
                    print(f"❌ Missing config key: {key}")

            # Check locations structure
            if 'locations' in config:
                locations = config['locations']
                if isinstance(locations, dict):
                    print(f"✅ Locations configured: {len(locations)} tiers")
                    total_locations = sum(len(tier) for tier in locations.values())
                    print(f"✅ Total locations: {total_locations}")
                else:
                    print("❌ Locations should be a dictionary")

        except json.JSONDecodeError:
            print("❌ Invalid JSON in config.json")
    else:
        print("❌ config.json not found")

    # Check environment variables
    load_dotenv()
    api_key = os.getenv('API_KEY')
    if api_key:
        print("✅ API_KEY environment variable set")
    else:
        print("❌ API_KEY environment variable not set")

    # Check Python syntax
    import subprocess
    try:
        result = subprocess.run(['python', '-m', 'py_compile', 'src/extract.py', 'src/transform.py', 'src/load.py', 'src/utils.py'],
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ All Python files compile successfully")
        else:
            print(f"❌ Python compilation errors: {result.stderr}")
    except FileNotFoundError:
        print("⚠️  Python not found in PATH")

    print("\n" + "=" * 60)
    print("🎉 Configuration validation complete!")

if __name__ == "__main__":
    validate_config()