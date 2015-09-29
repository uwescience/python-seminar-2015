---
layout: lesson
root: ../..
title: Project Organization for Reproducible Research
---

#Project Organization for Reproducible Research

Introduction
------------
####*Up until now you learnt:*

- basic Python programming
- manipulation of arrays and data frames
- displaying results
- organizing functions
- version control

####*In this session you will learn:*

- how to organize a project
- how to document code
- how to write testable programs


These lecture notes are a modified version of the materials for Reproducible Workflow by Justin Kitzes:
[https://github.com/jkitzes/datasci-lessons/blob/gh-pages/lessons/python/reproducible_workflow.md](https://github.com/jkitzes/datasci-lessons/blob/gh-pages/lessons/python/reproducible_workflow.md) 
and influenced by the works of Victoria Stodden. [Here](http://www.stanford.edu/~vcs/Papers.html) are some 
of her papers.


We will take the work you have done with the Verbal Autopsy data during the [pandas session](https://github.com/uwescience/python-seminar-2015/blob/master/pandas/01-pandas.ipynb) and transform it in  a stand alone reproducible project.

1.	Create a clear and useful directory structure for our project.
2.	Set up (and use) Git to track our changes.
3.	Add the raw data to our project.
4.	Write the core "scientific code" to perform the analysis, including tests.
5. Create a script to regenerate all results for this project.
6.	Push the button and watch the magic.


<!--Extra:

For our purposes, we can summarize the goal of reproducibility in two related 
ways, one technical and one colloquial.

In a technical sense, your goal is to __have a complete chain of custody (ie, 
provenance) from your raw data to your finished results and figures__. That is, 
you should _always_ be able to figure out precisely what data and what code 
were used to generate what result - there should be no "missing links". If you 
have ever had the experience of coming across a great figure that you made 
months ago and having no idea how in the world you made it, then you understand 
why provenance is important. Or, worse, if you've ever been unable to recreate 
the results that you once showed on a poster or (gasp) published in a 
paper...

In a colloquial sense, I should be able to sneak into your lab late at night, 
delete everything except for your raw data and your code, and __you should be 
able to run a single command to regenerate EVERYTHING, including all of your 
results, tables, and figures in their final, polished form__. Think of this as 
the "push button" workflow. This is your ultimate organizational goal as a 
computational scientist. Importantly, note that this rules out the idea of 
manual intervention at any step along the way - no tinkering with figure axes 
in a pop-up window, no deleting columns from tables, no copying data from one 
folder to another, etc. All of that needs to be fully automated.

As an added bonus, if you couple this with a version control system that tracks 
changes over time to your raw data and your code, you will be able to instantly 
recreate your results from any stage in your research (the lab presentation 
version, the dissertation version, the manuscript version, the Nobel Prize 
committee version, etc.). Wouldn't that be nice?



- Suppose your computer explodes tomorrow?
- Suppose you explode tomorrow!!! -->


1.	Setting up the project directory
------------------------------------

<!-- Let's create a project (a reasonably self-contained set of code, data, and 
results to answer a discrete scientific question) that performs analysis of the verbal autopsy data.---> 


TODO: Create a `verbal_autopsy_analysis` in a convenient place on our hard drive. You might 
want to create a main directory called `Projects` or `Research` in your home 
folder or in your Documents folder to hold the directories for all of your 
individual research projects.

TODO: Within the `verbal_autopsy_analysis` directory, create four subdirectories:
	 
		.
    	|-- data
    	|-- man
    	|-- results
    	|-- src
    
    

The `data` directory will hold all of the raw data associated with the project, 
which in this case will be the data .csv file and the codebook .xlsx file.

The `man` folder, short for manuscript, will (someday) 
contain the manuscript that we'll write describing the results of our analysis 
(you were planning on using version control for your manuscript too, weren't 
you?). 

The `results` folder will contain the results of our analysis, including 
both tables and figures. 

The `src` directory will contain all of our code.

For bonus points, do this all from the command line.

2.	Initialize a Git repository
-------------------------------

Since we want to use version control to track the development of our project, 
we'll start off right away by initializing an empty Git repository within this 
directory. 


TODO: open a Terminal window, navigate to the main 
`verbal_autopsy_analysis` directory, and run the command `git init`.

TODO: create a README.txt in `verbal_autopsy_analysis` and write a short description of this project. Commit your changes.

As you add things to the project directory, and modify old things, you'll want 
to frequently commit your changes as we discussed in the Git session.



3.	Add raw data
----------------

The data for this project can be retrieved online, but for the sake of the exercise, we will download it and place it locally.

TODO: Download the data file from [here](http://ghdx.healthdata.org/sites/default/files/%20'record-attached-files/IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11.csv) and 
place it in the `data` subdirectory.

TODO: Download the metadata from [here](http://ghdx.healthdata.org/sites/default/files/%20'record-attached-files/IHME_PHMRC_VA_DATA_CODEBOOK_Y2013M09D11.xlsx) and place it in the `data` subdirectory.

Q: Should your `data` directory be placed under version control?
 
A: Raw data should never change  =>  there's only the original version!

A reasonable rule of thumb for getting started is that if the file is 
realatively small (ours is < 100k), go ahead and commit it to the Git 
repository, as you won't be wasting much hard disk space. Additionally, the 
file will then travel with your code, so if you push your repository to Github 
(for example) and one of your collaborators clones a copy, they'll have 
everything they need to generate your results.

However, if your file is relatively large AND is backed up elsewhere, you 
might want to avoid making a duplicate copy in the `.git` directory. You can add it to the .gitignore file to avoid accidentally adding it to Github. 

TODO: Add a description of your data `README.txt` file and place it in the data 
subdirectory. You can start by copying the text bellow:


	Data downloaded from the Global Health Data Exchange website (http://ghdx.healthdata.org/) from the following link: http://ghdx.healthdata.org/sites/default/files/record-attached-files/IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11_1.csv. It includes Population Health Metrics Research Consortium Gold Standard Verbal Autopsy Adult Data 2013. Add extra details ...
	
	

At this point, your project directory should look like this:

	.
    |-- README.txt
    |-- data
    |   |-- IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11_0.csv
    |	|-- IHME_PHMRC_VA_DATA_CODEBOOK_Y2013M09D11_0.xlsx
    |-- man
    |-- results
    |-- src

TODO: Commit both the data and README files to your git repository.


Q: What if your raw data is hosted elsewhere, on a SQL 
server, for example, or a shared hard drive with your lab? What if someone changes it while you are not looking?

A: Keep a copy of the metadata associated with the dataset (it does have metadata, 
doesn't it?), which hopefully will include something like a version number and 
a last-updated date, and store this along with your results. If 
there's no metadata, try to shame your collaborators into creating some! Record the time when the data was accessed with your analysis.

4. Write code to perform analysis
---------------------------------



### Modules
*A module is a file containing Python definitions and statements.*

Good for storing functions which will be used over and over again by different programs.

Suppose the file `myModule.py` contain the code:

```
def myFunction(a):
	return(a+1)
```


Ypu can call functions from this module:

```
import myModule
a = myModule.myFunction(2)
print(a)
```

*Modules are loaded only during first import (to save time)!*

To reload a module after making changes:

```
	reload(myModule) #Python 2.7
```
or

```
	import imp
	imp.reload(myModule) # Python 3
```
 

TODO: Create a module called `verbal_autopsy_functions.py` and place it in the `src` directory.

TODO: Define a function in it: 


counts\_per_word, which takes as inputs a data frame of verbal autopsy data and a specific word, and returns a table of this form:

counts\_per_word(df,word\_womb)


|  Site      | Cause of Death| Times word_fever is mentioned| 
|------------|---------------|------------------------------|
| AP	   | AIDS        |97
|...|...| .....					|

	
	
### Testing

*Testing is an integral part of writing code!*

TODO: Create a file `test_verbal_autopsy_functions.py` inside the `src` directory.

TODO: Inside this file write statements to test your function. 

For example,

1. test if the output of the function is a data frame
2. test if the columns of the outputted data frame are as expected
3. test what happens when the input data frame is not the right form
4. ...

I give you freedom how to write these tests, just ensure when you run
```
	python test_verbal_autopsy_functions.py 
```
you will veryfy if your module works properly.

In the future seminars, we will learn how to run tests automatically (using [unittest](https://docs.python.org/2/library/unittest.html) and [nosetests](https://nose.readthedocs.org/en/latest/)).
	


<!--Modify module as little as possible, modify main file for every result needed.
(or create a notebook and call functions from there, but notebooks can get too long)!-->



### Documentation

Documentation is crucial for creating maintable code!

#### 1. Line-level comments

```
	x = 0 # set x to zero
```

This is better:

```
	# Initializing the number of objects
	x = 0
	
```

- best if they are one line long
- describe what the code is doing and why
- need to be updated with every code change

<!--not comments to you but to somebody else-->


*An out-of-date comment is worse than no comment!*

TODO: Add some comments to `verbal_autopsy_functions.py`.


#### 2. Function-level definitions

In Python, a description of a function is known as a docstring. 
Many scientific Python packages use a convention similar to the below.

    def myFunction(input1, input2):
        """
        Calculate ...

        Parameters
        ----------
        input1 : str
            Description of input1.
        input2 : array
            Description of input2.

        Returns
        -------
        result : tuple
            Decription of output.
            
        Notes
        -----
        ...
        

        """

Compare with:

```       
	help(np.zeros)
	help(pd.pivot_table)
```

Note: comments are indented!

More info on docstrings: [PEP257](http://www.python.org/dev/peps/pep-0257/) 

<!-- works with IPython, [Sphinx](http://sphinx-doc.org/).-->


TODO: Write a docstring to your function(s) in 
`verbal_autopsy_functions.py`.

#### 3. Module-level documentation

At a higher level, you should also provide some overarching documentation of 
each of your Python module files. This is usually a relatively short summary, 
compared to a function-level docstring, that states the purposes of the module 
and lists what the module contains.

    #!/usr/bin/env python

    """
    Description of module.

    Functions
    ---------
    *list functions here with a short description*

    """

TODO: Add a short module docstring to `verbal_autopsy_functions.py`.

#### 4. Package-level and user documentation

- aimed at the user

Check out [Sphinx](http://sphinx-doc.org/)!


At this point, your project directory should look like this:

	.
    |-- README.txt
    |-- data
    |   |-- IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11.csv
    |	|-- IHME_PHMRC_VA_DATA_CODEBOOK_Y2013M09D11.xlsx
    |-- man
    |-- results
    |-- src
    |   |-- verbal_autopsy_functions.py
    |   |-- test_verbal_autopsy_functions.py

TODO: Add and commit the new files (your module and test file) to your git repository.

5. The 'run-analysis' script
--------------------
Goal: create a script which performs an automatic analysis of the verbal autopsy data. The idea is 
that you will be able to start with an empty results directory, execute the 
line `python script.py` in Terminal, and have tables and figures of the analysis saved in the 
`results` directory.

TODO: Create a file called `verbal_autopsy_analysis.py` in `src`.
	
Write statements in this file which

1. read the data
2. import functions from the module `verbal_autopsy_functions.py`
3. apply the `counts_per_word` function to the words:
	 *fever*, *asthma*, *cough*, and save a table for each output as a .csv file. It is best if you make this statement automatic so that you can apply it in the future to longer lists of words, make sure you change the output name for each table.



Don't forget to add `verbal_autopsy_analysis.py` to your git repo.

6. Run the final analysis
-------------------------------

TODO: Delete everything from the `results` directory.

TODO: Execute `python verbal_autopsy_analysis.py` from your `src` subdirectory and marvel at your 
fully reproducible workflow! 

After the execution, your directory should look like the one below.

	.
    |-- README.txt
    |-- data
    |   |-- IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11.csv
    |	|-- IHME_PHMRC_VA_DATA_CODEBOOK_Y2013M09D11.xlsx
    |-- man
    |-- results
    |-- |-- counts_table_fever.csv
    |   |-- counts_table_asthma.csv
    |   |-- counts_table_cough.csv
    |-- src
    |   |-- verbal_autopsy_functions.py
    |   |-- test_verbal_autopsy_functions.py
    |   |-- verbal_autopsy_analysis.py

Q: Should we you the 
contents of the `results` directory to your git repository?

A: You do not need to do this, since the files in your `results` 
directory contain no unique information on their own. Everything you need to 
create them is contained in the `data` and `src` directories. One exception to 
this, though, might be if your analysis takes a very long time to run and the 
outputs are fairly small in size, in which case you may want to periodically 
commit (so that you can easily recover) the results associated with 
"intermediate" versions of your code.



*Organizing code and data is an art! Take our advice and find the best solution for your project!*

*Good Luck!* 