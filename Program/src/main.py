__author__ = "Rebecca Merriman"
from HierarchicalClustering import HierarchicalClustering
import cPickle as pickle

def main():


    import sys
    print("What would you like to execute?\n Please type 'r' if you want to run the "
          "analysis for ransomware\n please type 'b' if you want to to run the "
          "analysis for backdoor\n or please type 't' if you want to to run the "
          "analysis for trojan\n and then press enter (without the quote marks)")

    answer = (sys.stdin.readline())
    sampleType = ""
    if answer == "r\n":
        sampleType = ""
    elif answer == "b\n":
        sampleType = "2"        
    elif answer == "t\n":
        sampleType = "3"
    else:
        print "You have entered an incorrect input"
        exit(0)
    
    # bit vector with full representation
    print("Running experiment for Uni-gram bit vector with full representation")
    HierarchicalClustering.Clustering(typeVector="uni", behaviour="b", sampleType = sampleType)
    # frequency vector with full representation
    print("Running experiment for Uni-gram frequency vector with full "
          "representation")
    HierarchicalClustering.Clustering(typeVector="uni", behaviour="f", sampleType = sampleType)
    # bit vector with category
    print("Running experiment for Uni-gram bit vector with category")
    HierarchicalClustering.Clustering(typeVector="uni", behaviour="bc", sampleType = sampleType)
    # frequency vector with category
    print("Running experiment for Uni-gram frequency vector with category")
    HierarchicalClustering.Clustering(typeVector="uni", behaviour="fc", sampleType = sampleType)

    # di-gram
    # bit vector with full representation
    print("Running experiment for Di-gram bit vector with full representation")
    HierarchicalClustering.Clustering(typeVector="di", behaviour="b", sampleType = sampleType)
    # frequency vector with full representation
    print("Running experiment for Di-gram frequency vector with full "
          "representation")
    HierarchicalClustering.Clustering(typeVector="di", behaviour="f", sampleType = sampleType)
    # bit vector with category
    print("Running experiment for Di-gram bit vector with category")
    HierarchicalClustering.Clustering(typeVector="di", behaviour="bc", sampleType = sampleType)
    # frequency vector with category
    print("Running experiment for Di-gram frequency vector with category")
    HierarchicalClustering.Clustering(typeVector="di", behaviour="fc", sampleType = sampleType)

    # tri-gram
    # bit vector with full representation
    print("Running experiment for Tri-gram bit vector with full representation")
    HierarchicalClustering.Clustering(typeVector="tri", behaviour="b", sampleType = sampleType)
    # frequency vector with full representation
    print("Running experiment for Tri-gram frequency vector with full "
          "representation")
    HierarchicalClustering.Clustering(typeVector="tri", behaviour="f", sampleType = sampleType)
    # bit vector with category
    print("Running experiment for Tri-gram bit vector with category")
    HierarchicalClustering.Clustering(typeVector="tri", behaviour="bc", sampleType = sampleType)
    # frequency vector with category
    print("Running experiment for Tri-gram frequency vector with category")
    HierarchicalClustering.Clustering(typeVector="tri", behaviour="fc", sampleType = sampleType)


if __name__ == '__main__':
    main()
