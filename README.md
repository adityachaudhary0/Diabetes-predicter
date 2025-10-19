# 🩺 Diabetes Prediction using Machine Learning

This project predicts whether a person has diabetes based on medical parameters such as glucose level, BMI, insulin, and age.  
A Logistic Regression model is trained using the **PIMA Indians Diabetes Dataset**.

---

## 📊 Project Overview

The dataset consists of diagnostic measurements for female patients of Pima Indian heritage.  
The goal is to predict whether a person has diabetes (`Outcome = 1`) or not (`Outcome = 0`).

---

## ⚙️ Tech Stack
- **Python 3.x**
- **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, Joblib

---

## 🧠 Model Development Steps
1. **Data Preprocessing**
   - Handled missing values
   - Scaled features
   - Split dataset into training and testing sets
2. **Apply technique(PCA,K-means cross validation)**

3. **Model Training**
   - Used Logistic Regression as the primary model
   - Evaluated model with accuracy, precision, recall, F1, and AUC metrics

4. **Model Saving**
   - The trained model is stored as `diabetes_model.pkl`

5. **Prediction Script**
   - `predict.py` allows interactive user input from the terminal to make predictions.

---

## 📈 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 0.80 |
| Precision | 0.71 |
| Recall | 0.36 |
| F1-Score | 0.48 |
| ROC-AUC | 0.84 |

> The model achieves a good AUC of **0.84**, indicating strong discrimination between diabetic and non-diabetic cases.

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/adityachaudhary0/Diabetes-predicter.git
cd diabetes-prediction
2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the prediction script
python predict.py


You’ll be asked to input values for all features, and the model will predict whether the person is diabetic.