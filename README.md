Assignment name : Loan Outcome Prediction using Random Forest

********** TASK 1  *********
1. Introduction
In this project, I analyzed a dataset to predict loan outcomes using a Random Forest Classifier. The goal was to determine whether a loan would be repaid or defaulted based on various features such as loan details, user attributes, and GPS data.

2. Data Retrieval
To begin the analysis, I retrieved data from a PostgreSQL database hosted on AWS RDS. The relevant data was stored across three key tables:

Loan Outcomes: Contains information on whether the loan was repaid or defaulted.
GPS Fixes: Includes data on the user’s location history.
User Attributes: Provides details such as age, cash inflows, etc.

3. Data Exploration and Preprocessing
Loan Outcomes Distribution
I first analyzed the distribution of loan outcomes (repaid vs. defaulted). The data showed a nearly equal distribution of these outcomes, which made it a balanced classification problem.

User Age Distribution
I examined the age distribution of users to understand the demographics of individuals taking loans. This helped in identifying any age-related patterns in loan repayment behavior.

GPS Activity of Users
I explored the GPS activity for each user, which indicated how frequently users were engaging with the system. This feature could be relevant in understanding user behavior, which may influence their likelihood to repay a loan.

4. Feature Engineering
I performed several preprocessing steps to prepare the data for modeling:

I transformed the loan outcome into a binary variable, where loans marked as "repaid" were assigned a value of 1, and those marked as "defaulted" were assigned a value of 0.

To address data skewness, I applied a log transformation to the cash inflows of users, which helped to normalize the data distribution.

I also aggregated the GPS data by user, which helped in creating a summary of each user’s location activity over time. This might provide additional insights into their behavior patterns.


********** TASK 2  *********
5. Model Training
Once the data was preprocessed, I trained a Random Forest Classifier on the dataset. This model was selected because it is effective for classification problems, especially when dealing with a mix of numerical and categorical features.

6. Model Evaluation
After training the model, I evaluated its performance using metrics like accuracy, precision, recall, and F1 score. This allowed me to assess how well the model was predicting loan outcomes.

********** TASK 3  *********
I developed a Flask application to provide loan outcome predictions based on user input.

Flask Setup: The app is initialized using Flask and listens for incoming requests on the /predict endpoint.

Model Loading: I load the pre-trained machine learning model at the start using joblib.load('loan_predictor_model.pkl').

API Endpoint (/predict):

The endpoint accepts a POST request with user data in JSON format.
I convert the JSON data into a pandas DataFrame.
Any necessary preprocessing (like encoding or scaling) is applied before passing the data to the model.
The model predicts the loan outcome, and I return the result in JSON format ({'loan_outcome': prediction}).
Error Handling: In case of errors, I ensure the API responds with a 400 status code and the error message.

OUTPUT:
![image](https://github.com/user-attachments/assets/d15edd1b-4032-4435-bd47-420ae264cb66)

**********THANK YOU**********
