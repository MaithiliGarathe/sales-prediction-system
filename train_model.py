import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Load the dataset
data = pd.read_csv("data/advertising.csv")

# Input variables
X = data[["TV", "Radio", "Newspaper"]]

# Output variable
y = data["Sales"]

# Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict sales for test data
y_pred = model.predict(X_test)

# Calculate model performance
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

# Get trained values
intercept = model.intercept_
tv_coef = model.coef_[0]
radio_coef = model.coef_[1]
newspaper_coef = model.coef_[2]

# Display results
print("======================================")
print("       SALES PREDICTION SYSTEM")
print("======================================")
print()
print("Linear Regression Formula:")
print(
    f"Sales = {intercept:.4f} "
    f"+ ({tv_coef:.4f} × TV) "
    f"+ ({radio_coef:.4f} × Radio) "
    f"+ ({newspaper_coef:.4f} × Newspaper)"
)
print()
print(f"R² Score = {r2:.3f}")
print(f"MAE = {mae:.3f}")
print()

# Save trained model values for the webpage
with open("coefficients.js", "w") as file:
    file.write("const MODEL = {\n")
    file.write(f"    intercept: {intercept},\n")
    file.write(f"    tv: {tv_coef},\n")
    file.write(f"    radio: {radio_coef},\n")
    file.write(f"    newspaper: {newspaper_coef}\n")
    file.write("};\n")

print("coefficients.js created successfully!")
print("======================================")