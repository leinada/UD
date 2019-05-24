# Disaster Response Pipeline Project


### Table of Contents

1. [Project Motivation](#project_motivation)
2. [Installation and file descriptions](#files)

## Project Motivation<a name="project_motivation"></a>

This project creates an ETL and machine learning pipeline to categorize real messages that were sent during disaster events. The aim is to send the  message  directly to the appropriate aid agencies after the categorization. This project includes development of a  web app where an emergency worker can input a new message and get classification results in several categories which was built using a machine learning model. The web app will also display visualizations of the data.

## Installation and file descriptions <a name="files"></a>

The code contained in this repository was written in HTML and Python 3, and requires the following Python packages: json, plotly, pandas, nltk, flask, sklearn, sqlalchemy, sys, numpy, re, pickle, warnings


### Files:

```
- data
|- disaster_messages.csv   # csv file with messages data
|- disaster_categories.csv # csv file with messages categories
|- process_data.py         # ETL pipeline scripts to read, clean, and save data into a database
|- DisasterResponse.db     # output database of the ETL pipeline



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

### Required packages:


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