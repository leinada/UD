"""
Disaster Response pipeline project:
This code runs the ETL pipeline that cleans data and stores in database
"""
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
     Loads and merges two input dataframes
      
     Input:
        messages_filepath:    path to messages csv file
        categories_filepath:  path to categories csv file
     Output:
        dataframe with merged data set
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages,categories,on='id')
    return df  


def clean_data(df):
    """
    cleans input data set: 
                  remove duplicates
                  convert categories from strings to binary values
    Input: 
          raw dataframe
    Output:
           cleaned dataframe
   
    """
    #split categories into separate columns
    categories = df['categories'].str.split(";", expand = True)
    #select the first row of the categories dataframe
    row = categories[:1]
    #use this row to extract a list of new column names for categories.
    category_colnames = row.apply(lambda x: x.str.split('-')[0][0], axis=0)
    categories.columns = category_colnames

    #convert category values to just numbers 0 or 1.
    for column in categories:
        #set each value to be the last character of the string
        categories[column] = categories[column].transform(lambda x: x[-1:])
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])

    # drop the original categories column from `df`
    df.drop('categories', axis = 1, inplace = True)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis = 1)

    #drop the child_alone column since the value there is always 0
    #doesn't seem to  arelevant feature for this study
    df.drop('child_alone', axis = 1, inplace = True)
    # drop duplicates
    df = df.drop_duplicates(keep='first')
    return df
    
def save_data(df, database_filename):
    """
    save cleaned data into an SQLite database.
    
    Input:
    df: dataframe with cleaned version of merged message and categories data.
    database_filename: filename for output database.
       
    Output:
    None
    """
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('df', engine, index=False,if_exists='replace')
    

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
