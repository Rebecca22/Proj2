__author__ = "Rebecca Merriman"
from SystemCallRepresentation import SystemCallRepresentation
import numpy as np
import cPickle as pickle

"""
    This class produces a vector depending if it is a bit vector, frequency vector or 
    n-gram and returns it.
"""
vector = 0
expectedVectors = {}


def getVector():
    """
        Method should return the vector
        :return: the vector called vector
    """
    global vector
    return vector


def setVector(vec):
    """
        Method should set the vector to the value passed in.
        :param vec: set the global parameter vector to vec
    """
    global vector
    vector = vec


def produceVector(typeVector, behaviour, sampleType):
    """
        Method should produce the vector according to the type (uni = uni-gram,
        d = di-gram vector and t = tri-gram vector).
        :param typeVector: refers to the type of vector ie. uni-gram (1-gram),
        di-gram (2-gram) or tri-gram (3-gram)
        :param behaviour: refers to the type of behaviour of the system call (full
        representation or by category)
    """
    global vector, expectedVectors
    expectedVectors = {}

    from collections import OrderedDict
    systemCallDictionary = OrderedDict()  # stores every system call for each family

    systemCallsRep = SystemCallRepresentation.getSystemCallRepresentation(behaviour, sampleType)


    print("Producing the feature vectors")

    # set up keys for dictionary
    systemCallDictionary = setUpKeys(systemCallsRep, typeVector, systemCallDictionary, behaviour, sampleType)

    allSystemCallsDictionary = dict()  # stores every system call for each family

    allSysCalls = SystemCallRepresentation.getAllSystemCallNames()
    syscallsLength = len(allSysCalls)
    allIdFamily = SystemCallRepresentation.getAllSamplesIds()

    # loops for all the samples, sets up the key in the dictionary according to
    # uni-gram, di-gram or tri-gram and then sets the value at the key to 1 if
    # it is a bit vector or increments the value at the key to 0 if it is a
    # frequency vector
    for sample in range(0, syscallsLength):
        expectedVectors[sample] = list()
        sampleLen = len(allSysCalls[sample])

        for listIndex in range(0, sampleLen):
            listSyscalls = allSysCalls[sample][listIndex]
            listIds = allIdFamily[sample][listIndex]   

            length = len(listSyscalls)
            if typeVector == "di":
                length -= 1
            if typeVector == "tri":
                length -= 2

            # setting up the key in the dictionary
            for index in range(0, length):
                if typeVector == "uni":
                    # set the key to the system call at the corresponding index
                    # of the list to a uni-gram
                    key = "%s" % (listSyscalls[index])                   
                elif typeVector == "di":
                    # set nextKey to the next system call in the list
                    # concatenate the next system call in the list to the
                    # previous system call set the key to the system call
                    # at the corresponding index of the list to a di-gram
                    nextIndex = index + 1
                    nextKey = listSyscalls[nextIndex]
                    key = "%s  %s" % (listSyscalls[index], nextKey)
                else:
                    # set nextKey to the next system call in the list
                    # set nextKey2 to the next system call in the list after nextKey
                    # concatenate the next system call and the one after that in
                    # the list to the name of the previous system call
                    # set the key to the system call at the corresponding index
                    # of the list to a tri-gram
                    nextIndex = index + 1
                    followingIndex = index + 2
                    nextKey = listSyscalls[nextIndex]
                    nextKey2 = listSyscalls[followingIndex]
                    key = "%s  %s  %s" % (listSyscalls[index], nextKey, nextKey2)

                # setting up the value of the key in the dictionary
                # if it is a bit vector set the key calculated above to 1
                if (behaviour == "b") or (behaviour == "bc"):
                    systemCallDictionary[key] = 1
                else:
                    # otherwise it is a frequency vector increment the value by 1
                    systemCallDictionary[key] += 1
                
            # adds the dictionary containing the vector of system calls per file
            # per family to the dictionary containing the vector of system calls
            # for all json files
            fileName = listIds + str(sample)
            allSystemCallsDictionary[fileName] = systemCallDictionary.values()

            expectedVectors[sample].append(systemCallDictionary.values())

            # sets all keys in dictionary to 0
            systemCallDictionary = systemCallDictionary.fromkeys(
                systemCallDictionary.keys(), 0)            
        

    # convert to numpy array
    setVector(np.array(allSystemCallsDictionary.values()))
    setExpectedVector(expectedVectors) 

    shape = int(vector.shape[1])

    print "The number of system call dimensions is:", shape

    typeOfVector = typeVector + " " + behaviour
    # update the pickle files with the updated lists
    nGram, syscallRep = typeOfVector.split()

    if syscallRep == "b":
        nGram += "Full Representation Bit Vector"
    if syscallRep == "f":
        nGram += "Full Representation Frequency Vector"
    if syscallRep == "bc":
        nGram += "Category Bit Vector"
    if syscallRep == "fc":
        nGram += "Category Frequency Vector"

    if sampleType == "":
        sampleType = "ransomware"
    if sampleType == "2":
        sampleType = "backdoor"
    if sampleType == "3":
        sampleType = "trojan"

    fileName = sampleType + " " + syscallRep + " vector " + nGram + ".txt"

    file = open(fileName, "w")
    file.write(str(allSystemCallsDictionary))
    file.close()


def getExpectedVector():
    """
        Method should return the expectedVectors dictionary
        :return: the dictionary called expectedVectors
    """
    global expectedVectors
    return expectedVectors


def setExpectedVector(expectedVec):
    """
        Method should set the expectedVectorDictionary to the value passed in.
        :param expectedVec: set the expectedVectorDictionary to expectedVec
    """
    global expectedVectors
    expectedVectors = expectedVec


