# 🚚📄 Vendor Invoice Intelligence Portal

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

# 🚀 Project Overview

**Vendor Invoice Intelligence Portal** is an AI-driven finance analytics application designed to help organizations analyze vendor invoices efficiently.

The system uses machine learning to:

* Predict freight costs.
* Identify risky vendor invoices requiring manual approval.
* Support finance teams with intelligent decision-making.
* Provide real-time predictions through an interactive dashboard.

---

# 🏢 Business Problem

Organizations process thousands of invoices every month. Manual invoice verification often results in:

* Increased processing time.
* Human errors.
* Delayed approvals.
* Higher operational costs.
* Difficulty identifying risky invoices.

This project applies machine learning to automate freight prediction and invoice risk assessment, improving operational efficiency.

---

# ✨ Features

✅ Freight Cost Prediction using Quantity and Invoice Dollars.

✅ Invoice Manual Approval Prediction.

✅ Interactive Streamlit Dashboard.

✅ Real-Time Prediction Interface.

✅ Machine Learning Regression Models.

✅ Automated Invoice Risk Assessment.

✅ User-Friendly Dashboard.

✅ Business-Oriented Analytics Interface.

✅ Model Selection Functionality.

---

# 🛠️ Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Programming Language  |
| Streamlit    | Dashboard Development |
| Pandas       | Data Processing       |
| NumPy        | Numerical Computing   |
| Scikit-learn | Machine Learning      |
| Plotly       | Data Visualization    |
| Joblib       | Model Serialization   |
| SQLite       | Database Storage      |

---

# 🤖 Machine Learning Models

### Freight Cost Prediction Models

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

### Invoice Approval Prediction

* Classification-based invoice risk prediction model.

---

# 📊 Model Performance

| Metric                    | Value     |
| ------------------------- | --------- |
| R² Score                  | **97%**   |
| Mean Absolute Error (MAE) | **24.46** |

The developed models demonstrate high predictive performance and reliable business insights.

---

# 📁 Project Structure

```text
Vendor-Invoice-Intelligence-Portal/
│
├── app.py
├── freight_cost_predict/
├── invoice_flagging/
├── inference/
├── models/
├── Notebooks/
└── requirements.txt
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/vendor-invoice-intelligence-portal.git

cd vendor-invoice-intelligence-portal
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
plotly
joblib
sqlite3
```

---

# ▶️ How to Run the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

# 📈 Streamlit Dashboard Features

### 🚚 Freight Cost Prediction

* Enter Quantity.
* Enter Invoice Dollars.
* Predict Freight Cost instantly.
* Compare different regression models.

### ⚠️ Invoice Risk Assessment

* Enter invoice-related features.
* Predict manual approval requirement.
* Identify potentially risky invoices.

### 📊 Business Analytics Dashboard

* Interactive visualizations.
* Real-time predictions.
* Business-oriented interface.
* Model selection options.

---

# 💼 Business Impact

The Vendor Invoice Intelligence Portal helps organizations:

* Reduce manual invoice review efforts.
* Improve invoice approval decisions.
* Detect risky invoices earlier.
* Optimize freight cost estimation.
* Increase operational efficiency.
* Support finance teams with AI-driven analytics.

---

# 🚀 Future Enhancements

* User Authentication System.
* PDF Invoice Upload.
* Explainable AI (XAI) Integration.
* ERP System Integration.
* Cloud Deployment.
* REST API Development.
* Advanced Business Analytics Dashboard.
* Automated Report Generation.

---

# 👩‍💻 Author

## Saniya Koyal

**Data Science Student | Machine Learning Enthusiast | AI Developer**

### Responsibilities

* Developed and customized the complete application.
* Implemented machine learning models.
* Designed the Streamlit dashboard.
* Performed data preprocessing and model evaluation.
* Built business-oriented analytics features.
* Prepared the project for deployment and portfolio presentation.

---

# ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork the repository
* 📢 Share the project

---

<p align="center">
Made with ❤️ using Python, Machine Learning, and Streamlit
</p>
