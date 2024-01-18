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


def myfun(conn, address):
    attempts = 0
    try:
        print("accepting Cennection From {0}".format(address))
        rmsg = conn.recv(2048).decode('utf-8')
        rmsg = re.split('-', rmsg)
        client_name = rmsg[0]
        print(client_name, "is connected to the server")



        option = conn.recv(1024).decode('utf-8')
        if not option or option.lower().replace(" ", "") == 'e' or attempts > 10:
            print(f"The Client {client_name} has disconnected.")

        counter = 0
        nmsg = ""
        email_nmsg = ""
        with open("GA7.json", 'r') as r:
            obj = json.loads(r.read())
        optionCounter = 0
        if option.lower().replace(" ", "") == "a":
            optionCounter += 1
            requestInfo(client_name, option, requestParams)
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

                nmsg += (subMessage)

            if (nmsg == ""):
                nmsg = "No data"
                conn.sendall(nmsg.encode('utf-8'))

            else:
                conn.sendall(nmsg.encode('utf-8'))

                emailoption = """Chooose one option:
                1. Download as txt file.
                2. Receive data via email.
                3. None of the above
                """
                conn.sendall(emailoption.encode('utf-8'))
                printOption = conn.recv(1048).decode('utf-8')  # receive option to print txt/email/none
                if printOption.lower().replace(" ", "") == "1":
                    Info_txtFile(client_name, option, optionCounter, nmsg)  #
                elif printOption.lower().replace(" ", "") == "2":
                    themailSender(client_name, client_email, nmsg)




        elif option.lower().replace(" ", "") == 'b':

            requestInfo(client_name, option, requestParams)
            counter = 0
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
                                         , 'Estimated Arrival Time', 'Arrival Terminal', 'Delay',
                                      'Arrival Gate']
                        , [IATA, departureAirport, departureTime,
                           estimatedArrivalTime, arrivalTerminal, delay, arrivalGate]]


                    subMessage =  f'''Flight Number#{counter}:
{optionB_table}

                                                      \n
                                                     '''
                    nmsg += subMessage
  
        elif option.lower().replace(" ", "") == 'c':
            optionCounter += 1

            conn.sendall("enter the ICAO number: ".encode('utf-8'))
            input_icao = conn.recv(10240)
            input_icao = input_icao.decode('utf-8')
            requestInfo(client_name, option, input_icao)
            input_icao = input_icao.upper().replace(" ", "")
            for flight in obj['data']:
                if flight['departure']['icao'] == input_icao:
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
                    nmsg += subMessage




        elif option.lower().replace(" ", "") == 'd':
            optionCounter += 1

            conn.sendall("Please enter flight IATA: ".encode('utf-8'))
            input_iata = conn.recv(1024)
            input_iata = input_iata.decode('utf-8')
            input_iata = input_iata.upper().replace(" ", "")
            requestInfo(client_name, option, input_iata)

            for flight in obj['data']:
                if flight['flight']['iata'] == input_iata:
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

                    nmsg +=   subMessage

            if (nmsg == ""):
                nmsg = "No data"
                conn.sendall(nmsg.encode('utf-8'))
            else:
                print("Invalid option, please try again.")
                attempts += 1

    except ConnectionResetError:
        print(f"Client {client_name} disconnected unexpectedly.")

    finally:
        conn.close()


while True:
    conn, addr = Server_Side.accept()
    Thread = threading.Thread(target=myfun, args=(conn, addr))
    Thread.start()
