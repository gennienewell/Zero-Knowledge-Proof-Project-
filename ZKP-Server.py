"""
ZKP: GC Authenticator (Server)
Author's: Gene Newell, Justin Bowser, Zion Lowe, Dr. Carr
"""

import socket, pickle, random, time
from matrix import Matrix

#Try Connecting to Port.
try:
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 50007
    #Listen for client and bind socket connection.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
except:
    pass

# Handles Client
def client(client_socket, client_address):
    try:
        print(f"[Client Function] New Connection {client_address} and connected!")
        cvList = []
        k , n = random.randint(3,5) , random.randint(6,10)
        # While colors greater than vertices.
        while k > n:
            k = random.randint(3,5)
            n = random.randint(6,10)

        # Append to color  Vertex list    
        cvList.append(n)
        cvList.append(k)
        print("Send ",cvList," to client!")

        # Send number of colors and nodes.
        data = pickle.dumps(cvList)
        client_socket.send(data) 
    except:
        print("Sending Data Failed!")
    
    try:
        # Wait until client responds with matrix.
        graph = client_socket.recv(4096)
        permutedMatrix = pickle.loads(graph)

        print()
        print("Server's adjacency matrix sent from client: \n")
        permutedMatrix.printMatrix()
        print() 
    except:
        print("Graph failed to pickle properly!")

    try:    
        # What vertices(nodes) are colored(are in set) X(1-n)?
        for c, (key, currSet) in enumerate(permutedMatrix.HshMap.items()):
            print(f"[Server]: What Nodes are colored {key}?\n")
            # Sends current color(hashMap key)
            color = pickle.dumps(key)
            client_socket.send(color)

            # Receives answer and Server checks.
            recAnswer = client_socket.recv(4096)
            answer = pickle.loads(recAnswer)

            print(f"Client response: {answer}")
            #  if query true continue  else cancel connection.
            acessGranted = False
            if set(answer) == set(currSet):
                print("Vertices are correct continue!")
                acessGranted = True
                continue
            else:
                print("Vertices are incorrect continue!")
                acessGranted = False
                client_socket.close()
                break 

        # Give or Deny Access!
        if acessGranted == True:
            print("Access Granted!")
        else:
            print("Access Denied!")       
    except:
        print("Failed to Traverse Matrix!")


# Main Function.
def main():
    try:
        # Listen for one connection at a time.
        s.listen(1) 
        print ("\nServer is Listening.....")

        # Connection Accepted
        client_socket, client_address = s.accept()
        print ('Connected by', client_address)
        
        while True:
            # Send arguments to handleClient function.
            client(client_socket, client_address)
            print("[Server] Back to main function!") 
             
            # Exit connection when complete.
            print("Closing connection and return to main function!")

            # Close connection after processing 
            client_socket.close()       
            break
    except:
        pass
    
#Start main Program.
if __name__ == "__main__":
    print("[Starting] Server.....")
    main()