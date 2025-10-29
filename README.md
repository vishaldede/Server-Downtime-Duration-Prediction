# 🧠 Server Downtime Duration Prediction

A **Machine Learning Regression Project** that predicts **server downtime duration (in minutes)** based on real-world system metrics — CPU usage, memory load, disk IOPS, latency, temperature, region, and OS details.  

---

## 🚀 Project Overview

| Stage | Description |
|--------|-------------|
| **Goal** | Predict server downtime duration using supervised regression |
| **Technique** | Supervised ML (Regression) |
| **Algorithms Used** | Linear, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting, XGBoost |
| **Deployment** | Streamlit Web App |
| **Database** | MySQL |
| **Dataset** | Synthetic but realistic dataset with 10,000+ records, 10 columns, and realistic data inconsistencies |

---

## 🧩 Features

- Dataset with **strong feature correlations (R² ≈ 0.88–0.9)**  
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

Stored the dataset in **MySQL** and explored insights via SQL:

1. Average downtime by region  
2. Average downtime by OS  
3. Top 5 servers with highest downtime  
4. Region-wise CPU vs downtime relationship  
5. Monthly downtime trend  
6. Outlier incidents (downtime > 3× mean)  
7. Avg CPU and Memory load by OS  

---

## 📊 Exploratory Data Analysis (EDA)

Performed using **Pandas, Matplotlib, Seaborn** to answer 7 questions:

1. Downtime distribution  
2. Average downtime by region  
3. Average downtime by OS  
4. Correlation heatmap  
5. CPU vs Downtime scatter  
6. Downtime trend over time  
7. Temperature vs Downtime regression  

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
- Gradient Boosting  
- XGBoost  

### **Evaluation Metrics**
- **R² Score**
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **5-Fold Cross Validation (CV R²)**

| Model | R² | CV R² | MAE | RMSE |
|--------|----|-------|------|------|
| **XGBoost** | **0.89** | 0.87 | 8.5 | 11.2 |
| Random Forest | 0.88 | 0.86 | 9.0 | 11.8 |
| Gradient Boosting | 0.86 | 0.84 | 9.4 | 12.5 |
| Linear Regression | 0.81 | 0.78 | 11.8 | 15.1 |

Saved best model → **`server_downtime_model.pkl`**

---

## 🧪 Cross Validation

from sklearn.model_selection import cross_val_score
cv_score = cross_val_score(best_model, X_train, y_train, cv=5, scoring='r2')
print(cv_score.mean())
