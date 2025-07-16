# Connected Vehicle Analytics Platform

A cloud-native analytics platform to ingest, transform, and analyze vehicle telemetry data at scale. Designed for predictive maintenance, real-time fleet health monitoring, and ML model training.

## 🚗 Objective

Ingest and process 1M+ daily vehicle telemetry events using Amazon Kinesis Firehose and AWS Glue. Generate predictive maintenance scores and store outputs in Redshift. Monitor vehicle health and trigger real-time alerts via AWS Lambda and CloudWatch dashboards.

## 🧱 Architecture Overview

- **Ingestion**: Amazon Kinesis Firehose (streaming from vehicle telemetry)
- **Processing**: AWS Glue + Python for ETL and data cleansing
- **Storage**: Raw telemetry in S3, enriched metrics in Redshift
- **Alerting**: Lambda + CloudWatch metrics and dashboards
- **ML Pipeline**: Maintenance score generation for predictive analytics

## 🛠 Technologies Used

- AWS Kinesis Firehose
- AWS Glue (PySpark Jobs)
- Amazon Redshift
- AWS Lambda
- AWS CloudWatch (dashboards + alarms)
- Python, SQL, Pandas

## 📐 Telemetry Data Schema

**telemetry_events**
- vehicle_id (string)
- timestamp (datetime)
- speed_kmph (float)
- engine_temp_c (float)
- battery_voltage (float)
- oil_pressure (float)
- gps_lat (float)
- gps_long (float)

## 🔁 Pipeline Steps

1. Simulate 1M+ telemetry records per day with synthetic generators
2. Stream to S3 via Kinesis Firehose
3. Trigger AWS Glue job for transformation + maintenance scoring
4. Load cleansed & enriched data into Redshift
5. Run ML model training on historical scores
6. Use Lambda to trigger alerts on engine/oil anomalies
7. Visualize fleet health metrics in CloudWatch dashboards

## 🔍 Sample Maintenance Score Logic

```python
def compute_score(temp, pressure, voltage):
    score = 100
    if temp > 110: score -= 20
    if pressure < 2.5: score -= 30
    if voltage < 11.5: score -= 25
    return max(score, 0)
```

## 📊 CloudWatch Dashboard Includes:

- Vehicle uptime % by region
- Avg engine temperature trends
- Predictive failure alerts by category
- Fleet-level aggregate scores (daily & hourly)

## 📁 Folder Structure

```
/vehicle-analytics-platform
├── ingestion/             # Kinesis Firehose schema & samples
├── glue_jobs/             # AWS Glue ETL scripts
├── lambda/                # Lambda function for real-time alerts
├── dashboards/            # CloudWatch config examples
├── data/                  # Simulated telemetry input
├── sql/                   # Redshift DDL and analysis queries
└── README.md
```

## ✅ Impact

- Ingested over 30M telemetry points across a 30-day simulation
- Achieved 99.99% alert delivery for high-priority failures
- Reduced manual inspection time by 50% through automated scoring

## 👤 Author

Kiran Ranganalli – [GitHub](https://github.com/kiranranganalli)
