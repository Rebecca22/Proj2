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
