# 🧠 Server Downtime Duration Prediction

A **Machine Learning Regression Project** that predicts **server downtime duration (in minutes)** based on system metrics — CPU usage, memory load, disk IOPS, latency, temperature, region, and OS details.  

This project demonstrates **data engineering, EDA, ML modeling, SQL analytics, and Streamlit deployment**.

---

## 🚀 Project Overview

| Stage | Description |
|--------|-------------|
| **Goal** | Predict server downtime duration using supervised regression |
| **Technique** | Supervised ML (Regression) |
| **Algorithms Used** | Linear, Ridge, Lasso, Decision Tree, Random Forest |
| **Deployment** | Streamlit Web App |
| **Database** | MySQL |
| **Dataset** | dataset with 10,000+ records, 10 columns and data inconsistencies |

---

## 🧩 Features

- dataset with **strong feature correlations **  
- **Real-world data imperfections** — missing values, inconsistent formatting, abbreviations, outliers, duplicates  
- **Comprehensive data cleaning** and preprocessing pipeline  
- **SQL-based analytics** (7 business-style insights)  
- **Exploratory Data Analysis (EDA)** using Pandas, Matplotlib, Seaborn  
- **Model comparison** across multiple regression algorithms  
- **Cross-validation**, model evaluation (R², MAE, RMSE)  
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

## 🗄️ SQL Analysis (7 Queries)

Stored the dataset in **MySQL** and explored insights via SQL

---

## 📊 Exploratory Data Analysis (EDA)

Performed using **Pandas, Matplotlib, Seaborn** to answer 7 questions: 

---

## ⚙️ Machine Learning Pipeline

### **Preprocessing**
- Scaled numeric features using `StandardScaler`  
- Encoded categorical variables using `OneHotEncoder`  
- Split data: 80% training / 20% testing  

### **Models Trained**
- Linear Regression  
- Ridge / Lasso Regression  
- Decision Tree  
- Random Forest  
-     

### **Evaluation Metrics**
- **R² Score**
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **5-Fold Cross Validation (CV R²)**

Saved best model → **`server_downtime_model.pkl`**

---


