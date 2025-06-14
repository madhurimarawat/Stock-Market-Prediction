# 📦 InfluxDB Setup Guide

This guide provides step-by-step instructions for installing, configuring, and using InfluxDB to store and manage time-series stock data for the project.

## 🛠 Installation

### ✅ Windows

1. Download from: [https://portal.influxdata.com/downloads/](https://portal.influxdata.com/downloads/)
2. Extract the ZIP file.
3. Add the InfluxDB binary path to system environment variables.
4. Run `influxd` in a terminal to start the service.

### ✅ Linux (Debian/Ubuntu)

```bash
wget https://repos.influxdata.com/influxdb.key
gpg --dearmor influxdb.key | sudo tee /etc/apt/trusted.gpg.d/influxdb.gpg > /dev/null
echo "deb [signed-by=/etc/apt/trusted.gpg.d/influxdb.gpg] https://repos.influxdata.com/debian stable main" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt update
sudo apt install influxdb2
sudo systemctl start influxdb
```

## 🗃️ Initial Configuration

1. Open browser: `http://localhost:8086`
2. Set up user credentials, organization, and bucket.
3. Create a bucket named: **`stock_price`**
4. Generate an API token for accessing the bucket.

## 🧪 Sample Query (InfluxQL)

```influxql
CREATE DATABASE stock_price;
USE stock_price;
INSERT stock_price,ticker=AAPL price=185.6,volume=129000 1672549200000000000
```

> **Note:** The **measurement name** used throughout this project is: **`stock_price`**

## 📤 Sending Data to InfluxDB

The following Python scripts are included in this folder to send various types of stock data to InfluxDB using batch processing:

- `InfluxDB_Batch_Dataframe.py` – sends **original historical stock data**
- `InfluxDB_Batch_Dataframe_Hybrid_Model.py` – sends **original and hybrid model predicted data**
- `InfluxDB_Batch_Dataframe_Model_Prediction.py` – sends **original and numerical model predicted data**
- `InfluxDB_Batch_Dataframe_Textual_Analysis.py` – sends **original and predicted sentiment/classification data from textual analysis**

These scripts are fully integrated to push structured data directly into the configured InfluxDB bucket `stock_price` using the measurement name `stock_price`.

## 🧵 Integration Note

This InfluxDB instance serves as the time-series backend for Grafana dashboards within this project. The same bucket and measurement names (**`stock_price`** and **`stock_price`**) will be used in Grafana data source configuration and queries.
