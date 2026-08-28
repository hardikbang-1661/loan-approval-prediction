import streamlit as st
import pandas as pd
import joblib


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# LOAD MODEL
# ==================================================

@st.cache_resource
def load_model():
    return joblib.load("loan_approval_model.pkl")


model = load_model()


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("💳 Loan Predictor")

    st.markdown("---")

    st.subheader("📌 Navigation")

    page = st.radio(
        "Go to",
        [
            "Loan Prediction",
            "About Model",
            "How It Works"
        ]
    )

    st.markdown("---")

    st.subheader("🤖 Model Information")

    st.write("**Algorithm:** Random Forest")

    st.write("**Task:** Classification")

    st.write("**Target:** Loan Approval")

    st.write("**Classes:** Approved / Rejected")

    st.markdown("---")

    st.subheader("📊 Important Factors")

    st.write(
        """
        The model considers factors such as:

        • CIBIL Score  
        • Annual Income  
        • Loan Amount  
        • Loan Term  
        • Education  
        • Employment Status  
        • Residential Assets  
        • Commercial Assets  
        • Luxury Assets  
        • Bank Assets  
        • Number of Dependents
        """
    )

    st.markdown("---")

    st.caption(
        "ML-based prediction system"
    )


# ==================================================
# PAGE 1 — LOAN PREDICTION
# ==================================================

if page == "Loan Prediction":

    st.title("💳 Loan Approval Prediction System")

    st.write(
        "Enter the applicant's information below to predict "
        "whether the loan is likely to be approved."
    )

    st.divider()

    # ----------------------------------------------
    # APPLICANT INFORMATION
    # ----------------------------------------------

    st.header("👤 Applicant Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        dependents = st.number_input(
            "Number of Dependents",
            min_value=0,
            max_value=20,
            value=2,
            step=1
        )

        education = st.selectbox(
            "Education",
            [
                "Graduate",
                "Not Graduate"
            ]
        )

        self_employed = st.selectbox(
            "Self Employed",
            [
                "Yes",
                "No"
            ]
        )

    with col2:

        income_annum = st.number_input(
            "Annual Income (₹)",
            min_value=0,
            value=5000000,
            step=100000
        )

        loan_amount = st.number_input(
            "Loan Amount (₹)",
            min_value=0,
            value=15000000,
            step=100000
        )

        loan_term = st.number_input(
            "Loan Term (Years)",
            min_value=1,
            max_value=50,
            value=10,
            step=1
        )

    with col3:

        cibil_score = st.number_input(
            "CIBIL Score",
            min_value=0,
            max_value=900,
            value=700,
            step=1
        )

        residential_assets = st.number_input(
            "Residential Assets Value (₹)",
            min_value=0,
            value=5000000,
            step=100000
        )

        commercial_assets = st.number_input(
            "Commercial Assets Value (₹)",
            min_value=0,
            value=2000000,
            step=100000
        )


    # ----------------------------------------------
    # ADDITIONAL FINANCIAL INFORMATION
    # ----------------------------------------------

    st.header("🏠 Additional Financial Information")

    col1, col2 = st.columns(2)

    with col1:

        luxury_assets = st.number_input(
            "Luxury Assets Value (₹)",
            min_value=0,
            value=3000000,
            step=100000
        )

    with col2:

        bank_assets = st.number_input(
            "Bank Asset Value (₹)",
            min_value=0,
            value=4000000,
            step=100000
        )


    st.divider()


    # ----------------------------------------------
    # CONVERT CATEGORICAL VARIABLES
    # ----------------------------------------------

    education_value = (
        1 if education == "Graduate"
        else 0
    )

    self_employed_value = (
        1 if self_employed == "Yes"
        else 0
    )


    # ----------------------------------------------
    # PREDICTION BUTTON
    # ----------------------------------------------

    predict_button = st.button(
        "🔍 Predict Loan Status",
        type="primary",
        use_container_width=True
    )


    if predict_button:

        # ------------------------------------------
        # CREATE INPUT DATAFRAME
        # ------------------------------------------

        input_data = pd.DataFrame({

            "no_of_dependents": [
                dependents
            ],

            "education": [
                education_value
            ],

            "self_employed": [
                self_employed_value
            ],

            "income_annum": [
                income_annum
            ],

            "loan_amount": [
                loan_amount
            ],

            "loan_term": [
                loan_term
            ],

            "cibil_score": [
                cibil_score
            ],

            "residential_assets_value": [
                residential_assets
            ],

            "commercial_assets_value": [
                commercial_assets
            ],

            "luxury_assets_value": [
                luxury_assets
            ],

            "bank_asset_value": [
                bank_assets
            ]
        })


        # ------------------------------------------
        # MAKE PREDICTION
        # ------------------------------------------

        prediction = model.predict(
            input_data
        )[0]


        # ------------------------------------------
        # APPROVAL PROBABILITY
        # ------------------------------------------

        probability = model.predict_proba(
            input_data
        )[0][1]


        st.divider()

        st.header("📋 Prediction Result")


        # ------------------------------------------
        # APPROVED
        # ------------------------------------------

        if prediction == 1:

            st.success(
                "## ✅ Loan Approved"
            )

            st.write(
                "Based on the machine learning model, "
                "this applicant is predicted to be **Approved**."
            )


        # ------------------------------------------
        # REJECTED
        # ------------------------------------------

        else:

            st.error(
                "## ❌ Loan Rejected"
            )

            st.write(
                "Based on the machine learning model, "
                "this applicant is predicted to be **Rejected**."
            )


        # ------------------------------------------
        # PROBABILITY
        # ------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Approval Probability",
                f"{probability * 100:.2f}%"
            )

        with col2:

            st.metric(
                "CIBIL Score",
                cibil_score
            )


        st.progress(
            float(probability)
        )


        # ------------------------------------------
        # APPLICANT SUMMARY
        # ------------------------------------------

        st.subheader("👤 Applicant Summary")

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        with summary_col1:

            st.write("**Education**")
            st.write(education)

            st.write("**Employment**")
            st.write(
                "Self Employed"
                if self_employed == "Yes"
                else "Salaried / Other"
            )

        with summary_col2:

            st.write("**Annual Income**")
            st.write(
                f"₹{income_annum:,.0f}"
            )

            st.write("**Loan Amount**")
            st.write(
                f"₹{loan_amount:,.0f}"
            )

        with summary_col3:

            st.write("**Loan Term**")
            st.write(
                f"{loan_term} years"
            )

            st.write("**Dependents**")
            st.write(dependents)


