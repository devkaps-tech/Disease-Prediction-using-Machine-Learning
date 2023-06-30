# Disease Prediction System using Machine Learning
This project aims to create a Disease Prediction System using machine learning algorithms. It utilizes Flask, a web framework for Python, to develop a web application that allows users to input certain parameters and predicts the likelihood of a disease based on the provided data.

## Table of Contents
### Introduction
      1.1 Overview
      1.2 Purpose
### Literature Survey
      2.1 Existing Problem
      2.2 Proposed Solution
### Usage
### Result
### Installation

## Introduction
### Overview
The project "Disease Prediction Using Machine Learning" aims to use advanced data analysis methods and machine learning algorithms to create models that can help predict diseases           early on. The project team hopes to develop accurate and effective models that can identify patterns and signs that may indicate the onset of diseases by analyzing a variety of             medical data, including patient demographics, clinical records, genetic information, and lifestyle factors.

### Purpose
This initiative aims to revolutionize healthcare by using the potential of machine learning algorithms to predict diseases. The traditional way of diagnosing diseases relies on             symptoms, manual interpretation of medical data, and the knowledge of healthcare experts. However, these methods are not always accurate or timely, which can lead to delayed                diagnosis and poor patient outcomes. This initiative seeks to overcome these limitations by providing medical professionals with powerful tools for early diagnosis and intervention         using machine learning techniques.

## Literature Survey
### Existing Problem
Traditional methods in healthcare have some limitations. They rely on a manual examination of patient data and professional interpretation, which can be inaccurate, time-consuming,         and not scalable to large datasets. It can be difficult for healthcare professionals to identify small patterns and signs in large datasets, which can delay diagnosis and lead to           subpar treatment outcomes. Additionally, it is difficult to accurately determine a person's risk of developing a disease and predict future occurrences due to the complexity of             disease development and the interaction of multiple risk factors.

### Proposed Solution
Machine learning is being used to solve the limitations of traditional methods for disease prediction. Machine learning can identify hidden patterns and correlations in large amounts       of medical data, which can lead to more accurate and timely disease predictions. This is done by using advanced algorithms and data processing techniques. The proposed approach             involves creating prediction models that include multiple types of data, such as patient demographics, clinical records, genetic data, and lifestyle factors, to provide comprehensive       risk assessment tools.

### Usage
To use this Disease Prediction System, follow these steps:

Ensure you have Python installed on your system.
Install the required dependencies by running pip install flask numpy scikit-learn.
Download the pre-trained model file model.pkl and place it in the appropriate directory (as mentioned in the code).
Run the Flask application by executing the command python app.py.
Open your web browser and visit http://localhost:5000 to access the Disease Prediction System.
Fill in the required parameters in the web form and submit the data.
The system will predict the likelihood of a disease based on the provided data and display the result on the webpage.


## Result
We have tested the data with four different models, namely Support Vector Machine, Random Forest, Logistic Regression, and Decision Tree, using different feature sets.
The best model, "Random Forest classifier with 90 features," achieved 99.25% accuracy on the given dataset.
A comparison of different machine learning algorithms helped us identify the most effective approaches for predicting diseases.
Although this model helps doctors diagnose, it is important to remember that this model is not a substitute for a doctor's expertise.
The project has limitations such as data availability and can be further improved, such as incorporating additional data sources or improving the model architecture.
Further research using larger and more diverse datasets is needed to develop machine learning models that can be effectively used in real-world clinical settings.


### Installation
To run this application locally, please follow these steps:

Clone this repository or download the source code.
Ensure you have Python 3.x installed on your system.
Install the required dependencies by running pip install flask numpy scikit-learn.
Download the pre-trained model file model.pkl and place it in the appropriate directory (as mentioned in the code).
Open a terminal or command prompt and navigate to the project directory.
Run the Flask application by executing the command python app.py.
Open your web browser and visit http://localhost:5000 to access the Disease Prediction System.
