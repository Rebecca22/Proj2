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

main.py -  used to run my program by running the main method. 
HierarchicalClustering package - contains a class that standardises the feature vectors if it receives a frequency vector, calculates the Euclidean Distances of each of the feature vectors and then produces a dendogram.
JsonFiles package - contains a class that gets all the folders in directory samples, and for each folder, get the json files and stores the contents of the files in a list and then store the list for each files in a family in a dictionary and returns the dictionary.
ProduceVector package - contains a class which produces a vector depending if it is a bit vector, frequency vector or n-gram and returns it.
SystemCallRepresentation package - contains a class which produces a list and returns it depending on the type of syscall behaviour being  represented ie syscall and ioctl, syscall with binder semantics, composite behaviours and ioctl or composite behaviour and binder semantics.
Validation package – contains a class that evaluates the cuts on the dendogram at different heights using metrics (FMS, F1, ARI and SC) by finding the best clustering for the matrix passed in.

##### To run the code:

To run my program, run main.py (https://github.com/ .........).

The user is asked what they should like to execute. ...... 