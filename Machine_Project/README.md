# Titanic Customer Satisfaction Prediction

This project is a machine learning project aiming to predict customer satisfaction using the Titanic dataset. The main goal is to explore different models and preprocessing techniques to achieve high accuracy and create an interactive interface for predictions using Streamlit.

## Project Outline

### 1. Importing Libraries

Loaded essential Python libraries for data analysis, visualization, and machine learning.


### 2. Exploratory Data Analysis (EDA)

Examined the dataset to understand distributions, correlations, and patterns in the data.


### 3. Handling Missing Values

Identified and treated missing values to ensure data quality.


### 4. Data Splitting

Split the dataset into training and testing sets.


### 5. Encoding

Converted categorical features into numerical values using encoding techniques.


### 6. Scaling

Standardized numerical features to improve model performance.


### 7. Handling Outliers

Detected and treated outliers to reduce their impact on model predictions.


### 8. Balancing Data

Applied techniques to balance the dataset and handle class imbalances.


### 9. Modeling

Tested several machine learning models:

1- **Logistic Regression**

2- **Random Forest**

3- **XGBClassifier**

4- **KNN**

5- **SVC**



### 10. Feature Selection

Used Feature Importance to select the most relevant features, improving model efficiency.


### 11. Final Model

**Random Forest was selected as the final model due to its superior performance.**

*Accuracy after feature selection: 94.8%*

*Accuracy before feature selection: 96.1%*



### 12. Streamlit Interface

**Built an interactive interface using Streamlit to:**

***Input new data***

***Encode it using a custom function***

***Make predictions with the trained Random Forest model***




### Goal : 

**--> The project demonstrates the full machine learning workflow, from data preprocessing and model selection to feature engineering
and deployment in an interactive web app. It allows users to predict customer satisfaction in an intuitive way.**
