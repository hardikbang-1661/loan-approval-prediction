# Loan Approval Prediction System

## 📌 Overview

This project is a **Machine Learning-based Loan Approval Prediction System** developed using Python and Streamlit.

The application predicts whether a loan application is likely to be **Approved** or **Rejected** based on the applicant's financial, credit, employment, and asset-related information.

The trained machine learning model is integrated into an interactive Streamlit web application.

---

## 🎯 Objective

The main objective of this project is to build a machine learning system that can predict loan approval based on important applicant characteristics.

The system takes applicant information as input and provides:

* Loan approval prediction
* Loan rejection prediction
* Approval probability
* Applicant summary

---

## 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** for loan approval prediction.

The model configuration is:

```python
RandomForestClassifier(
    bootstrap=False,
    criterion="gini",
    max_depth=None,
    random_state=42
)
```

Random Forest was selected because it provides strong classification performance by combining multiple decision trees.

---

## 📊 Features Used

The model uses the following features:

| Feature              | Description                                 |
| -------------------- | ------------------------------------------- |
| Number of Dependents | Number of people dependent on the applicant |
| Education            | Graduate / Not Graduate                     |
| Self Employed        | Yes / No                                    |
| Annual Income        | Applicant's annual income                   |
| Loan Amount          | Requested loan amount                       |
| Loan Term            | Loan duration in years                      |
| CIBIL Score          | Applicant's credit score                    |
| Residential Assets   | Value of residential assets                 |
| Commercial Assets    | Value of commercial assets                  |
| Luxury Assets        | Value of luxury assets                      |
| Bank Assets          | Value of bank assets                        |

---

## 🖥️ Application

The application is built using **Streamlit**.

The application contains a sidebar with:

* Loan Prediction
* About Model
* How It Works
* Model Information
* Important Features

The main prediction page allows users to enter applicant information and receive a prediction.

### Prediction Output

The application displays:

```text
Loan Approved
```

or

```text
Loan Rejected
```

It also displays the estimated loan approval probability.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Transformation
   ↓
Random Forest Model
   ↓
Model Training
   ↓
Save Model (.pkl)
   ↓
Streamlit Application
   ↓
User Input
   ↓
Loan Prediction
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Joblib**
* **Streamlit**
* **Git & GitHub**

---

## 📁 Project Structure

```text
loan-approval-prediction/
│
├── app.py
├── train_model.py
├── loan_approval_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

#### `app.py`

Contains the Streamlit web application.

It handles:

* User input
* Data preprocessing
* Model prediction
* Approval probability
* Result display

#### `train_model.py`

Used for:

* Loading the dataset
* Cleaning the data
* Converting categorical variables
* Training the Random Forest model
* Saving the trained model

#### `loan_approval_model.pkl`

Contains the trained Random Forest machine learning model.

#### `requirements.txt`

Contains the Python libraries required to run the application.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hardikbang-1661/loan-approval-prediction.git
```

### 2. Navigate to the Project

```bash
cd loan-approval-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🧠 Train the Model

If you want to train the model again, place the dataset in the project directory and run:

```bash
python train_model.py
```

This will generate:

```text
loan_approval_model.pkl
```

The Streamlit application then uses this saved model for prediction.

---

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

Basic deployment process:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Select app.py
       ↓
Install requirements.txt
       ↓
Deploy Application
```

After deployment, Streamlit provides a public URL that can be shared with others.

---

## 🔮 Future Improvements

Possible improvements include:

* Add model accuracy and evaluation metrics
* Add confusion matrix
* Add feature importance visualization
* Add SHAP-based model explanations
* Compare multiple machine learning algorithms
* Add prediction history
* Generate downloadable prediction reports
* Improve UI and visualizations
* Add authentication
* Deploy the application publicly

---

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes**.

The prediction generated by this machine learning model should not be used as the sole basis for an actual financial or lending decision.

Real-world loan approval systems require additional financial, regulatory, security, fairness, and human-review considerations.

---

## 👨‍💻 Author

**Hardik**

GitHub: [@hardikbang-1661](https://github.com/hardikbang-1661)

---

## ⭐ Acknowledgement

This project was developed as a machine learning and deployment project to demonstrate:

* Data preprocessing
* Machine learning classification
* Model serialization
* Streamlit application development
* GitHub version control
* Cloud deployment
