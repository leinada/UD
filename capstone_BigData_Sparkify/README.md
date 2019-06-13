# Predicting customer churns with Spark

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Files Description](#files)
4. [Result](#Result)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

This project uses the following software and Python libraries:

Python

Spark

Pyspark

pandas

Matplotlib

Seaborn

You will also need to have software installed to run and execute a Jupyter Notebook.

If you do not have Python installed yet, it is highly recommended that you install the Anaconda distribution of Python, which already has the above packages and more included. And for Spark, you can do this using AWS or IBM Cloud.

## Project Motivation<a name="motivation"></a>

This is udacity's capstone project, using spark to analyze user behavior data from music app Sparkify.

Sparkify is a music app, this dataset contains two months of sparkify user behavior log. The log contains some basic information about the user as well as information about a single action. A user can contain many entries. In the data, a part of the user is churned, through the cancellation of the account behavior can be distinguished.

## Files Description<a name="files"></a>

**Sprakify .ipynb** Main file of the project, it demonstrates the process of using pyspark to explore the data and build the model.

## Result

According to the results of the model, it is the frequency of Thumbs Down that has the greatest impact. Churn users have more Thumbs Down. Naturally, users will leave if they are not satisfied.

udacity goals for this project
Load large datasets into Spark and manipulate them using Spark SQL and Spark Dataframes
Use the machine learning APIs within Spark ML to build and tune models
Integrate the skills you've learned in the Spark course and the Data Scientist Nanodegree program



I posted a blog with more detail, you can find it [here](https://medium.com/).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

The dataset is provided by Udacity team. Analysis of the medium data set is accomplished via IBM watson studio 