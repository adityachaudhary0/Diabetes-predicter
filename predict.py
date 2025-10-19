import joblib
import numpy as np

# Load the trained model
model = joblib.load("diabetes_model.pkl")

print("\n--- 🩺 Diabetes Prediction ---")
print("Please enter the following values:\n")

# Collect user input for all 8 features
input_ = []
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

for col in features:  # assuming the last column is 'Outcome'
    value = float(input(f"Enter value for {col}: "))
    input_.append(value)

# Convert input to numpy array and reshape
sample_data = np.array([input_])

# Make prediction
prediction = model.predict(sample_data)

# Display result
print("\n--- Result ---")
if prediction[0] == 1:
    print("🩸 The model predicts: Diabetic")
else:
    print("✅ The model predicts: Non-Diabetic")
