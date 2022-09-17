# Adjacency Matrix Class
class Matrix(object):
    # Constructer
    def __init__(self, numOfVertices = None):
        # Initialize Complete Matrix(VxV) with 1's, if r == c put 0's.
        self.HshMap = None # Hash map that sets colors to nodes
        self.adjMatrix = [[ 1 for i in range(numOfVertices)] for i in range(numOfVertices)]
        for i in range(numOfVertices):
            for j in range(numOfVertices):
                self.adjMatrix[i][j] = 0 if i == j else 1

    # Color Graph
    def colorGraph(self, colorSets):
        # for each Subset in list.
        for subSet in colorSets:
            for i in subSet:
                for j in subSet:
                    # For all occurrences of curr element in subset put a Zero(0)
                    self.adjMatrix[i][j] = 0
        print()
    # Setters
    def setMap(self, map):
        self.HshMap = map 
    # Print Matrix Obj
    def printMatrix(self):
         for row in self.adjMatrix:
            for item in row:
                print(item, end = " ")
            print()