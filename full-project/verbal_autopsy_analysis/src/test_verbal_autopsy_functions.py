# -------------------------------------------
# Loading Python modules
# -------------------------------------------

import pandas as pd
import os
import sys


# -------------------------------------------
# Loading the verbal autopsy analysis module
# -------------------------------------------
import verbal_autopsy_functions
import imp
imp.reload(verbal_autopsy_functions)


# -------------------------------------------
# Defining all tests in individual functions
# -------------------------------------------


def test_type_counts_per_word_output(df):
    df_fever = verbal_autopsy_functions.counts_per_word(df,'word_fever')
    if type(df_fever) is not pd.core.frame.DataFrame:
        print ('The  output of the type is not a data frame.')


def test_columns_counts_per_word_output(df):
    df_fever = verbal_autopsy_functions.counts_per_word(df,'word_fever')
    if list(df_fever.columns.values)!=['site', 'Cause of death','Times word_fever is mentioned.']:
        print ('The column names are not as expected.')

def test_word_existence_counts_per_word(df):
    try:
        df_fever = verbal_autopsy_functions.counts_per_word(df,'word_nonexisting')
    except KeyError:
        print ('Non-existing word causes an error.')


# -------------------------------------------
# Reading the data
# -------------------------------------------

# creating the data path
data_path = os.path.join(os.getcwd(),'..','data')


# reading the data files
df = pd.read_csv(os.path.join(data_path,'IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11_0.csv'),low_memory = False)


# -----------------------------------
# Running all tests
# -----------------------------------
test_type_counts_per_word_output(df)
test_columns_counts_per_word_output(df)
test_word_existence_counts_per_word(df)



