# 💳 Loan Approval Prediction System

### 🚀 Machine Learning + Streamlit Web Application

A machine learning-based web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on an applicant's financial, credit, employment, and asset-related information.

The application uses a **Random Forest Classifier** and provides an interactive **Streamlit** interface for making predictions.

---

## 🌐 Live Application

> 🚀 **Try the deployed application:**
> **[🔗 Open Loan Approval Predictor](#)**

> Replace the `#` above with your Streamlit Cloud URL after deployment.

---

## 📌 Project Overview

Loan approval decisions depend on multiple factors such as:

* 💰 Annual income
* 💳 CIBIL score
* 🏦 Bank assets
* 🏠 Residential assets
* 🏢 Commercial assets
* 💎 Luxury assets
* 💵 Loan amount
* 📅 Loan term
* 👨‍👩‍👧 Number of dependents
* 🎓 Education
* 💼 Employment status

This project uses these features to train a machine learning classification model and provide an instant prediction through a web interface.

---

## ✨ Features

### 👤 Applicant Input

Users can enter:

* Number of dependents
* Education
* Self-employment status
* Annual income
* Loan amount
* Loan term
* CIBIL score
* Residential asset value
* Commercial asset value
* Luxury asset value
* Bank asset value

### 🤖 Machine Learning Prediction

The application predicts:

```text
✅ Loan Approved
```

or

```text
❌ Loan Rejected
```

### 📊 Approval Probability

The application also displays the model's estimated probability of loan approval.

### 📋 Applicant Summary

After prediction, the application displays a summary of the applicant's information.

### 📚 Educational Information

The sidebar contains information about:

* Machine learning model
* Important input features
* Prediction workflow
* How the application works

---

## 🧠 Machine Learning Model

The application uses a:

### 🌳 Random Forest Classifier

The model configuration used in this project is:

```python
RandomForestClassifier(
    bootstrap=False,
    criterion="gini",
    max_depth=None,
    random_state=42
)
```

Random Forest is an ensemble learning algorithm that combines multiple decision trees to produce a more robust prediction.

---

## 📥 Model Features

The model uses the following features:

| Feature                    | Description             |
| -------------------------- | ----------------------- |
| `no_of_dependents`         | Number of dependents    |
| `education`                | Graduate / Not Graduate |
| `self_employed`            | Self-employed status    |
| `income_annum`             | Annual income           |
| `loan_amount`              | Requested loan amount   |
| `loan_term`                | Loan duration           |
| `cibil_score`              | Applicant's CIBIL score |
| `residential_assets_value` | Residential asset value |
| `commercial_assets_value`  | Commercial asset value  |
| `luxury_assets_value`      | Luxury asset value      |
| `bank_asset_value`         | Bank asset value        |

---

## 🔄 Machine Learning Pipeline

```text
                Dataset
                   │
                   ▼
          Data Preprocessing
                   │
                   ▼
       Feature Transformation
                   │
                   ▼
        Random Forest Model
                   │
                   ▼
             Prediction
              /       \
             /         \
            ▼           ▼
       Approved      Rejected
```

---

## 🖥️ Application Architecture

```text
┌─────────────────────────────┐
│        Streamlit UI         │
│                             │
│  Applicant Information      │
│  Financial Information      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Data Preprocessing     │
│                             │
│  Categorical → Numerical    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Random Forest Model     │
│                             │
│ loan_approval_model.pkl     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│        Prediction           │
│                             │
│ Approved / Rejected         │
│ Approval Probability        │
└─────────────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| 🐍 Python        | Programming language      |
| 🤖 Scikit-learn  | Machine learning          |
| 🌳 Random Forest | Classification algorithm  |
| 🐼 Pandas        | Data processing           |
| 📦 Joblib        | Model serialization       |
| 🎨 Streamlit     | Web application           |
| 🐙 GitHub        | Version control & hosting |

---

## 📁 Project Structure

```text
loan-approval-prediction/
│
├── app.py
│
├── train_model.py
│
├── loan_approval_model.pkl
│
├── loan_approval_dataset.csv
│
├── requirements.txt
│
└── README.md
```

### File Description

**`app.py`**

The main Streamlit application responsible for:

* User interface
* Input collection
* Data preprocessing
* Model prediction
* Result visualization

**`train_model.py`**

Used to:

* Load the dataset
* Clean the data
* Transform categorical variables
* Train the Random Forest model
* Save the trained model

**`loan_approval_model.pkl`**

The trained Random Forest model used by the Streamlit application.

**`requirements.txt`**

Contains the Python dependencies required to run the application.

---

# 🚀 Run Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/loan-approval-prediction.git
```

Move into the project directory:

```bash
cd loan-approval-prediction
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Train the Model

If you need to recreate the model:

```bash
python train_model.py
```

This will generate:

```text
loan_approval_model.pkl
```

---

## 4️⃣ Run Streamlit

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

```text
Create GitHub Repository
          ↓
Upload Project Files
          ↓
Connect GitHub to Streamlit
          ↓
Select app.py
          ↓
Deploy
          ↓
Get Public URL
```

### Required Deployment Files

For Streamlit deployment, the main files are:

```text
app.py
loan_approval_model.pkl
requirements.txt
```

The dataset and training script are not required for prediction after the model has already been trained.

---

# 📊 Example Prediction

### Example Input

```text
Number of Dependents: 2
Education: Graduate
Self Employed: No
Annual Income: ₹50,00,000
Loan Amount: ₹1,50,00,000
Loan Term: 10 years
CIBIL Score: 750
Residential Assets: ₹50,00,000
Commercial Assets: ₹20,00,000
Luxury Assets: ₹30,00,000
Bank Assets: ₹40,00,000
```

### Example Output

```text
╔══════════════════════════════╗
║       ✅ LOAN APPROVED       ║
╚══════════════════════════════╝

Approval Probability: XX.XX%
```

The exact prediction depends on the trained model and input values.

---

# 🎯 Project Objectives

The main objectives of this project are:

* Build a machine learning model for loan approval prediction.
* Perform data preprocessing and feature transformation.
* Train a Random Forest classification model.
* Save the trained model using Joblib.
* Build an interactive Streamlit interface.
* Provide real-time loan approval predictions.
* Deploy the application as a web application.

---

# 🔮 Future Improvements

Possible improvements include:

* 📈 Add model performance visualizations.
* 🔍 Add feature importance visualization.
* 🧠 Add explainable AI using SHAP.
* 📊 Compare multiple ML algorithms.
* 📉 Add confusion matrix and classification metrics.
* 👤 Add user authentication.
* 💾 Store prediction history.
* 📄 Generate downloadable prediction reports.
* 📱 Improve mobile responsiveness.
* ☁️ Deploy using Streamlit Community Cloud.
* 🔐 Add appropriate security and privacy controls.

---

# ⚠️ Disclaimer

This application is intended for **educational and demonstration purposes**.

The prediction generated by the machine learning model should **not be treated as the sole basis for an actual financial or lending decision**.

Real-world loan approval systems require additional financial, regulatory, fairness, security, and human-review considerations.

---

# 👨‍💻 Author

**Isha**

⭐ If you found this project useful, consider giving the repository a **star**!

---

## 📜 License

This project is available for educational and learning purposes.
#   l o a n - a p p r o v a l - p r e d i c t i o n  
 