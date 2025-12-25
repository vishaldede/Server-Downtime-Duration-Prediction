# 🧠 Server Downtime Duration Prediction

A **Machine Learning Regression Project** that predicts **server downtime duration (in minutes)** based on real-world system metrics — CPU usage, memory load, disk IOPS, latency, temperature, region, and OS details.  

---

## 🚀 Project Overview

| Stage | Description |
|--------|-------------|
| **Goal** | Predict server downtime duration using supervised regression |
| **Technique** | Supervised ML (Regression) |
| **Algorithms Used** | Linear, Lasso, Ridge, Decision Tree, Random Forest, Support Vector Machine, K-Nearest Neighbors |
| **Deployment** | Streamlit Web App |
| **Database** | MySQL |
| **Dataset** | Synthetic but realistic dataset with 10,000+ records, 10 columns, and realistic data inconsistencies |

---

## 🧩 Features

- Dataset with **strong feature correlations (R² ≈ 0.90+)**
- **Real-world data imperfections** — missing values, inconsistent formatting, abbreviations, outliers, duplicates  
- **Comprehensive data cleaning** and preprocessing pipeline  
- **SQL-based analytics** 
- **Exploratory Data Analysis (EDA)** using Pandas, Matplotlib, Seaborn  
- **Model comparison** across multiple regression algorithms  
- **Cross-validation**, model evaluation (R², MAE, MSE)  
- **Deployed using Streamlit** for real-time predictions

---

## 🧠 Data Description

| Column | Description |
|---------|--------------|
| `Server_ID` | Unique server identifier |
| `Region` | Server region (US-East, EU-West, Asia-Pacific, India-Central) |
| `CPU_Usage` | Average CPU utilization (%) |
| `Memory_Usage` | Average RAM utilization (%) |
| `Disk_IOPS` | Disk I/O operations per second |
| `Network_Latency_ms` | Average network latency in milliseconds |
| `Temperature_C` | Data center temperature in °C |
| `OS_Version` | Operating system type (Windows/Linux) |
| `Incident_Date` | Date of incident (varied formats) |
| `Downtime_Minutes` | Target variable — total downtime duration in minutes |

---

## 🧹 Data Cleaning Steps

Performed using **Pandas**:
1. Fixed inconsistent categorical values (`Region`, `OS_Version`)  
2. Corrected abbreviations and typos  
3. Standardized date formats across multiple styles  
4. Converted incorrect data types  
5. Handled missing values (median/mode imputation)  
6. Removed duplicate rows  
7. Treated outliers using the IQR method  

Output: **`server_downtime_dataset_cleaned.csv`**

---

## 🗄️ SQL Analysis

Stored the dataset in **MySQL** and explored insights via SQL

---

## 📊 Exploratory Data Analysis (EDA)

Performed using **Pandas, Matplotlib, Seaborn**

---

## ⚙️ Machine Learning Pipeline

### **Preprocessing**
- Encoded categorical variables using OneHotEncoder
- Scaled numeric features using StandardScaler 
- Split data: 80% training / 20% testing

### **Models Trained**
- Linear Regression  
- Lasso / Ridge Regression  
- Decision Tree  
- Random Forest  
- Support Vector Machine
- K-Nearest Neighbors

### **Evaluation Metrics**
- **R² Score**
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **5-Fold Cross Validation (CV)**

LinearRegression | 0.90
Saved best model → **`server_downtime_model.pkl`**

