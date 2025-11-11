# Email Spam Classification using KNN and SVM
# Dataset: https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("emails.csv")

# Separate features (X) and target (y)
# The dataset has 'Email No.' as first column, 'Prediction' (1 = spam, 0 = not spam) as last column
X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --- K-Nearest Neighbors ---
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# --- Support Vector Machine ---
svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

# --- Evaluate Performance ---
print("KNN Accuracy:", accuracy_score(y_test, y_pred_knn))
print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))

print("\nKNN Classification Report:\n", classification_report(y_test, y_pred_knn))
print("\nSVM Classification Report:\n", classification_report(y_test, y_pred_svm))
