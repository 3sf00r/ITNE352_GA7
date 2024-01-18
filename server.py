#Done by: Yusuf Abdulnoor saeed, 202100829
#Done by: Ali Mohammed Alasfoor, 202100850

import socket
import json
import requests
import threading
import re

Server_Side = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server_Side.bind(("127.0.0.1", 7779))

print("server is up and ready")

while True:
    icao = input("Enter the airport code in icao number ")
    str(icao)
    if len(icao) == 4:
        break
    else:
        print("Enter the airport code in 4 length ICAO number")

params = {
    'access_key': '0a1c0f6c47e99ca42111e8bdd6e8771d',
    'arr_icao': icao,
    'limit': 100
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

if api_result.status_code < 200 or api_result.status_code > 300:
    raise Exception

with open("GA7.json", "w") as f:
    json.dump(api_result.json(), f, indent=2)

Server_Side.listen(30)

def down_txt(client_name, option, optionCounter, data):{
    
}
def SendEmail(client_name, C_email, data):
    with open("data.txt", 'w') as rdr:
        rdr.write(data)
        

def HMainFunc(conn, address):
    attempts = 0
    try:
        print("accepting Cennection From {0}".format(address))
        recmsg = conn.recv(2048).decode('utf-8')
        recmsg = re.split('-', recmsg)
        client_name = recmsg[0]
        print(client_name, "is connected to the server successfully")



        option = conn.recv(1024).decode('utf-8')
        if not option or option.lower().replace(" ", "") == 'e':
            print(f"The Client {client_name} has disconnected.")

        counter = 0
        data = ""
        
        with open("GA7.json", 'r') as r:
            obj = json.loads(r.read())
            
        optionCounter = 0
        if option.lower().replace(" ", "") == "a":
            optionCounter += 1
            for flight in obj['data']:

                subMessage = ""
                if flight['flight_status'] != "active" and flight['flight_status'] != "scheduled":
                    counter += 1
                    IATA = flight['arrival']['iata']
                    departureAirport = flight['departure']['airport']
                    arrivalTime = flight['arrival']['actual']
                    arrivalTerminal = flight['arrival']['terminal']
                    arrivalGate = flight['arrival']['gate']

                    optionA_table = [['IATA', 'Departure Airport', 'arrival Time', 'arrivalTerminal', 'arrivalGate'], [IATA, departureAirport, arrivalTime,arrivalTerminal, arrivalGate]]
                    subMessage = f'''
                    Flight Number#{counter}:

{optionA_table}

                     \n
                    '''

                    data += (subMessage)
            conn.sendall(data.encode('utf-8'))

            #if (data == ""):
                #data = "No data"
                #conn.sendall(data.encode('utf-8'))
            #else:
                #conn.sendall(data.encode('utf-8'))

                #options = "options: 1. Download data as .txt file. 2. have data sent by email."
                #conn.sendall(options.encode('utf-8'))
                #printOption = conn.recv(1048).decode('utf-8') 
                #if printOption.lower().replace(" ", "") == "1":
                #    down_txt(client_name, option, optionCounter, data)  
                #elif printOption.lower().replace(" ", "") == "2":
                #    C_email=""
                #    SendEmail(client_name, C_email, data)  




        elif option.lower().replace(" ", "") == 'b':
            optionCounter += 1
            for flight in obj['data']:
                subMessage = ""
                if flight['arrival']['delay'] is not None:
                   counter += 1
                   IATA = flight['arrival']['iata']
                   departureAirport = flight['departure']['airport']
                   departureTime = flight['departure']['estimated']
                   estimatedArrivalTime = flight['arrival']['estimated']
                   arrivalTerminal = flight['arrival']['terminal']
                   delay = flight['arrival']['delay']
                   arrivalGate = flight['arrival']['gate']

                   optionB_table = [['IATA', 'Departure Airport', 'Departure Time'
                                        , 'Estimated Arrival Time', 'Arrival Terminal', 'Delay','Arrival Gate']
                       , [IATA, departureAirport, departureTime,
                          estimatedArrivalTime, arrivalTerminal, delay, arrivalGate]]

                    
                   subMessage =  f'''Flight Number#{counter}:
{optionB_table}

\\n
'''
                   data += subMessage
            conn.sendall(data.encode('utf-8'))
                    
        elif option.lower().replace(" ", "") == 'c':
            optionCounter += 1
            RIcao = conn.recv(1024)
            RIcao = RIcao.decode('utf-8')
            RIcao = RIcao.upper().replace(" ", "")
            for flight in obj['data']:
                if flight['departure']['icao'] == RIcao:
                    IATA = flight['flight']['iata']
                    departureAirport = flight['departure']['airport']
                    departureTime = flight['departure']['estimated']
                    estimatedArrivalTime = flight['arrival']['estimated']
                    departureGate = flight['departure']['gate']
                    arrivalGate = flight['arrival']['gate']
                    status = flight['flight_status']

                    optionC_table = [['IATA', 'Departure Airport', 'Departure Time'
                                         , 'Estimated Arrival Time', ' Gate', 'Arrival Gate', 'Status']
                        , [IATA, departureAirport, departureTime, estimatedArrivalTime,
                           departureGate, arrivalGate, status]]
                    subMessage = f'''
                                         Flight Number#{counter}:

{optionC_table}

                                                      \n
                                                     '''

                    data += subMessage
            conn.sendall(data.encode('utf-8'))


        elif option.lower().replace(" ", "") == 'd':
            optionCounter += 1

            Riata = conn.recv(1024)
            Riata = Riata.decode('utf-8')
            Riata = Riata.upper().replace(" ", "")

            for flight in obj['data']:
                if flight['flight']['iata'] == Riata:
                    IATA = flight['flight']['iata']
                    departureAirport = flight['departure']['airport']
                    departureGate = flight['departure']['gate']
                    departureTerminal = flight['departure']['terminal']
                    arrivalAirport = flight['arrival']['airport']
                    arrivalGate = flight['arrival']['gate']
                    arrivalTerminal = flight['arrival']['terminal']
                    status = flight['flight_status']
                    scheduledDeparture = flight['departure']['scheduled']
                    scheduledArrival = flight['arrival']['scheduled']
                    
                    optionD_table = [['IATA', 'Departure Airport', 'Departure Gate'
                                         , 'Departure Terminal', 'Arrival Airport', 'Arrival Gate'
                                                                                    'ArrivalTerminal', 'Status',
                                      'Scheduled Departure', 'Scheduled Arrival']
                        , [IATA, departureAirport, departureGate, departureTerminal,
                           arrivalAirport, arrivalGate, arrivalTerminal, status, scheduledDeparture,
                           scheduledArrival]]
                    
                
                    subMessage = f'''
                                         Flight Number#{counter}:
{optionD_table}
                                                      \n
                                                     '''
                    data += subMessage
            if (data == ""):
                data = "no data"
                conn.sendall(data.encode('utf-8'))
            else:
                conn.sendall(data.encode('utf-8'))
                
            
    except ConnectionResetError:
        print(f" client {client_name} has disconnected")
        
    finally:
        conn.close()


while True:
    conn, addr = Server_Side.accept()
    Thread = threading.Thread(target=HMainFunc, args=(conn, addr))
    Thread.start()
