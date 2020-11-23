# starter code and guidance for ML assignment 3, option 3

## Assignment description 

You are going to use [KMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) to cluster data on 6,104 food recalls (because of food poisoning outbreaks) **on text describing the reason (specific food items) for the recall.** The measure of success is subjective; you know you have chosen the right features and number of clusters when the food items each cluster "seem" like they belong together. 

#### The data and goal

The description of each recall food item is verbose; e.g.: 

> River Ranch brand Diced Grn Cabbage w/Color, 4 x 5lb bag, UPC: n/a; Product is a salad item; bagged in clear polyethylene film (foodservice) and polypropylene/polyethylene (retail). Refrigerate and consume within Best By date. Product is processed and packaged by River Ranch Fresh Foods, LLC Salinas, CA

However, this does not allow for summarization by broader category (e.g., "meats," "vegetables"). Depending on how you decide to approach the problem, you might end up with large, broad clusters such as "vegetables," or smaller, specific clusters such as "bagged lettuces." It's up to you to decide what would be most useful. 

#### Starter code

A [starter Jupyter notebook](https://github.com/visualizedata/ml/blob/master/final_assignment_3/option_3/starter_code.ipynb) is included to give you a jump start on:  

* reading the metadata  
* subsetting features from the full set of metadata  
* visual tools for determining the right number of clusters  
* fitting KMeans  
* getting image names, by cluster

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