def setUpKeys(systemCallsRep, typeVector, systemCallDictionary, behaviour, sampleType):
    """
        Method should set up the keys in the systemCallDictionary depending on the
        type of vector passed in.
        :param systemCallsRep the system call representation from
        getSystemCallRepresentation in the SystemCallRepresentation class
        :param typeVector: refers to the type of vector ie. uni-gram (1-gram),
        di-gram (2-gram) or tri-gram (3-gram)
        :param systemCallDictionary stores every system call for each family
        :return the dictionary containing the keys in the systemCallDictionary
         depending on the type of vector passed in.
    """
    # creates all the keys for the uni-gram, di-gram or tri-gram
    # loops for the all the json files in all the families and adds all keys
    # to dictionary
    
  
    systemCallsRepLength = len(systemCallsRep)
    if typeVector == "uni":
        # add the keys to the dictionary and set the value as 0
        systemCallDictionary = systemCallDictionary.fromkeys(systemCallsRep, 0)
    elif typeVector == "di":
        for index in range(0, systemCallsRepLength):
            # set nextKey to the next system call in the list
            # concatenate the name of the next system call in the list to the
            # name of the previous system call
            # add the key to the dictionary and set the value as 0
            for nextKey in range(1, systemCallsRepLength):
                # make sure that the index does not go out of the range of the list
                key = "%s  %s" % (systemCallsRep[index], systemCallsRep[index])
                systemCallDictionary[key] = 0
                key = "%s  %s" % (systemCallsRep[nextKey], systemCallsRep[nextKey])
                systemCallDictionary[key] = 0
                key = "%s  %s" % (systemCallsRep[index], systemCallsRep[nextKey])
                systemCallDictionary[key] = 0
                key = "%s  %s" % (systemCallsRep[nextKey], systemCallsRep[index])
                systemCallDictionary[key] = 0
    else:
        # set nextKey to the next system call in the list
        # set nextKey2 to the next system call in the list after nextKey
        # concatenate the name of the next system call and the one after that in
        # the list to the name of the previous system call
        # add the key to the dictionary and set the value as 0
        for index in range(0, systemCallsRepLength):
            for nextIndex in range(1, systemCallsRepLength):
                for followingIndex in range(2, systemCallsRepLength):
                    key = "%s  %s  %s" % (systemCallsRep[index],
                                          systemCallsRep[index],
                                          systemCallsRep[index])
                    systemCallDictionary[key] = 0
                    key = "%s  %s  %s" % (systemCallsRep[nextIndex],
                                          systemCallsRep[nextIndex],
                                          systemCallsRep[nextIndex])
                    systemCallDictionary[key] = 0
                    key = "%s  %s  %s" % (systemCallsRep[followingIndex],
                                          systemCallsRep[followingIndex],
                                          systemCallsRep[followingIndex])
                    systemCallDictionary[key] = 0
                    key = "%s  %s  %s" % (systemCallsRep[index],
                                          systemCallsRep[nextIndex],
                                          systemCallsRep[followingIndex])
                    systemCallDictionary[key] = 0
                    key = "%s  %s  %s" % (systemCallsRep[index],
                                          systemCallsRep[followingIndex],
                                          systemCallsRep[nextIndex])
                    systemCallDictionary[key] = 0
                    key = "%s  %s  %s" % (systemCallsRep[nextIndex],
                                          systemCallsRep[index],
                                          systemCallsRep[followingIndex])
                    systemCallDictionary[key] = 0
                    key = "%s  %s  %s" % (systemCallsRep[nextIndex],
                                          systemCallsRep[followingIndex],
                                          systemCallsRep[index])
                    systemCallDictionary[key] = 0
                    key = "%s  %s  %s" % (systemCallsRep[followingIndex],
                                          systemCallsRep[index],
                                          systemCallsRep[nextIndex])
                    systemCallDictionary[key] = 0
                    key = "%s  %s  %s" % (systemCallsRep[followingIndex],
                                          systemCallsRep[nextIndex],
                                          systemCallsRep[index])
                    systemCallDictionary[key] = 0

    if sampleType == "":
        sampleType = "ransomware"
    if sampleType == "2":
        sampleType = "backdoor"
    if sampleType == "3":
        sampleType = "trojan"
        
    fileName = sampleType + " " + behaviour + " system call dimensions " + typeVector + ".txt"

    file = open(fileName, "w")
    file.write(str(systemCallDictionary.keys()))
    file.close()
    
    systemCallDictionary1 = {}
    
    allSysCalls = SystemCallRepresentation.getAllSystemCallNames()
    syscallsLength = len(allSysCalls)

    for sample in range(0, syscallsLength):
        sampleLen = len(allSysCalls[sample])

        for listIndex in range(0, sampleLen):
            listSyscalls = allSysCalls[sample][listIndex]
            
            length = len(listSyscalls)
            if typeVector == "di":
                length -= 1
            if typeVector == "tri":
                length -= 2
                
            # setting up the key in the dictionary
            for index in range(0, length):
                if typeVector == "uni":
                    key = "%s" % (listSyscalls[index])                   
                elif typeVector == "di":
                    nextIndex = index + 1
                    nextKey = listSyscalls[nextIndex]
                    key = "%s  %s" % (listSyscalls[index], nextKey)
                else:
                    nextIndex = index + 1
                    followingIndex = index + 2
                    nextKey = listSyscalls[nextIndex]
                    nextKey2 = listSyscalls[followingIndex]
                    key = "%s  %s  %s" % (listSyscalls[index], nextKey, nextKey2)

                systemCallDictionary1[key] = 0    
    
    print "compiled keys"
        
    return systemCallDictionary1
