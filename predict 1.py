#!/usr/bin/env python3

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Create a logistic regression model
model = LogisticRegression()

# Fit the model with the data
model.fit(X, y)

# Use the trained model to make predictions on new data
new_data = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = model.predict(new_data)

# Print the predicted class
print(prediction)