# ==================================================
# PAGE 2 — ABOUT MODEL
# ==================================================

elif page == "About Model":

    st.title("🤖 About the Machine Learning Model")

    st.write(
        """
        This application uses a **Random Forest Classifier**
        to predict loan approval.
        """
    )

    st.divider()

    st.subheader("🌳 Random Forest")

    st.write(
        """
        Random Forest is an ensemble machine learning algorithm
        that combines multiple decision trees to produce a more
        robust classification result.
        """
    )

    st.subheader("📥 Input Features")

    features = [
        "Number of Dependents",
        "Education",
        "Self Employed",
        "Annual Income",
        "Loan Amount",
        "Loan Term",
        "CIBIL Score",
        "Residential Assets",
        "Commercial Assets",
        "Luxury Assets",
        "Bank Assets"
    ]

    for feature in features:
        st.write(f"• {feature}")

    st.divider()

    st.subheader("⚙️ Model Configuration")

    st.code(
        """
RandomForestClassifier(
    bootstrap=False,
    criterion="gini",
    max_depth=None,
    random_state=42
)
        """
    )


# ==================================================
# PAGE 3 — HOW IT WORKS
# ==================================================

elif page == "How It Works":

    st.title("⚙️ How the Application Works")

    st.write(
        "The complete machine learning pipeline is:"
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.subheader("1️⃣ Input")

        st.write(
            "The user enters applicant and financial information."
        )

    with col2:

        st.subheader("2️⃣ Processing")

        st.write(
            "The categorical values are converted into numerical values."
        )

    with col3:

        st.subheader("3️⃣ Prediction")

        st.write(
            "The Random Forest model processes the applicant data."
        )

    with col4:

        st.subheader("4️⃣ Result")

        st.write(
            "The system predicts Approved or Rejected."
        )

    st.divider()

    st.subheader("🔄 Prediction Pipeline")

    st.code(
        """
User Input
    ↓
Data Preprocessing
    ↓
Feature Vector
    ↓
Random Forest Model
    ↓
Prediction
    ↓
Approval Probability
    ↓
Approved / Rejected
        """
    )

    st.info(
        "This application is intended for educational and "
        "demonstration purposes. A real lending decision should "
        "not rely solely on an ML prediction."
    )