__author__ = "Rebecca Merriman"
import json
from glob import glob
import os.path
"""
    This class gets all the folders in directory samples, and for each folder,
    it will get the json files and stores the contents of the files in a list and
     then store the list for each family in a dictionary and returns the dictionary.
"""

# initialising variables
data = []  # stores the contents of each file
familiesDictionary = {}  # stores all the contents of files per directory where each
#  key = the number of directory in the folder samples
numOfFilesDictionary = {}  # stores the number of json files per directory
numberOfFamilies = 0  # stores the number of the family in the samples directory
count = 0  # stores the number of files per family


def getJsonFiles():
    """
        Method should return the list of the contents of all the json files
        :return: the global list data
    """
    global data
    return data


def readJsonFile(sampleType):
    """
        Method should read the json file and produce a list of all the contents
        Used: https://stackoverflow.com/questions/39522949/parse-a-directory-of-json-files-with
        -python
    """
    global data, count, numberOfFamilies, numOfFilesDictionary, familiesDictionary

    # gets all folders in directory
    # for each folder, it will get the json files
    # and adds the contents of the files to the list
    # adds the contents of each family to the dictionary
    numberOfFamilies = 0
    sample = '../samples'+ sampleType
    pattern = os.path.join(sample, '*')
    for file_name in glob(pattern):
        data = []
        pattern2 = os.path.join(file_name, '*.json')
        for name in glob(pattern2):
            with open(name) as jsonFile:
                data.append(json.load(jsonFile))
                jsonFile.close()

        listFiles = []
        familiesDictionary[numberOfFamilies] = data
        dictionary = familiesDictionary[numberOfFamilies][0]['properties']
        for value in dictionary.values():
            listValues = []
            listValues = value.split()  # split the string by " "
            for item in listValues:
                listFiles.append(item)
        listFiles = list(dict.fromkeys(listFiles))  # remove duplicates
        numOfFilesDictionary[numberOfFamilies] = len(listFiles)
        numberOfFamilies += 1


def getFamiliesDictionary():
    """
        Method should return the dictionary of the contents of all the json files for
        all the families
        :return: the global dictionary called familiesDictionary
    """
    return familiesDictionary


def getNumOfFilesDictionary():
    """
        Method should return the dictionary of the number of files in each family
        :return: the global dictionary called numOfFilesDictionary
    """
    global numOfFilesDictionary
    return numOfFilesDictionary


def getNumberOfFamilies():
    """
        Method should return the number of families in the samples folder
        :return: the number of families
    """
    global numberOfFamilies
    return numberOfFamilies
