# starter code and guidance for ML assignment 3, option 1

## Due dates:

* Iteration 1: April 21, 11pm  
* Final: Monday, May 4 at 11:59pm 

## Assignment description 

**Data: Amazon Fine Food Reviews**. The Amazon Fine Food Reviews dataset consists of 455,000 food reviews Amazon users left up to October 2012. This is the same data file you are using for Machine Learning Assignment 1.   


You are going to use [KMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) clustering to create a **recommendation engine.** The measure of success is subjective; you know you have chosen the right features and number of clusters when the products in each cluster "seem" like they belong together. 

One limitation of the data is the lack of a feature that names the product (ProductId is included, but there is no product name). However, in most cases, the product can be deduced by reading the review summary and the first few lines of the review. 

For this assignment, you must use only the data available in `Amazon.csv`; do not augment the data with other sources (we will do that in a future assignment). However, **the original dataset will need extensive transformations and feature extractions before it will be useful for training the model**. 

#### Starter code

A [starter Jupyter notebook](https://github.com/visualizedata/ml/blob/master/ML_assignment_3/option_1/kmeans_amazon.ipynb) is included to give you a jump start on:  

* reading and restructuring the data  
* subsetting features from the full set of metadata  
* visual tools for determining the right number of clusters  
* fitting KMeans  
* assessing the results  

### Your work will be assessed on: 

* data processing and transformation  
* choosing the right number of clusters for the problem  
* the organization and documentation of your GitHub repository  
* communication of your work in class reflections and final presentations  
* model improvement over the semester

### Include with submission: 

* your Python code in a Jupyter Notebook (include all code that contributed to your final model, including data work and feature transformations)  
* plots that show why you chose the number of clusters you chose  
* clear documentation that demonstrates cluster results for "good" clusters (including photos, by cluster)
