# Disaster Response Pipeline Project


## Table of Contents

1. [Project Motivation and details](#project_motivation)
2. [Installation and file descriptions](#files)
3. [Instructions](#instr)

## Project Motivation and details<a name="project_motivation"></a>

This project creates an ETL and machine learning pipeline to categorize real messages that were sent during disaster events. The aim is to send the  message  directly to the appropriate aid agencies after the categorization. This project includes development of a  web app where an emergency worker can input a new message and get classification results in several categories which was built using a machine learning model. The ML script builds a pipeline that processes text and then performs multi-output classification on the 36 categories in the dataset. The web app uses the trained model to input text and return classication results and also display visualizations of the data.

## Installation and file descriptions <a name="files"></a>

#### Files:

```
- data
|- disaster_messages.csv   # csv file with messages data
|- disaster_categories.csv # csv file with messages categories
|- process_data.py         # ETL pipeline scripts to read, clean, and save data into a database
|- DisasterResponse.db     # output SQLite database of the ETL pipeline

- app
| - template
| |- master.html  # web app main page
| |- go.html   # template file used for the display of reults
|- run.py  # flask file to run the web application
|-plotlyInWordCloud.py  # file used for worldcloud visualization

- models
|- train_classifier.py #machine learning pipeline scripts to train and develop a classifier
|- classifier.pkl  # trained ML model

- README.md
```

#### Required packages:
- Python 3
- flask
- json
- joblib
- nltk
- pandas
- plotly
- numpy
- sklearn
- sqlalchemy
- sys
- re
- pickle

## Instructions <a name="instr"></a>

1. Run the following commands in the project's root directory to set up your database and model.

- To run ETL pipeline that cleans data and stores in database python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
- To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl

2. Run the following command in the app's directory to run your web app.

- python run.py

3. Go to http://0.0.0.0:3001/