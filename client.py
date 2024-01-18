#Done by: Yusuf Abdulnoor saeed, 202100829
#Done by: Ali Mohammed Alasfoor, 202100850


import socket
from prettytable import PrettyTable

#creating the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#teying to establish connection with the server.
try:
    client_socket.connect(('127.0.0.1',7779))
except:
    print("could not connect to the server")
    exit(0) 


#creating the table
Table = PrettyTable(["Client_name"])


#Enter the client name
Client_name = input("Enter your name: ")
#Send the client name to the server
Client_name = Client_name.encode('ascii')
client_socket.sendall(Client_name)

l_client = client_socket.recv().decode()
print("\n Hi ",Client_name)
print("\n")

#fnn to decoding and printing the data
def Display_data(data):
    Data = data.decode('utf-8')
    print(Data)


while True:

    try:
	    print("\n Choose one option:")
        print("1.Display arrived flights")
        print("2.Display delayed flights")
        print("3.Display flights from one specific city")
        print("4.Display details from one particular flight")
        print("5.Quit")
        option = int(input("Enter your selection: "))
        
	#Display all arrived flights
        if option == "1":
            client_socket.sendall(option.encode('utf-8'))
            data = client_socket.recv()
            Display_data(data)
	
	#Display all delayed flights
        elif option == "2":
            client_socket.sendall(option.encode('utf-8'))
            data = client_socket.recv()
            Display_data(data)
	
	#Display all flights from a specific city
        elif option == "3":
            client_socket.sendall(option.encode('utf-8'))
            city = input("Enter city code: ")
            client_socket.sendall(city.encode('utf-8'))
            data = client_socket.recv()
            Display_data(data)

	#Display details of a particular flight
        elif option == "4":
            client_socket.sendall(option.encode('utf-8'))
            flight = input("Enter flight number")
            client_socket.sendall(flight.encode('utf-8'))
            data = client_socket.recv()
            Display_data(data)
	
	#Closing the connection
        elif option == "5":
            client_socket.sendall(option.encode('utf-8'))
            print("Connection has been closed")
            print("Good Bye")
            client_socket.close()
            break
   
        else:
            print("Invalid option")
            
    except:
        print("Error connecting to server")
        break