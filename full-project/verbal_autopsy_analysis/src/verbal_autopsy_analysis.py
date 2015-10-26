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
# Reading the data
# -------------------------------------------

# creating the data path
data_path = os.path.join(os.getcwd(),'..','data')


# reading the data files
df = pd.read_csv(os.path.join(data_path,'IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11_0.csv'),low_memory = False)
cb = pd.read_excel(os.path.join(data_path,'IHME_PHMRC_VA_DATA_CODEBOOK_Y2013M09D11_0.xlsx'))


# creating the results path
results_path = os.path.join(os.getcwd(),'..','results')

# calclulate the counts table for each word and write it to a csv file
for word in ['word_asthma','word_fever','word_cough']:
   table_counts = verbal_autopsy_functions.counts_per_word(df,word)
   table_counts.to_csv(os.path.join(results_path,word+'.csv'))



