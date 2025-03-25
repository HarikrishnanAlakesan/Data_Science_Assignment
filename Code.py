import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("heart.csv")

# Encode categorical features
categorical_cols = ["Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"]
df_encoded = df.copy()

for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df[col])

# Split features and target
X = df_encoded.drop(columns=["HeartDisease"])
y = df_encoded["HeartDisease"]

# Standardize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Function to predict heart disease
def predict_heart_disease():
    try:
        user_input = [
            float(age_entry.get()),  # Age
            int(sex_entry.get()),  # Sex (0=Female, 1=Male)
            int(cp_entry.get()),  # Chest Pain Type (0-3)
            float(trestbps_entry.get()),  # Resting BP
            float(chol_entry.get()),  # Cholesterol
            int(fbs_entry.get()),  # Fasting Blood Sugar (0 or 1)
            int(restecg_entry.get()),  # Resting ECG (0-2)
            float(thalach_entry.get()),  # Max Heart Rate
            int(exang_entry.get()),  # Exercise Angina (0 or 1)
            float(oldpeak_entry.get()),  # ST Depression
            int(slope_entry.get()),  # ST Slope (0-2)
        ]
        user_df = pd.DataFrame([user_input], columns=X.columns)
        user_df_scaled = scaler.transform(user_df)
        prediction = model.predict(user_df_scaled)
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
        messagebox.showinfo("Prediction Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values!")

# Create GUI window
root = tk.Tk()
root.title("Heart Disease Prediction")
root.geometry("400x500")

tk.Label(root, text="Enter the following details:").pack()

labels = ["Age (29-77):", "Sex (0=Female, 1=Male):", "Chest Pain Type (0-3):", "Resting BP (94-200):", "Cholesterol (126-564):",
          "Fasting Blood Sugar (0 or 1):", "Resting ECG (0-2):", "Max Heart Rate (71-202):", "Exercise Angina (0 or 1):", "ST Depression (0-6.2):", "ST Slope (0-2):"]

entries = []
for label in labels:
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

[age_entry, sex_entry, cp_entry, trestbps_entry, chol_entry, fbs_entry, restecg_entry, thalach_entry, exang_entry, oldpeak_entry, slope_entry] = entries

tk.Button(root, text="Predict", command=predict_heart_disease).pack()

root.mainloop()
