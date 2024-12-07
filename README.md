# -----ITNE352 Project---S1---2024/2025----

## Group: B3
### Section: 2
- **Haya Alkaabi (202203340)**
- **Muneera Almehaiza (202206145)**

---

## Project Description

This project aims to develop a client-server system for exchanging current news information. It emphasizes critical aspects of client-server architecture, network communication, multithreading, API integration, and coding best practices. The server, implemented in Python, retrieves news updates from NewsAPI.org, manages multiple simultaneous client connections, and responds to various client requests. The client script, also written in Python, establishes a connection to the server to fetch and display news articles and sources. Users can easily navigate through different options to obtain specific news details or exit the application.

---

## Table of Contents

1. [Requirements](#requirements)
2. [How to Run the System](#how-to-run-the-system)
3. [Project Scripts](#project-scripts)
4. [Additional Concepts](#additional-concepts)
5. [Acknowledgments](#acknowledgments)
6. [Conclusion](#conclusion)
7. [Resources](#resources)

---

## Requirements

To set up and ensure an efficient run of this project on your local machine, follow these instructions:

### Prerequisites

1. **Python**: Ensure Python is installed on your system. If not, please download it from [python.org](https://www.python.org/downloads/).
2. **NewsAPI Key**: Sign up on [NewsAPI.org](https://newsapi.org/) to get your API key.

### Setup

1. Clone the repository.
2. Create a virtual environment.
3. Activate the virtual environment.

---

## How to Run the System

### First, Running the Server:
1. Open a terminal and navigate to the directory containing `Server.py`.
2. Run the server using: 
   ```bash
   python Server.py
