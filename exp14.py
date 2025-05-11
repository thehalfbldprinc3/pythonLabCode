# Import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
# ===========================
# 1. Load the Digits Dataset
# ===========================
digits = datasets.load_digits()
# ===========================
# 2. Split the Data into Training and Test Sets
# ===========================
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2, random_state=42
)
# ===========================
# 3. Create and Train the SVM Classifier
# ===========================
clf = SVC(kernel='linear')   # Using a linear kernel
clf.fit(X_train, y_train)    # Train the model
# ===========================
# 4. Make Predictions
# ===========================
y_pred = clf.predict(X_test)
# ===========================
# 5. Evaluate the Model
# ===========================
# Accuracy Score
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
# Classification Report
print("\nClassification Report:\n", classification_report(y_test, y_pred))
# ===========================
# 6. Display the Confusion Matrix
# ===========================
disp = ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()
# ===========================
# 7. Display Sample Predictions
# ===========================
fig, axes = plt.subplots(1, 5, figsize=(10, 3))
for i, ax in enumerate(axes):
    ax.set_axis_off()
    ax.imshow(X_test[i].reshape(8, 8), cmap=plt.cm.gray_r)
    ax.set_title(f"Pred: {y_pred[i]}")
plt.suptitle("Sample Test Predictions")
plt.show()