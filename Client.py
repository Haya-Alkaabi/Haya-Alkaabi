import socket

n = input("Welcome! Press Enter")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", 49999))

        # ask for user name and send it to the server
        client_name = input("Enter your name: ")
        client_socket.send(client_name.encode('utf-8'))
        while True:

            print("\n Menu options:")
            print("1. Search headlines")
            print("2. List of Sources")
            print("3. Quit")

            option = input("Enter the menu option:")

            if option == '1':
                client_socket.send(option.encode('utf-8'))
                print("1.1 Search for keywords")
                print("1.2 Search by category")
                print("1.3 Search by country")
                print("1.4 List all new headlines")
                print("1.5 Back to the main menu")

                while True:
                    service = input("Enter the option number:")
                    if service == '1.1':
                        client_socket.send(service.encode('utf-8'))
                        print("Search for keywords")
                        par= input("Enter the keyword: ")
                        client_socket.send(par.encode('utf-8'))
                        type_request = 'keywords'
                    elif service == '1.2':
                        client_socket.send(service.encode('utf-8'))
                        print("business, general, health, science, sports, technology")
                        par = input("Choose a category: ")
                        client_socket.send(par.encode('utf-8'))
                        type_request = 'category'
                    elif service == '1.3':
                        client_socket.send(service.encode('utf-8'))
                        print("au, ca, jp, ae, sa, kr, us, ma")
                        par = input("Choose a country: ")
                        client_socket.send(par.encode('utf-8'))
                        type_request = 'country'
                    elif service == '1.4':
                        client_socket.send(service.encode('utf-8'))
                        print("List all the new headlines")
                        par = "all"
                        client_socket.send(par.encode('utf-8'))
                        type_request = 'all'
                    elif service == '1.5':
                        client_socket.send(service.encode('utf-8'))
                        break
                    '''
                    client_socket.send('1'.encode('utf-8'))
                    client_socket.send(type_request.encode('utf-8'))
                    client_socket.send(par.encode('utf-8'))
                    '''
                    response = client_socket.recv(4069).decode('utf-8')
                    print(response)

            if option == '2':
                print("2.1 Search by category")
                print("2.2 Search by country")
                print("2.3 Search by language")
                print("2.4 List all")
                print("2.5 Back to the main menu")

                while True:
                    service = input("Enter the option number:")
                    if service == '2.1':
                        client_socket.send(service.encode('utf-8'))
                        print("business, general, health, science, sports, technology")
                        par = input("Choose a category: ")
                        client_socket.send(par.encode('utf-8'))
                        type_request = 'category'
                    elif service == '2.2':
                        client_socket.send(service.encode('utf-8'))
                        print("au, ca, jp, ae, sa, kr, us, ma")
                        par = input("Choose a country: ")
                        client_socket.send(par.encode('utf-8'))
                        type_request = 'country'
                    elif service == '2.3':
                        client_socket.send(service.encode('utf-8'))
                        print("ar, en")
                        par = input("Choose a language: ")
                        client_socket.send(par.encode('utf-8'))
                        type_request = 'language'
                    elif service == '2.4':
                        client_socket.send(service.encode('utf-8'))
                        print("List all the new headlines")
                        par = "all"
                        client_socket.send(par.encode('utf-8'))
                        type_request = 'all'
                    elif service == '2.5':
                        break

            if option == '3':
                print("Good bye!")
                exit()
