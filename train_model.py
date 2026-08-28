import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

df = pd.read_csv("loan_approval_dataset.csv")


# --------------------------------------------------
# 2. Clean Column Names
# --------------------------------------------------

df.columns = df.columns.str.strip()


# --------------------------------------------------
# 3. Check Loan Status Values
# --------------------------------------------------

print("Loan status values before cleaning:")
print(df["loan_status"].value_counts(dropna=False))


# --------------------------------------------------
# 4. Clean Loan Status
# --------------------------------------------------

df["loan_status"] = (
    df["loan_status"]
    .astype(str)
    .str.strip()
    .str.lower()
)


df["loan_status"] = df["loan_status"].map({
    "approved": 1,
    "rejected": 0
})


# --------------------------------------------------
# 5. Remove Rows With Missing Target
# --------------------------------------------------

df = df.dropna(subset=["loan_status"])


# --------------------------------------------------
# 6. Remove Loan ID
# --------------------------------------------------

df = df.drop(columns=["loan_id"])


# --------------------------------------------------
# 7. Convert Categorical Variables
# --------------------------------------------------

df["education"] = (
    df["education"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map({
        "graduate": 1,
        "not graduate": 0
    })
)


df["self_employed"] = (
    df["self_employed"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map({
        "yes": 1,
        "no": 0
    })
)


# --------------------------------------------------
# 8. Select Features
# --------------------------------------------------

features = [
    "no_of_dependents",
    "education",
    "self_employed",
    "income_annum",
    "loan_amount",
    "loan_term",
    "cibil_score",
    "residential_assets_value",
    "commercial_assets_value",
    "luxury_assets_value",
    "bank_asset_value"
]


X = df[features]
y = df["loan_status"]


# --------------------------------------------------
# 9. Remove Rows With Missing Values
# --------------------------------------------------

valid_rows = X.notna().all(axis=1) & y.notna()

X = X[valid_rows]
y = y[valid_rows]


# --------------------------------------------------
# 10. Check Data
# --------------------------------------------------

print("\nFinal dataset shape:")
print(X.shape)

print("\nMissing values in X:")
print(X.isna().sum())

print("\nMissing values in y:")
print(y.isna().sum())


# --------------------------------------------------
# 11. Create Random Forest Model
# --------------------------------------------------

model = RandomForestClassifier(
    bootstrap=False,
    criterion="gini",
    max_depth=None,
    random_state=42
)


# --------------------------------------------------
# 12. Train Model
# --------------------------------------------------

model.fit(X, y)


# --------------------------------------------------
# 13. Save Model
# --------------------------------------------------

joblib.dump(model, "loan_approval_model.pkl")


print("\n--------------------------------")
print("Model trained successfully!")
print("--------------------------------")
print("Model saved as:")
print("loan_approval_model.pkl")