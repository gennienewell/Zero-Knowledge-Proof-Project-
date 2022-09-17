"""
ZKP: GC Authenticator (Client)
Author's: Gene Newell
"""

import socket, pickle ,random, time
from matrix import Matrix

# Try Connecting to Port.
try:
    # Create a socket connection.
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 50007
    toFrmServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    toFrmServer.connect((HOST, PORT))
except:
    print("Connection Failed!")

def infoAboutGraph():
    print("""\n     In cryptography, a zero-knowledge proof or zero-knowledge 
protocol is a method by which one party (the prover) can prove to 
another party (the verifier) that a given statement is true while the
prover avoids conveying any additional information apart from the fact
that the statement is indeed true.\n""")
    print("""\n     In graph theory and computer science, an adjacency matrix is 
a square matrix used to represent a finite graph. The elements of 
the matrix indicate whether pairs of vertices are adjacent or not in the graph.
-Wikipedia-\n""")

def colorCode():
    print("Color Codes - [0 : Turquoise, 9 : Orange, 8 : Yellow, 7 : Red, 6 : Green,\n 5 : White, 4 : Pink, 3 : Gray, 2 : blue , 1 : black]")
    

def generateGraphs(n, k):
    # Creating Initial Matrices objects for Client and Server's permutated graph.
    m, permutedMatrix = Matrix(n) , Matrix(n)

    # Information about Graph's and ZKP.
    infoAboutGraph()
    colorCode()

    # List's of Initial Graphs Vertices Order.
    verticesOrder = [i for i in range(n)]
    permutedOrder = [i for i in range(n)]

    # Permutate List for graph placement.
    random.shuffle(permutedOrder)

    print()
    print("Initial Vertex Order ->   ",verticesOrder)
    print("Permutated Vertex Order ->",permutedOrder)
    print()

    # Initalize n list's[] of k colorSets{}. 
    # Ex: [P1 = {2 , 5}, P2 = {1,4,3},P3 = {0}]
    partiansSets = [set() for i in range(k)]
    permutatedPSets = [set() for i in range(k)]

    # Add vertices to partions(Color Sets) randomly.
    c = int(0)
    for val in verticesOrder:
        # Make sure each partion set gets at least one vertex.
        if c < len(partiansSets):
            partiansSets[c].add(val) 
            c += 1
        else:
            partiansSets[random.randint(0, len(partiansSets)-1)].add(val)

    # Color Initial graph so no vertex in the set is adjacent to one another(secret)
    m.colorGraph(partiansSets)

    # For each index value in orginal list.
    x = int(0)
    for index, v in enumerate(verticesOrder):
        # Return value in the same position in permuted list.
        x = permutedOrder[index]
        #Then traverse the old list of color sets and search 
        # for the old index sets position.
        for i , subSet in enumerate(partiansSets):
            for j , num in enumerate(subSet):
                # if found 
                if v == num:
                    permutatedPSets[i].add(x) 

    # Color permuted graph for server
    permutedMatrix.colorGraph(permutatedPSets) #(Not a secret)

   # Set "sets" to hashmap
    mp1 = {}
    for i, val in enumerate(partiansSets):
        mp1[i] = val
    mp2 = {}
    for i, val in enumerate(permutatedPSets):
        mp2[i] = val
    
    # Set Class Hashmaps
    m.setMap(mp1)
    permutedMatrix.setMap(mp2)

    # Print M and P sets
    print("Color's(Partions) Sets ->", partiansSets)
    print("Permuted(Partions) Sets ->",permutatedPSets,"\n")

    # Print M and P matrices
    print("Adjacency Graph of Initial Vertices:\n")
    m.printMatrix()
    print("\nPermuted Adjacency Graph that will be sent to Server:\n")
    permutedMatrix.printMatrix()

    # return permuted matrix to main function.
    return permutedMatrix


# Main Function.
def main():
    try:
        # Client Receives Data[Vertices, Colors] from Server.
        data = toFrmServer.recv(4096)
        nodeColorList = pickle.loads(data)

        # Store Data from server and build matrix.
        Vertices = nodeColorList[0]
        Colors = nodeColorList[1]

        # Build graph aslong as colors less than nodes. 
        if Colors <= Vertices :
            print (f"\nInitial Vertices: {nodeColorList[0]} and {nodeColorList[1]} colors from Server.")
            permutedMatrix = generateGraphs(Vertices, Colors)
        else:
            print("Error Building Graph!")

        # Send Matrix to server
        graph = pickle.dumps(permutedMatrix)
        toFrmServer.send(graph)
    except:
        print("Error Sending Graph!")

    try:
        while True:
            # Receives current color to check if nodes are the same.
            data = toFrmServer.recv(4096)
            currentColor = pickle.loads(data)

            print()
            print(f"Current color sent from server is: {currentColor}")
            print()

            # Send nodes back to the server
            print(f"Nodes colored {currentColor} are {permutedMatrix.HshMap[currentColor]}")
            answer = pickle.dumps(permutedMatrix.HshMap[currentColor])
            toFrmServer.send(answer)
    except:
        pass
          
    
#Start Main Function
if __name__ == "__main__":
    main()
