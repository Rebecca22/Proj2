__author__ = "Rebecca Merriman"
from sklearn import preprocessing
from scipy.cluster.hierarchy import linkage  # ,dendrogram
from ProduceVector import ProduceVector
from Validation import Validation
# from matplotlib import pyplot as plt

"""
    This class standardises the feature vectors if it receives a frequency vector,
     calculates the euclidean distances of each of the feature vectors and then
      validates the clusters produced by the dendograms.
    used https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
"""

euclideanDistance = 0
standardisation = 0
bestCluster = 0


def getEuclideanDistance():
    """
        Method should return a euclidean distance matrix of the vector
        :return the Euclidean Distance linkage matrix of the vector
    """
    global euclideanDistance
    return euclideanDistance


def calculateEuclideanDistance(vector):
    """
        Method should calculate the euclidean distance of the vector
        :param vector: refers to the vector that will be transformed into a linkage
         matrix of euclidean distances
    """
    global euclideanDistance
    # create linkage matrix with the distance metric as euclidean distance
    # calculate the distances of the clusters by starting as singletons
    # and in each iteration will merge the two clusters which have the smallest distance
    # returns array of length n - 1
    # Z[i] will tell us which clusters were merged in the i-th iteration
    # each row has format [cluster1, cluster1, dist, sample_count].
    euclideanDistance = linkage(vector, metric='euclidean')


def getStandardisation():
    """
        Method should return a standardisation matrix of the vector
        :return the standardisation matrix of the vector
    """
    global standardisation
    return standardisation


def calculateStandardisation(vector):
    """
        Method should standardise the feature vector
        :param vector: refers to the vector that will be standardised
        # from http://sebastianraschka.com/Articles/2014_about_feature_scaling.html
    """
    global standardisation
    # from http://sebastianraschka.com/Articles/2014_about_feature_scaling.htm
    std_scale = preprocessing.StandardScaler().fit(vector)
    standardisation = std_scale.transform(vector)


def Clustering(typeVector, behaviour, sampleType):
    """
        Method should standardise the vector if the vector is a frequency vector,
        calculate the euclidean distance of the vectors and produce a dendogram.
        :param typeVector: refers to the type of vector ie. uni-gram (1-gram),
        di-gram (2-gram) or tri-gram (3-gram)
        :param behaviour: refers to the type of behaviour of the system call (full
        representation or by category)
    """
    ProduceVector.produceVector(typeVector, behaviour, sampleType)
    vector = ProduceVector.getVector()

    if sampleType == "":
        sampleType2 = "ransomware"
    if sampleType == "2":
        sampleType2 = "backdoor"
    if sampleType == "3":
        sampleType2 = "trojan"

    if (behaviour == "f") or (behaviour == "fc"):        

        calculateStandardisation(vector)
        vector = getStandardisation()

        typeOfVector = typeVector + " " + behaviour

        nGram, syscallRep = typeOfVector.split()

        if syscallRep == "b":
            nGram += "Full Representation Bit Vector"
        if syscallRep == "f":
            nGram += "Full Representation Frequency Vector"
        if syscallRep == "bc":
            nGram += "Category Bit Vector"
        if syscallRep == "fc":
            nGram += "Category Frequency Vector"


        fileName = sampleType2 + " " + syscallRep + " standardisation " + nGram + ".txt"

        file = open(fileName, "w")
        file.write(str(vector.tolist()))
        file.close()

    calculateEuclideanDistance(vector)    

    typeOfVector = typeVector + " " + behaviour

    nGram, syscallRep = typeOfVector.split()

    if syscallRep == "b":
        nGram += "Full Representation Bit Vector"
    if syscallRep == "f":
        nGram += "Full Representation Frequency Vector"
    if syscallRep == "bc":
        nGram += "Category Bit Vector"
    if syscallRep == "fc":
        nGram += "Category Frequency Vector"    

    fileName = sampleType2 + " " + syscallRep + " matrix " + nGram + ".txt"

    file = open(fileName, "w")
    file.write(str(getEuclideanDistance().tolist()))
    file.close()

    print("Producing a dendrogram")


    typeOfVector = typeVector + " " + behaviour

    setBestCluster(Validation.evaluate(getEuclideanDistance(), vector, typeOfVector, sampleType))


def getBestCluster():
    """
        Method should return the bestCluster of the matrix passed in to the evaluate
        method in the validation class
        :return the bestCluster
    """
    global bestCluster
    return bestCluster


def setBestCluster(cluster):
    """
        Method should set the bestCluster variable to the values passed in
        :param cluster: the score and number of clusters of the best clustering
    """
    global bestCluster
    bestCluster = cluster
