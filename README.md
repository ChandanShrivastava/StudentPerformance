## About the project
This is a dataset about student performance in math, reading and writing based on several factors such as gender, race/ethnicity, parental level of education, access to lunch, access to a test preparatory course. For the sake of this project we will use the math scores as a target variable whose values need to be predicted and the rest of the fields will be treated as dependent variables. <br>

Since this is going to be a regression problem, we will use traditional Machine Learning algorithms like ```Linear Regression, Lasso, Ridge, K-Neighbors Regressor, Decision Tree Regressor, Random Forest Regressor, XGBRegressor, CatBoosting Regressor and Adaboost Regressor```. We will perform an analysis of the predictions of each of these algorithms and choose the one that gives us the best accuracy score after hyper-parameter tuning of the model during training.

## Deployed model
The project uses git actions to successully build the project on push to main branch.

trainNBuild.yml
Is the workflow file to build the project and create a Docker image and push the image to my docker hub.
The workflow uses self-hosted AWS EC2 instance as runner. 

https://hub.docker.com/r/shrivac2510/studentperf_api

cd.yml
This workflow gets triggered on successful completion of trainNBuild.yml and uses self-hosted AWS EC2 instance as runner. The workflow simply pulls the docker image on the EC2 instance and runs the image.