# Linear Regression Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import pandas as pd
import numpy as np
import joblib

df = pd.read_csv('./data/optimized_portfolio.csv') # Load data

df['Cumulative_Close'] = df['Close'].cumsum()

# Generate lagged features for 1 to 5 days
for i in range(1, 6):
    df[f'Lag_{i}'] = df['Cumulative_Close'].shift(i)

# Drop rows with NaN values resulting from the shift operation
df_lagged = df.dropna()

# Define the features and target variable
X = df_lagged[[f'Lag_{i}' for i in range(1, 6)]]
y = df_lagged['Cumulative_Close']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the testing set
y_pred = model.predict(X_test)

# Calculate the Root Mean Squared Error (RMSE) for the predictions
lr_mse = mean_squared_error(y_test, y_pred, squared=False)
lr_r2 = r2_score(y_test, y_pred)
lr_mae = mean_absolute_error(y_test, y_pred)
lr_rmse = np.sqrt(lr_mse)

print(f'Linear Regression MSE: {lr_mse:.2f}')
print(f'Linear Regression R^2: {lr_r2:.2f}')
print(f'Linear Regression MAE: {lr_mae:.2f}')
print(f'Linear Regression RMSE: {lr_rmse:.2f}')

# Save the model
joblib.dump(model, './models/linear_regression.pkl')