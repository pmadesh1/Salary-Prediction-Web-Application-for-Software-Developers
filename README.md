# Salary-Prediction-Web-Application-for-Software-Developers

This is a machine learning web application that predicts the salary of software developers based on their country, years of experience, and education level, using real-world data collected from the Stack Overflow 2022 survey - https://insights.stackoverflow.com/survey. The web application is built using the Streamlit library, which provides an interactive and user-friendly interface for users to input their data and receive a salary prediction.

The project includes data manipulation using NumPy and Pandas to create an appropriate data frame for the machine learning model. The DecisionTreeRegressor model is used to train the model, with the best value estimator obtained from GridSearchCV. The serialized model is saved using Pickle for future predictions.

DecisionTreeRegressor is a machine learning model that uses a tree structure to model the relationships between the input features and the target variable (salary in this case). It works by splitting the data based on the values of the input features to create a set of decision rules that predict the target variable. The hyperparameters of the DecisionTreeRegressor model (such as max_depth and min_samples_split) can significantly affect its performance. Therefore, it's essential to tune these hyperparameters to find the optimal set of values for the given dataset.

GridSearchCV is a hyperparameter tuning technique that exhaustively searches for the best set of hyperparameters from a predefined set of values. In this project, GridSearchCV is used to find the optimal hyperparameters for the DecisionTreeRegressor model by testing a range of values for max_depth and min_samples_split. The best value estimator obtained from GridSearchCV is then used to train the model.

This project provides an efficient and accurate way for software developers to estimate their salaries based on their qualifications and location. The open-source code and documentation can be found in this repository, along with the necessary files to run the web application.

Screen shots of web application are as follows,

![image](https://user-images.githubusercontent.com/97992645/224174593-79a81ded-4998-4c70-b81c-8dc21961e22f.png)

![image](https://user-images.githubusercontent.com/97992645/224174900-ce69269d-52dc-4d6a-ae45-69ce9cb62d51.png)

![image](https://user-images.githubusercontent.com/97992645/224175050-76d1b8af-0d91-43a3-9cd8-283d092dbc23.png)





