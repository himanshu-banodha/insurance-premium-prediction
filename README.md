# Insurance Premium Prediction
Welcome to the Insurance Premium Prediction project! This repository contains a machine learning web application built with Python, Flask, and various machine learning libraries to predict insurance premiums based on user input data.

## Problem Statement
The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an insurance policy rather han the ineffective part.

## Features
* **User-Friendly Interface:** Simple and intuitive web interface for inputting data and predicting insurance premiums.
* **Machine Learning Models:** Utilizes machine learning algorithms to provide accurate premium predictions.
* **Data Preprocessing:** Handles data cleaning and preprocessing to ensure high-quality predictions.
* **Model Deployment:** Deploys the machine learning model using Flask for easy access and use.

## Dataset Information
[Dataset link](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction)

The insurance.csv dataset contains 1338 observations (rows) and 7 features (columns). The dataset contains 4 numerical features (age, bmi, children and expenses) and 3 nominal features (sex, smoker and region) that were converted into factors with numerical value designated for each level.

## Machine Learning Model
The machine learning model is trained on a dataset containing information about individuals' insurance premiums. The model considers features such as age, gender, BMI, number of children, smoker status, and region to predict the insurance premium.

## Data Preprocessing
* **Data Cleaning:** Handles missing values and incorrect data types.
* **Feature Encoding:** Converts categorical variables into numerical format.
* **Feature Scaling:** Normalizes the data to improve model performance.

## Model Training
The model is trained using algorithms like Linear Regression, Random Forest, Graidient Boosting regression algorithm etc.
The final model is saved as model.pkl for deployment.

## Tools and Libraries Used
* **Python:** Programming language.
* **Flask:** Web framework for deploying the application.
* **Pandas:** For data manipulation and analysis.
* **NumPy:** For numerical computations.
* **Scikit-learn:** For machine learning algorithms and model training.
* **Matplotlib/Seaborn:** For data visualization.

## Installation
To run this project locally, follow these steps:

1. Clone the repository

```
git clone https://github.com/himanshu-banodha/insurance-premium-prediction.git
cd insurance-premium-prediction
```

2. Install the required dependencies

Make sure you have Python 3.7+ and pip installed. Then, run:
```
pip install -r requirements.txt
```

3. Run the Flask app
```
python app.py
```

## Usage
1. Open your web browser and go to `http://localhost:5000`
2. Enter the required input data (e.g., age, gender, BMI, number of children, smoker status, region).
3. Click on the "Predict" button to get the insurance premium prediction.

## Thank You.
----
