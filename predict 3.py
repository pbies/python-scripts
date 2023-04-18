#!/usr/bin/env python3

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv('data.csv')

# Preprocess the data
X = data.drop(columns='target')
y = data['target']

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Choose a model and hyperparameters
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean squared error: {mse:.2f}')

# Fine-tune the model
if mse > acceptable_error:
    # Try adjusting the hyperparameters
    model = LinearRegression(normalize=True)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    # If the error is still too high, try a different model
    if mse > acceptable_error:
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)

# Save the model for future use
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
