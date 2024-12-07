 -----ITNE352 Project---S1---2024/2025----

 
              The project Title:
"Multithreaded News Client/Server Information System"


 Group:B3
 .Section:2
 .Haya Alkaabi(202203340)
 .Muneera Almehaiza(202206145)

 
Project Description:
This project aims to develop a client-server system for exchanging current news information. It emphasizes critical aspects of client-server architecture, network communication, multithreading, API integration, and coding best practices. The server, implemented in Python, retrieves news updates from NewsAPI.org, manages multiple simultaneous client connections, and responds to various client requests. The client script, also written in Python, establishes a connection to the server to fetch and display news articles and sources. Users can easily navigate through different options to obtain specific news details or exit the application. 


Table of Contents:
1. [Requirements]
2. [How to]
3. [The Scripts]
4. [Additional Concept] 
5. [Acknowledgments] 
6. [Conclusion]
7.[Resources]


1.Requirements:
To set up and ensure an efficient run of this project on your local machine, follow these instructions:

Prerequisites
1-Python: You need to ensure Python is installed on your system, if not please download it from their website [python.org]or go to this link (https://www.python.org/downloads/).
2-NewsAPI Key: You need to Sign up on their website NewsAPI.org in order to get your API key.
Setup
1-Clone the repository
2-Create a virtual environment
3-Activate the virtual environment 

2.How to Run the System:
First Running the Server:
Open a terminal and navigate to the directory containing Server.py.
Run the server using: python Server.py
The server will start and listen for incoming connections.

Then Running the Client:
Open another terminal and navigate to the directory containing Client.py.
Run the client using: python Client.py

After this Follow the on-screen instructions to interact with the server and chocie the option from the menu ...

 3.Project Scripts
1/Server Script (Server.py)
Main Functionality: Listens for client connections, handles requests for news articles, and retrieves data from NewsAPI.
Key Packages: socket, threading, json, newsapi
Important Functions:HandleClient(clientSocket, clientAddress): Manages individual client connections and processes requests.

2/Client Script (Client.py)
Main Functionality: Connects to the server, sends requests for news articles, and displays the results.
Key Packages: socket
Important Functions:The client script prompts the user for input and sends requests accordingly.

Example from Server.py
def HandleClient(clientSocket, clientAddress):
    ...
    if option == '1':
        news = newsapi.get_top_headlines(q=par, page_size=15)

 4.Additional concept: 

5.Acknowledgments:
I would like to extend my heartfelt thanks to Dr. Mohammed Almeer for his exceptional guidance and support during this project. His valuable insights and assistance were essential to the successful completion of this work. I also wish to express my appreciation to NewsAPI for supplying the news data utilized in this project, as their service was vital for collecting the required information.


6.Conclusion:
The Multithreaded News Client/Server Information System project provided valuable experience in network programming, client-server architecture, and API integration. The development of a multithreaded application enhances both functionality and user experience.


7.Resources:
1-NewsAPI Documentation
2-Python Socket Programming
3-Threading in Python


Course instructor: Dr. Mohammed Almeer
 
