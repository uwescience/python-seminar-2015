'''
    This module contains functions for the analysis of the verbal autopsy data.
    
    Functions
    --------
    counts_per_word
    ...

'''

import pandas as pd

def counts_per_word(df,word):
    """
        Counts the number of words for each combination of site and cause of death.
        
        Parameters
        ----------
        df: pandas data frame
            data frame in the form of the verbal autopsy data
        word: str
            string of the form 'word_fever'
        
        Returns
        -------
        counts_table: data frame
            contains the counts
    """
    # create a table which is summing all the counts of a given word with
    # colums being cause of death and rows being the sites.
    piv = pd.pivot_table(df, values=word,
                         index=['site'], columns=['gs_text34'],
                         aggfunc=sum)
                         
    # make a list of the causes
    causes = list(piv.columns)
    
    # create a new column from the index
    piv['site'] = piv.index
    
    # reorganize table by creating columns for the cause of death and the counts.
    counts_table = pd.melt(piv, id_vars=['site'], value_vars=causes,
                                              var_name='Cause of death',
                                              value_name='Times '+word+ ' is mentioned.')
    return(counts_table)

