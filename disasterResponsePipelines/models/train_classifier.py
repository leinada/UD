"""
Disaster Response pipeline project:
This code runs the ML pipeline that cleans data and stores in database
"""
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import re
import pickle
import nltk
nltk.download(['stopwords','punkt', 'wordnet'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer,TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

import xgboost
from xgboost.sklearn import XGBClassifier

def load_data(database_filepath):
    """Loads  database and get the features and labels
    Input:
        database_filepath (str): string filepath of the sqlite database
    Output:
        X :  string, Feature data, just the messages
        Y :  df, classification labels
        category_names, list, list of the category names for visualization 
    """
    engine = create_engine('sqlite:///' + database_filepath)
    df=pd.read_sql_table('df', engine)

    X = df['message']
    Y = df.drop(['message', 'genre', 'id', 'original'], axis=1)
    category_names = Y.columns.tolist()
    return X, Y, category_names
       
def tokenize(text):
    """
    Input:
        text: string,  list of text messages 
    Output:
        clean_tokens: tokenized text for ML modeling
    """
    # Convert text to lowercase and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    # Tokenize words
   
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens
    
def build_model():
    """
    Build ML pipeline
    Output:
         gridsearchcv object with optimal model parameter   
    """
   
    tmp_model=XGBClassifier()
    #print(tmp_model.get_params().keys())

    ## Create pipeline
    pipeline = Pipeline([('vect', CountVectorizer(tokenizer=tokenize)),
                         ('tfidf', TfidfTransformer(use_idf = True)),
                         ('clf', MultiOutputClassifier(estimator=tmp_model))
                        ])

 

    parameters_xgb = {
        'clf__estimator__n_estimators':[100],
        'clf__estimator__ntrees':[100,200,300],
        'clf__estimator__learning_rate':[0.01,0.1,0.5],
        'clf__estimator__gamma': [0.0,0.01,0.1],
        'clf__estimator__reg_alpha':[1e-5, 0.001, 0.1],
        'clf__estimator__seed':[42]
    }


    cv = GridSearchCV(pipeline, parameters_xgb, verbose=10, n_jobs=-1);
    return cv
    

def evaluate_model(model, X_test, Y_test, category_names):
    """
    Evalutates the model on test data
    Input: X_test, Messages to test on
           Y_test: Categories to predict
           category_names: Category label names
    """

    predicted = model.predict(X_test) #predict labels for test data
    actual=np.array(Y_test)
    
    tmp_acc=[]
    tmp_prec=[]
    tmp_recall=[]
    tmp_f1=[]
    
    for i in range(0, len(category_names)):
        tmp_actual=actual[:, i]
        tmp_pred=predicted[:, i]

        # print("====================",category_names[i],"========================")
        # print(classification_report(tmp_actual, tmp_pred))
   
        acc=accuracy_score(tmp_actual, tmp_pred)
        prec=precision_score(tmp_actual, tmp_pred,average='weighted')
        rec=recall_score(tmp_actual, tmp_pred,average='weighted')
        f1=f1_score(tmp_actual, tmp_pred,average='weighted')
        
        tmp_acc.append(acc)
        tmp_prec.append(prec)
        tmp_recall.append(rec)
        tmp_f1.append(f1)

    #create a dataframe with the metrics evaluated    
    metrics_df = pd.DataFrame(index = category_names)
    metrics_df['accuracy']=tmp_acc
    metrics_df['precision']=tmp_prec
    metrics_df['recall']=tmp_recall
    metrics_df['f1']=tmp_f1
    print(metrics_df)

    #print("==========================================================")
    #print('Mean accuracy: ', np.mean(tmp_acc))
    #print('Mean precision: ', np.mean(tmp_prec))
    #print('Mean recall: ', np.mean(tmp_recall))
    #print('Mean f1-score: ', np.mean(tmp_f1))

    print("==========================================================")
    print(metrics_df.describe())
    
def save_model(model, model_filepath):
    """
    export model to pickle file  for future visualization
    
    This function saves trained model as Pickle file, to be loaded later.
    
    Input:
        model: GridSearchCV or Scikit Pipeline object
        model_filepath -> output .pkl file path with filename
    """
    
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 42)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        #print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
