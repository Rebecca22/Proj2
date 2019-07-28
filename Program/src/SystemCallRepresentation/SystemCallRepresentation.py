__author__ = "Rebecca Merriman"
from JsonFiles import ReadFromJsonFiles

"""
    This class produces a list of syscalls from the files and returns it depending
    on the type of syscall behaviour being represented ie. full representation or
    by category.
"""
dictionaries = {}
syscalls = []  # stores all the names of the system calls in a list for each family
allSystemCallNames = dict()  # stores every system call key observed for each family
#  where each key = the number of the family
syscallsPerFamily = {}  # stores the names of the system calls per family
idPerSample = []  # contains the id of the samples
allIds = []  # contains the ids of all the samples per family
allIdFamily = {}  # stores ids of files per family


def getSystemCallRepresentation(typeSyscall, sampleType):
    """
        Method should return the list of all syscalls seen in the json files in each
        family. It should distinguish between the type of behaviour to represent.
        :param typeSyscall: refers to the type of behaviour of the system call ie.
        by full representation or category.
        :return: list of all syscalls seen in the json files in each family
    """

    global syscalls, syscallsPerFamily, allSystemCallNames, allIds, allSyscalls,\
        dictionaries
    allSyscalls = []
    syscalls = []
    ReadFromJsonFiles.readJsonFile(sampleType)
    familiesDictionary = ReadFromJsonFiles.getFamiliesDictionary()
    numOfFamilies = ReadFromJsonFiles.getNumberOfFamilies()

    # checks all traces in every family and adds any syscalls or category to a list
    for family in range(0, numOfFamilies):
        syscallsPerFamily = {}
        allIds = []

        dictionary = familiesDictionary[family][0]['properties']

        syscallsList = []
        syscallsList = dictionary.keys()

        syscalls = []

        for syscall in syscallsList:
            if typeSyscall == "bc" or typeSyscall == "fc":
                temp1 = syscall.split("_", 1)[0]
                syscalls.append(temp1)
                allSyscalls.append(temp1)
            else:
                syscalls.append(syscall)
                allSyscalls.append(syscall)

        # store all syscalls in a dictionary with the key being the number of the
        # system call
        syscallsDictionary = {}
        i = 0
        for syscall in syscalls:
            syscallsDictionary[i] = syscall
            i += 1

        dictionarySyscallandValues = {}

        # stores in a dictionary each system call with each instance that executes
        # the system call
        i = 0
        for value in dictionary.values():
            listValues = []
            listValues = value.split()  # split the string by " "
            dictionarySyscallandValues[syscallsDictionary[i]] = listValues
            i += 1

        del dictionarySyscallandValues['label']

        # create dictionary of each instance with the system calls called for each
        # instance
        dictionaryFilesAndSyscalls = {}
        for syscall in dictionarySyscallandValues:
            for jsonFile in dictionarySyscallandValues[syscall]:
                listOfSyscalls = []
                if jsonFile in dictionaryFilesAndSyscalls:
                    listOfSyscalls = dictionaryFilesAndSyscalls[jsonFile]
                    listOfSyscalls.append(syscall)
                    dictionaryFilesAndSyscalls[jsonFile] = listOfSyscalls
                else:
                    listOfSyscalls.append(syscall)
                    dictionaryFilesAndSyscalls[jsonFile] = listOfSyscalls
        
        count = 0
        for key in dictionaryFilesAndSyscalls:
            syscallsPerFamily[count] = dictionaryFilesAndSyscalls[key]
            count += 1

        dictionaries[family] = dictionaryFilesAndSyscalls

        # add all system calls observed per file per family to a dictionary
        allSystemCallNames[family] = syscallsPerFamily
        
    # add all ids per json file per family to a dictionary
    for fam in range(0, numOfFamilies):
        allIds = []
        for jsonFile in dictionaries[fam]:
            allIds.append(jsonFile)
        allIdFamily[fam] = allIds

    # remove label
    syscalls = [x for x in syscalls if x != 'label']
    allSyscalls = [x for x in allSyscalls if x != 'label']
    return allSyscalls


def getAllSystemCallNames():
    """
        Method should return the dictionary of all the system call names
        :return: the dictionary allSystemCallNames
    """
    global allSystemCallNames
    return allSystemCallNames


def getAllSamplesIds():
    """
        Method should return the dictionary of all the id's of each file in each family
        :return: dictionary of all the id's of each file in each family
    """
    global allIdFamily
    return allIdFamily
