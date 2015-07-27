K-Means Text Clustering
-----------------------
A simple approach to cluster text using K-Means. Following are the steps involved. 

1. Pre-processing of input data
2. Deciding the number of clusters
3. Initialize initial positions of vectors.
4. Do K-Means
    a. Assign vectors to the closest cluster. by closer, 
       I mean the distance between the centroid of the cluster and the vector should be minimum. 
    b. Calculate centroid of each cluster
    c. Repeat step 4 until local minimum or maximum number of iterations is reached.

The problem that we try to solve here is recommendation of products based on their titles.

1. Pre-processing of input data
    I will use product titles from few e-commerce sites as my input. Text to vector representation is
    the process of simplifying input. Steps involved
       1. Remove unwanted characters which might create noise (numbers, special characters)
       2. get list of unique words from all the titles.
       3. give each word in the unique list a numerical id, each unique word represents
          a dimension, and list of dimensions form a vector
       4. each dimension in the vector is represented by number of times that particular dimension/word has appeared in the title.

       This process is well explained <a href="http://en.wikipedia.org/wiki/Bag-of-words_model"> here </a>
       The following code does it

       <- bag_of_words_gen.py ->

2. Determine the number of clusters
    There are <a href="http://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set"> many ways </a> to
    determine the number of clusters. For this experiment im expecting 10 clusters.

    k = 10

3. Initialize initial positions
    Initial k positions are Randomly selected and assumed as centroid of the required k clusters.

4. Do K-Means

    a. Assign data points to closer cluster
        For each vector, calculate euclidean distance between each centroids and assign
    b. Calculate center of each cluster
    c. Repeat step 4, 5 until local minimum or reaching maximum number of iterations.

    The euclidean distance between a vector and a centroid should be minimum.
    So we calculate distance between each vector with every other cluster.
    Once we find the vector with minimum distance with one of the k clusters.
        a. We add that vector to the cluster with minimum distance
        b. we remove the same from other clusters.

    While adding and removing vectors, the centroid of the cluster changes.



