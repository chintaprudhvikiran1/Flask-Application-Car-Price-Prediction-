# Car Price Prediction Application

## Introduction

A Flask web application has been developed to allow users to input data through an HTML form and receive predictions in JSON format.This repository contains a machine learning model for predicting car prices based on various numerical features. The project is built using Python, utilizing libraries like NumPy, Pandas, and Scikit-Learn.

## Project Structure

The project consists of the following components:

 1. Dataset: A CSV file containing car data.

 2. Data Processing: Filtering relevant numerical features based on correlation with car price.

 3. Model Training: Using a Linear Regression model for price prediction.

 4. Model Storage: Saving the trained model as a pickle file.

 5. Input Validation: Defining valid feature ranges in a JSON file.

 6. Web Application: A Flask-based interface for user input and prediction output.

## Dependencies

 To run this project, install the required dependencies using pip install numpy pandas scikit-learn flask pickle-mixin.

 ### Dataset Processing

  1. Loading Data:

      The dataset is read using Pandas.

  2. Feature Selection:

      Only numerical columns with strong correlation to car price are selected.

  ### Model Training

  1. Data Splitting:

      The dataset is split into training and testing sets.

  2. Model Creation:

      A Linear Regression model is trained.

  3. Saving the Model:

     The trained model is stored as a pickle file.

  4. Input Validation

     A JSON file is created to define valid feature ranges.

  5. Web Application

     A Flask application is created to serve predictions through a web form.

## Setting up Flask:

The application initializes Flask and loads the trained model.

  1. Handling Predictions:

     When the user submits the form, the app processes the inputs and returns predictions in JSON format.

  2. Running the Application

     Start the Flask server using python app.py.

  3. Open a browser and navigate to http://127.0.0.1:5000/.

     Enter the required details and submit the form to get the predicted car price.

## Conclusion

This project demonstrates the use of machine learning for car price prediction, integrating model training, storage, and a web-based interface for user interaction. Future improvements could include additional feature selection techniques, model enhancements, and a more advanced web interface.
