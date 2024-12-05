import socket
import threading
import json
from newsapi import NewsApiClient

key = '8f82fa538a7e499ebde5d4c1826c8686'
newsapi = NewsApiClient(api_key=key)

def HandlClient(clientSocket, clientAddress):
    print(f"[NEW CONNECTION] {clientAddress} connected")
    client_name = clientSocket.recv(1024).decode('utf-8')
    print(f"[CLIENT NAME] {client_name} from {clientAddress}")

    while True:
        try:
            option = clientSocket.recv(1024).decode('utf-8')
            type = clientSocket.recv(1024).decode('utf-8')
            par = clientSocket.recv(1024).decode('utf-8')
            print (f'The client chose {option} , with {type} as a request type and {par} as a parameter')

            if not option:
                break  # Client disconnected

            if option == '1':
                if type == '1.1':
                    news = newsapi.get_top_headlines(q=par, page_size=15)
                elif type == '1.2':
                    news = newsapi.get_top_headlines(category=par, page_size=15)
                elif type == '1.3':
                    news = newsapi.get_top_headlines(country=par, page_size=15)
                elif type == '1.4':
                    news = newsapi.get_top_headlines(page_size=15)

                response = json.dumps(news, ensure_ascii=False)  # Convert to JSON string
                clientSocket.send(response.encode('utf-8'))  # Send as bytes
                with open(f'{client_name}_top_headlines_{type}.json', 'w') as f:
                    json.dump(news, f, indent=4)

            if option == '2':
                if type == '2.1':
                    news = newsapi.get_sources(category=par)
                elif type == '2.2':
                    news = newsapi.get_sources(country=par)
                elif type == '2.3':
                    news = newsapi.get_sources(language=par)
                elif type == '2.4':
                    news = newsapi.get_sources(page_size=15)

                response = json.dumps(news, ensure_ascii=False)  # Convert to JSON string
                clientSocket.send(response.encode('utf-8'))  # Send as bytes
                with open(f'{client_name}_get_sources_{type}.json', 'w') as f:
                    json.dump(news, f, indent=4)

        except Exception as e:
            print(f"[ERROR] {e}")
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(("127.0.0.1",49999))
    server_socket.listen(3)

    print("# The server initiated and it is listening for client request #")

    # multithreading
    while True:
        clientSocket, clientAddress = server_socket.accept()
        print("The connection established with ",clientAddress)
        server_thread = threading.Thread(target = HandlClient, args = (clientSocket,clientAddress))
        server_thread.start()
