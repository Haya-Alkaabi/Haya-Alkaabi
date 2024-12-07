import socket
import tkinter as tk 
from tkinter import messagebox, simpledialog 

class NewsClientApp: 
    def __init__(self, master): # Initialize root window
        self.master = master
        self.master.title("News API Client")
        self.master.geometry("600x600")

        # Initialize the client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try: 
            self.client_socket.connect(("127.0.0.1", 49999))
        except Exception as e:  
            messagebox.showerror("Connection Error", f"Unable to connect to the server: {e}") 
            self.master.destroy()
            return 

        self.client_name = None 
        self.create_welcome_screen()  

    def create_welcome_screen(self): # Create the welcome screen
        """Create the welcome screen to ask for the user's name."""
        self.clear_frame()

        tk.Label(self.master, text="Welcome to News API", font=("Helvetica", 40,'bold')).pack(pady=20) 
        tk.Label(self.master, text="Please enter your name:", font=("Helvetica", 20)).pack(pady=10)

        self.name_entry = tk.Entry(self.master, font=("Helvetica", 14), width=30) 
        self.name_entry.pack(pady=10) 

        tk.Button(self.master, text="Start", command=self.submit_name, font=("Helvetica", 14)).pack(pady=10)

    def submit_name(self): # Submit the user's name
        """Handle the user's name input and proceed to the main menu."""
        name = self.name_entry.get().strip()
        if name:
            self.client_name = name
            self.client_socket.send(self.client_name.encode('utf-8'))
            self.create_main_menu() 
        else:  
            messagebox.showwarning("Input Error", "Name cannot be empty.") 

    def create_main_menu(self): # Create the main menu
        """Create the main menu screen."""
        self.clear_frame()

        tk.Label(self.master, text=f"Welcome, {self.client_name}!", font=("Helvetica", 35,'bold')).pack(pady=20)  
        tk.Label(self.master, text="Choose an option:", font=("Helvetica", 20)).pack(pady=10)  

        tk.Button(self.master, text="Search Headlines", command=self.search_headlines, font=("Helvetica", 20)).pack(pady=10) 
        tk.Button(self.master, text="List Sources", command=self.list_sources, font=("Helvetica", 20)).pack(pady=10) 
        tk.Button(self.master, text="Quit", command=self.quit_app, font=("Helvetica", 20)).pack(pady=10) 

    def search_headlines(self): # Search for headlines
        """Create the search headlines menu."""
        self.clear_frame() 

        tk.Label(self.master, text="Search Headlines", font=("Helvetica", 35,'bold')).pack(pady=20) # Display the title
        tk.Button(self.master, text="Search by Keyword", command=lambda: self.handle_search("1.1"), font=("Helvetica", 14)).pack(pady=10) # Search by keyword
        tk.Button(self.master, text="Search by Category", command=lambda: self.handle_search("1.2"), font=("Helvetica", 14)).pack(pady=10) # Search by category
        tk.Button(self.master, text="Search by Country", command=lambda: self.handle_search("1.3"), font=("Helvetica", 14)).pack(pady=10) # Search by country
        tk.Button(self.master, text="List All Headlines", command=lambda: self.handle_search("1.4"), font=("Helvetica", 14)).pack(pady=10) # List all headlines
        tk.Button(self.master, text="Back", command=self.create_main_menu, font=("Helvetica", 14)).pack(pady=20) # Back to main menu

    def handle_search(self, option): # Handle the search option
        """Handle specific search options."""
        try:
            self.client_socket.send(b"1")  # Signal for search operation
            self.client_socket.send(option.encode('utf-8'))

            if option in ["1.1", "1.2", "1.3"]:
                prompt = {
                    "1.1": "Enter a keyword to search:",
                    "1.2": "Enter a category (e.g., business):",
                    "1.3": "Enter a country code (e.g., us):"
                }[option]
                param = self.get_user_input(prompt) # Get user input
                if param:
                    self.client_socket.send(param.encode('utf-8')) # Send user input to server
                else:
                    messagebox.showwarning("Input Error", "Input cannot be empty.") # Show error message
                    return
            else:
                self.client_socket.send("all".encode('utf-8')) # Send 'all' for list all headlines

            response = self.receive_data() # Receive the response from the server
            self.display_response(response) # Display the response
        except Exception as e: # Handle any exceptions
            messagebox.showerror("Communication Error", f"An error occurred: {e}") # Show error message

    def list_sources(self): # List all sources
        """Create the list sources menu."""
        self.clear_frame() # Clear the current frame

        tk.Label(self.master, text="List Sources", font=("Helvetica", 35,'bold')).pack(pady=20) # Display the title
        tk.Button(self.master, text="Search by Category", command=lambda: self.handle_sources("2.1"), font=("Helvetica", 14)).pack(pady=10) # Search by category
        tk.Button(self.master, text="Search by Country", command=lambda: self.handle_sources("2.2"), font=("Helvetica", 14)).pack(pady=10) # Search by country
        tk.Button(self.master, text="Search by Language", command=lambda: self.handle_sources("2.3"), font=("Helvetica", 14)).pack(pady=10) # Search by language
        tk.Button(self.master, text="List All Sources", command=lambda: self.handle_sources("2.4"), font=("Helvetica", 14)).pack(pady=10) # List all sources
        tk.Button(self.master, text="Back", command=self.create_main_menu, font=("Helvetica", 14)).pack(pady=20) # Back to main menu

    def handle_sources(self, option): # Handle the sources option
        """Handle source listing options."""
        try: 
            self.client_socket.send(b"2")  # Signal for sources operation
            self.client_socket.send(option.encode('utf-8')) # Send the option to the server

            if option in ["2.1", "2.2", "2.3"]:
                prompt = {
                    "2.1": "Enter a category (e.g., business):",
                    "2.2": "Enter a country code (e.g., us):",
                    "2.3": "Enter a language code (e.g., en):"
                }[option]
                param = self.get_user_input(prompt)
                if param:
                    self.client_socket.send(param.encode('utf-8')) # Send user input to server
                else:
                    messagebox.showwarning("Input Error", "Input cannot be empty.") # Show error message
                    return
            else:
                self.client_socket.send("all".encode('utf-8')) # Send 'all' for list all sources

            response = self.receive_data() # Receive the response from the server
            self.display_response(response) # Display the response
        except Exception as e: # Handle any exceptions
            messagebox.showerror("Communication Error", f"An error occurred: {e}") # Show error message

    def receive_data(self): # Receive data from the server
        """Receive data from the server."""
        try:
            response = self.client_socket.recv(4069).decode('utf-8') # Receive the response from the server
            return response 
        except Exception as e: # Handle any exceptions
            return f"Error receiving data: {e}"

    def display_response(self, response): # Display the response
        """Display the server's response."""
        self.clear_frame() # Clear the current frame

        tk.Label(self.master, text="Response", font=("Helvetica", 16)).pack(pady=20) # Display the title
        response_label = tk.Label(self.master, text=response, wraplength=450, justify="left", anchor="nw") # Display the response
        response_label.pack(pady=10) # Display the response

        tk.Button(self.master, text="Back", command=self.create_main_menu, font=("Helvetica", 14)).pack(pady=20) # Display the back button

    def get_user_input(self, prompt): # Get user input
        """Get user input through a dialog."""
        return simpledialog.askstring("Input Required", prompt) 

    def quit_app(self): # Quit the application
        """Handle quitting the application."""
        self.client_socket.close() # Close the client socket
        self.master.destroy() # Destroy the main window

    def clear_frame(self): # Clear the frame
        """Clear all widgets from the frame."""
        for widget in self.master.winfo_children(): # Clear all widgets
            widget.destroy()  # Destroy each widget


if __name__ == "__main__": # Main entry point
    root = tk.Tk() # Create the main window
    app = NewsClientApp(root) # Create an instance of the NewsClientApp class
    root.mainloop() # Start the main event loop