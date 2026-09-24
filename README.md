# Sales Prediction System

## 📌 Project Overview

The Sales Prediction System is a Machine Learning project that predicts sales based on advertising expenditure on TV, Radio, and Newspaper.

The project uses Multiple Linear Regression to learn the relationship between advertising expenditure and sales.

## 🎯 Objective

The main objective of this project is to predict expected sales using:

- TV Advertising Spend
- Radio Advertising Spend
- Newspaper Advertising Spend

## 🤖 Machine Learning Model

**Algorithm:** Multiple Linear Regression

The model uses three independent variables:

- TV
- Radio
- Newspaper

The dependent variable is:

- Sales

The general equation used is:

**Sales = b₀ + b₁(TV) + b₂(Radio) + b₃(Newspaper)**

After training, the model learned the following approximate equation:

**Sales = 2.3684 + 0.0443(TV) + 0.1941(Radio) + 0.0148(Newspaper)**

## 🧠 Model Training

The model is trained using Python and Scikit-learn.

The training process includes:

1. Loading the dataset
2. Selecting input features and target variable
3. Splitting the data into training and testing sets
4. Creating the Linear Regression model
5. Training the model using `model.fit()`
6. Predicting values using the trained model
7. Evaluating model performance

The model is trained in:

`train_model.py`

The main training statement is:

```python
model.fit(X_train, y_train)
