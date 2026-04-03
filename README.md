# 🔍 SerpApi ETL Data Pipeline

## 📌 Overview

This project implements a **production-style ETL (Extract, Transform, Load) data pipeline** using the SerpApi Search API to collect and process search engine results data.

The system is designed to simulate real-world **data engineering workflows**, including data ingestion, transformation, storage, and analytics and Orchestrated ETL pipeline using Apache Airflow with scheduled execution and monitoring.

---

## 🎯 Objectives

* Extract structured search data from SerpApi
* Build a scalable and modular ETL pipeline
* Store and manage raw + processed datasets
* Enable downstream analytics and machine learning use cases

---

## 🏗️ Architecture

```
SerpApi → Extraction Layer → Raw Data Storage → Transformation Layer → Processed Data → Analytics / ML
```

---

## ⚙️ Tech Stack

* **Programming:** Python
* **Data Processing:** Pandas / PySpark
* **API Integration:** Requests
* **Storage:** CSV / Parquet / PostgreSQL / SQLite
* **Orchestration:** Apache Airflow
* **Environment Management:** python-dotenv
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
serpapi-etl-data-pipeline/
│
├── data/
│   ├── raw/                # Raw JSON responses
│   ├── processed/          # Cleaned datasets
│
├── dags/
│   └── job_market_etl_dag.py  # Airflow DAG for orchestration
│
├── src/
│   ├── extract.py          # API ingestion logic
│   ├── transform.py        # Data cleaning & transformation
│   ├── load.py             # Storage logic
│   ├── utils.py            # Helper functions
│
├── config/
│   └── config.json         # Query parameters, locations, and pipeline settings
│
├── notebooks/              # Exploratory analysis
├── tests/                  # Unit tests
│
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Custom Airflow Docker image
├── requirements.txt
├── .env                    # API keys (not committed)
├── .gitignore
├── README.md
```

---

## 🔑 Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/serpapi-etl-data-pipeline.git
cd serpapi-etl-data-pipeline
```

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```
API_KEY=your_serpapi_key_here
```

### 5. Configure Pipeline Settings

The `config/config.json` file contains all pipeline configuration:

- **query**: Job search term (default: "Barista")
- **locations**: Dictionary of location tiers (UK/US cities)
- **max_retries**: Number of API retry attempts (default: 5)
- **base_delay**: Base delay between retries in seconds (default: 2)

You can modify these settings to customize your job search.

---

This project includes Docker configuration for easy deployment with Apache Airflow.

#### Prerequisites
- Docker and Docker Compose installed

#### Quick Start with Docker

```bash
# Build and start all services
docker-compose up --build

# Or run in background
docker-compose up -d --build
```

#### Access Airflow
- Web UI: http://localhost:8080
- Default credentials: admin / admin

#### Stop Services
```bash
docker-compose down
```

#### Data Persistence

- Processed data is stored in the `data/` directory on your host machine
- Airflow metadata is stored in the `postgres_data` Docker volume
- Logs are stored in the `airflow_logs` Docker volume

#### Troubleshooting

- If you encounter permission issues, ensure Docker has access to the project directory
- For Windows users, you may need to enable file sharing in Docker settings
- Check container logs: `docker-compose logs <service_name>`

---

## ▶️ Running the Pipeline

### Option 1: Docker (Recommended)

```bash
docker-compose up --build
```

Access Airflow UI at http://localhost:8080 and trigger the `job_market_etl_pipeline` DAG.

### Option 2: Manual Execution

### Step 1: Extract Data

```
python src/extract.py
```

### Step 2: Transform Data

```
python src/transform.py
```

### Step 3: Load Data

```
python src/load.py
```

### Option 3: Using Airflow Locally

1. Install dependencies: `pip install -r requirements.txt`
2. Set environment variables as described above
3. Initialize and start Airflow
4. Access the Airflow web UI at `http://localhost:8080`
5. Enable the `job_market_etl_pipeline` DAG
6. Trigger the DAG manually or wait for the scheduled run

## 🧪 Testing

Run the unit tests:

```bash
python -m unittest tests/ -v
```

Validate your configuration:

```bash
python validate_config.py
```

---

## 📊 Sample Output

## 🔄 Example Use Case

This pipeline can be used to:

* Track **job market trends** (e.g., "Data Engineer jobs UK")
* Perform **SEO analysis**
* Monitor **competitor search rankings**
* Build **search-based datasets for ML models**

---

## 📊 Sample Output

| Title                 | Link        | Snippet       | Rank |
| --------------------- | ----------- | ------------- | ---- |
| Data Engineer Jobs UK | example.com | Hiring now... | 1    |

---

## 🚀 Future Improvements

* Store data in **cloud storage (AWS S3 / GCP)**
* Add **data quality checks and monitoring**
* Implement **ML models for trend prediction**
* Add **interactive dashboard (Streamlit / Power BI)**
* Expand to **additional job search APIs**

---

## 🔒 Security Best Practices

* API keys stored in `.env`
* `.env` excluded via `.gitignore`
* No sensitive data committed to repository

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

Your Name
MSc Data Science | Data Engineering Enthusiast
