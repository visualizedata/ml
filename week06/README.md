# Guidance on ML Assignment 1

### Step 0: Create randomly selected training and test subsets

This is a task you only need to do once. The training and test sets are saved as CSV files for later use. Here's a [Jupyter notebook](https://github.com/visualizedata/ml/blob/master/week06/_00_split.ipynb) you can use for guidance. In the third code cell, the `random_state` parameter needs an integer; any integer will do (I recommend the age of your favorite artist). This `random_state` parameter will control the randomness for reproducibility of the results, allowing you to get exactly the same training and test sets every time you run this. 

### Step 1: Train models on the training set

Here's a [Jupyter notebook](https://github.com/visualizedata/ml/blob/master/week06/_01_train.ipynb) you can use for guidance. In this stage, you're going through the entire process of creating a feature set and training it on several models. This includes the following:

1. Read the raw data.
2. Extract features from the natural language data (the text of the Amazon reviews.
3. Create additional quantitative features. Some already exist (review score / a.k.a. number of stars) and others can be created (e.g. the length of a review).
4. Combine all these features into a single, sparse matrix, `X`. Also create `y`, which is your vector of labels.
5. Use `X` and `y` to fit various models, with various configurations of parameter settings. 
6. Assess performance on the model fits. 

For every instance of a class that relies on a `fit` method, you'll store those instances in a pickle file for later use (`.pkl`). Here's [documentation](http://scikit-learn.org/stable/modules/model_persistence.html) on model persistence, for reference. 

### Step 2: Evaluate the performance of the various model fits on your test set

Here's a [Jupyter notebook](https://github.com/visualizedata/ml/blob/master/week06/_02_test.ipynb) you can use for guidance. This process is very similar to your work on the training set, with one important difference: for all class instances that involved data transformations and/or model fits, you should be loading the "pickled" instance and only using methods that `transform` or `predict`. In this notebook, you should not be using any methods that `fit` (including methods that also do other things, such as `fit_transform`. Any use of a method that includes the word "fit" will automatically assigned a value of 0 for all performance measures.

The `predict` methods from the pickled model fits can be used to assess the performance on the test data. Performance will often be considerably worse on the test set than performance on the training set. 

### Step 3: Prepare your submission. 

This Jupyter notebook -- [here's an example](https://github.com/visualizedata/ml/blob/master/week06/_03_submission.ipynb) -- is essentially the same as the notebook you use in Step 2, but it only includes the model fit that gives you the best performance (in this case, using Ridge Regression Classifier). 

Compress this notebook into a zip file, along with the relevant `.pkl` and files that were generated in Step 1. There's an example `.zip` file -- `submission_01.zip` -- in this repository. 

A screen shot of a directory with these contents highlighted:

![screen shot of file directory](https://github.com/visualizedata/ml/raw/master/week06/files_ss.png)

### Submit the `.zip` file you created in Step 3 to Canvas in "Assignments" no later than 5:00pm on Monday March 5. 
