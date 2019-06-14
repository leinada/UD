# Predicting customer churns with Spark

### Table of Contents

1. [Project Motivation](#motivation)
2. [Installation](#installation)
3. [Files Description](#files)
4. [Result](#Result)
5. [Acknowledgements](#ack)

## Project Motivation<a name="motivation"></a>

This is Udacity's capstone project. Sparkify is a music app, this dataset contains two months of sparkify user behavior log.  The goal of the project is to predict churned users based on user activites and attributes. Being able to predict churn can help the  company to prioritize their retention program on customers who are most likely to churn, and potentially saving millions in revenue

Check out the [blog post ](https://medium.com/) post for more details

## Installation <a name="installation"></a>

This project uses the following software and Python libraries:

- Python 3.6
- json
- pandas
- numpy
- sklearn
- re
- Spark 2.3
- Pyspark
- Matplotlib
- seaborn

You will also need to have software installed to run and execute a Jupyter Notebook. Analysis involving  Spark environment was done on  IBM Cloud (runtime with Spark Python 3.6XS (Driver with 1vCPU and 4GB RAM and 2 executors each with 1 vCPU and 4 GB RAM).


## Files Description<a name="files"></a>

```
- Sparkify_EDA_mini.ipynb                     #notebook for EDA with mini data set
- Sparkify_featModelTuning_mini_ibm.ipynb     #notebook for feature engineering and model development
- Sparkify_ML_medium_ibm.ipynb                #notebook for feature engineering and model development

```

## Result<a name="Result"></a>

Model performance on validation  data from medium set:

    |Accuracy|PySpark |
    |score   |F1 score|
    |--------|--------|
    | 0.825  | 0.7889 |

According to the results of the model,
The number of days the user active in the site has big impact. Next one is the number of advertisements the user sees followed by  average number of songs listened per session. Total thumbs up and thumps down also has reasonable effect on the users decision to continue with the service or not.

## Acknowledgements<a name="ack"></a>

The dataset is provided by Udacity team. Analysis of the medium data set is accomplished via IBM watson studio 