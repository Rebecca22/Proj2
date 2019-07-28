# A Novel Approach To Clustering Malware Behaviour To Improve Malware Detection

## Overview

My project implements clustering for operations of 3 different types of malware, specifically ransomware (sample), backdoor (sample2) and trojan (sample3) in order to evaluate the accuracy of clustering-based malware detection to then conclude using these results and results from other papers whether clustering malware behaviour improves malware detection. 

## Installation Requirements and Program Instructions

### Installation Requirements (see below for instructions):
*   Python 2.7.13
*   Python libraries: 
*   Scikit-learn
* Numpy
* Scipy
* Pandas
* Matplotlib 

To install the various applications/ libraries:

1.  Python 2.7.13
Install the correct python version for https://www.Python.org/downloads/release/Python-2713/  e.g. for a 64-bit operating system in windows install the Windows x86-64 MSI installer. **Note: Make sure the “Add to path” task is ticked so the Python programs are easier to type into cmd.** 
2.  “Scikit-learn” library (including numpy and scipy that scikit-learn depends on):
    1. Python has a special library installer program called "pip", install and update it to its latest version by typing in cmd: Python -m pip install -U pip setuptools
    2. The Scikit-learn website needs the “nunpy” and “scipy” libraries to be installed. For windows (other versions of OS may be readily available on the pip website) as there is no version available on the pip website, special files that pip can interpret need to be installed. Download Numpy: http://www.lfd.uci.edu/~gohlke/Pythonlibs/#numpy  (numpy‑1.13.1+mkl‑cp27‑cp27m‑win_amd64.whl ) and Scipy: http://www.lfd.uci.edu/~gohlke/Pythonlibs/#scipy  (scipy‑0.19.1‑cp27‑cp27m‑win_amd64.whl)
    3. Using cmd, navigate to “downloads” folder and type pip install numpy_file_name” and after this repeat this for scipy (as scipy depends on numpy).
    4. Finally type in cmd: pip install -U scikit-learn
3.  Any other Python libraries that are not supported by pip e.g. pandas
    1. Go to https://www.lfd.uci.edu/~gohlke/pythonlibs/#pandas and download the correct version(the same version as numpy and scipy (pandas 0.24.2 cp27 cp27m win_amd64.whl)).
    2. Using cmd, navigate to the “downloads” folder.
    3. Type in cmd: “pip install “pandas file_name”
4.  Any other Python libraries that are supported by pip e.g. matplotlib
In cmd type:
    1. In cmd type: Python -mpip install -U pip
    2. In cmd type: Python -mpip install -U matplotlib 


### User Manual:

#### Program

##### Description of the classes in src package:

main.py -  used to run my program by running the main method which runs experiments for each system call and vector representations.. 
HierarchicalClustering package - contains a class that standardises the frequency feature vectors (not bit vectors), calculates the Euclidean Distances of each of the feature vectors and then produces a dendrogram.
JsonFiles package - contains a class that gets all the folders in the specified samples folder (either ransomware, backdoor or trojan), and for each family of the specific malware, gets the json files and stores the contents of the files in a list and then stores the list for each files in a family in a dictionary and returns the dictionary.
ProduceVector package - contains a class which produces a vector depending on if it is a bit vector or frequency vector and the type n-gram and returns it.
SystemCallRepresentation package - contains a class which produces a list of system calls for each file and returns it depending on the type of syscall behaviour being represented ie full representation or category.
Validation package – contains a class that evaluates the cuts on the dendrogram at different heights using metrics (FMS, F1, ARI and SC) by finding the best clustering for the matrix passed in.

##### Google Colabatory and Git Hub(to produce the text files)

I used google colabatory to produce all the text files that the best clustering method on my local machine will use to find the best clustering for each family.

Please see https://github.com/Rebecca22/Proj2 for the code that is being run. Google colab clones my repository and then runs the main method within the program. After it has run the main method, the text files produced by my program will be downloaded.

This picture asks the user what they would like to execute. If they enter ‘r’, every experiment for each type of system call and feature vector representation will be executed for the ransomware malware family where the feature vectors will be constructed, standardised (if a frequency vector), a dendrogram will be produced and the cuts of the dendrogram at the various heights will be validated using FMS, F1, ARI and SC scores to determine the best cluster.  If they enter ‘b’ or ‘c’ then the same thing will happen as described above for ransomware but for backdoor (‘b’) or trojan (‘t’).

1.  User enters ‘r’ (same thing will happen for when the user enters ‘b’ or ‘t’):
    Here experiments for each type of vector (Uni-gram bit vector, Uni-gram frequency vector, Di-gram bit vector, Di-gram frequency vector, Tri-gram bit vector or Tri-gram frequency vector) and for each type of behaviour Full representation or Category). In each experiment, the feature vectors will be extracted from all the json files in the malware families (1 vector for every json file), standardised (if frequency vector), the Euclidean Distance is calculated on them and a dendrogram is created of the malware samples against Euclidean Distances. Next the dendrograms are cut at different heights to obtain different clusterings and the clusterings obtained are compared to the labelled dataset from Ramilli and the best clustering obtained (the method of feature selection and model construction and the cut that is the most similar as the labelled dataset) is when the Fowlkes Mallows Score, the F1-Score, the Adjusted Rand Index or the Silhouette Coefficient is the closest to 1.

    User enters ‘r’:

    The experiments for each feature vector will be run:
    1. Firstly the program, explains the type of feature vector and system call representation that it being run e.g. Running experiment for Uni-gram bit vector with full representation
    2. Next it says that it is producing the feature vectors. Here the program extracts the system calls from the malware samples, creates the dimensions of the feature vectors according to the Uni-gram, Di-gram or Tri-gram. The program prints compiled keys to tell the user that the dimensions of the feature vectors have been produced.
    3. It then populates the feature vectors according to the malware samples and whether the vector is a bit vector (1 if the system call is present in the behavioural profile or 0 otherwise) or frequency vector (the number of system calls observed in the behavioural profile according to the Uni-gram, Di-gram or Tri-gram).The program prints the number of system call dimensions of the feature vector to the user.
    4. Then a dendrogram is produced for the feature vector. Firstly if the feature vector is a frequency vector, it is standardised and then Euclidean distances are calculated and a dendrogram is constructed.
    5. Next the dendrogram produced is cut at different heights (the number of heights is displayed in the output to the user) to obtain different clusterings. The clusterings obtained are compared to the labelled dataset from Ramilli and are validated against the FMS, F1, ARI and SC scores and a graph is produced to display the scores at the different heights. 
 
 This process (steps a – e) continues for each feature vector (repeats 12 times). 
