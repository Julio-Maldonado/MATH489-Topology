import math

def singleLinkage():
    # get n amount of clusters
    n = int(input())
    
    # get all of the pairs and make them all become their own cluster
    inputClusters = input().split(" ")
    clustersLength = len(inputClusters)
    clusters = {}
    for i in range(clustersLength):
        clusters[i] = []
        clusters[i].append(list(map(int, inputClusters[i].split(","))))

    # iterate through all of the clusters - n times to create n clusters
    for i in range(clustersLength - n): 
        minDist = 999999999
        # iterate through all of the clusters and calculate the clusters with the min distance
        for j in range(clustersLength):
            for k in range(j + 1, clustersLength):
                for l in range(len(clusters[j])):
                    for m in range(len(clusters[k])):
                        val1 = (clusters[j][l][0] - clusters[k][m][0]) ** 2
                        val2 = (clusters[j][l][1] - clusters[k][m][1]) ** 2
                        dist = math.sqrt(val1 + val2)
                        if (dist < minDist):
                            minDist, i1, point2, i2 = dist, j, clusters[k][m], k
        # append the second point of the min distance pair to the first cluster
        clusters[i1].append(point2)

        # remove the second point of the min distance pair from the second cluster
        clusters[i2].remove(point2)

    # print out the clusters
    i = 1
    print("\nHere are the", n, "clusters:", end="\n\n")
    for (key, cluster) in clusters.items():
        if cluster:
            print("Cluster", i, ":", cluster)
            i += 1

def main():
    singleLinkage()

main()
