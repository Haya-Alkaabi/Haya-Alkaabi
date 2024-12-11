import socket
import tkinter as tk
from tkinter import messagebox, simpledialog

class NewsClientApp:
    def __init__(self, master):
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
        self.clear_frame()

        tk.Label(self.master, text="Welcome to News API", font=("Helvetica", 40, 'bold')).pack(pady=20)
        tk.Label(self.master, text="Please enter your name:", font=("Helvetica", 20)).pack(pady=10)

        self.name_entry = tk.Entry(self.master, font=("Helvetica", 14), width=30)
        self.name_entry.pack(pady=10)

        tk.Button(self.master, text="Start", command=self.submit_name, font=("Helvetica", 14)).pack(pady=10)

    def submit_name(self): 
        name = self.name_entry.get().strip()
        if name:
            self.client_name = name
            self.client_socket.send(self.client_name.encode('utf-8'))
            self.create_main_menu()
        else:
            messagebox.showwarning("Input Error", "Name cannot be empty.")

    def create_main_menu(self): # Create the main menu
        self.clear_frame()

        tk.Label(self.master, text=f"Welcome, {self.client_name}!", font=("Helvetica", 35, 'bold')).pack(pady=20)
        tk.Label(self.master, text="Choose an option:", font=("Helvetica", 20)).pack(pady=10)

        tk.Button(self.master, text="Search Headlines", command=self.search_headlines, font=("Helvetica", 20)).pack(pady=10)
        tk.Button(self.master, text="List Sources", command=self.list_sources, font=("Helvetica", 20)).pack(pady=10)
        tk.Button(self.master, text="Quit", command=self.quit_app, font=("Helvetica", 20)).pack(pady=10)

    def search_headlines(self): # Search headlines
        self.clear_frame()

        tk.Label(self.master, text="Search Headlines", font=("Helvetica", 35, 'bold')).pack(pady=20)
        tk.Button(self.master, text="Search by Keyword", command=lambda: self.handle_search("1.1"), font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="Search by Category", command=lambda: self.handle_search("1.2"), font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="Search by Country", command=lambda: self.handle_search("1.3"), font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="List All Headlines", command=lambda: self.handle_search("1.4"), font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="Back", command=self.create_main_menu, font=("Helvetica", 14)).pack(pady=20)

    def handle_search(self, option): # Handle search options
        try:
            self.client_socket.send(b"1")
            self.client_socket.send(option.encode('utf-8'))

            if option in ["1.1", "1.2", "1.3"]:
                prompt = {
                    "1.1": "Enter a keyword to search:",
                    "1.2": "Enter a category (e.g., business):",
                    "1.3": "Enter a country code (e.g., us):"
                }[option]
                param = self.get_user_input(prompt)
                if param:
                    self.client_socket.send(param.encode('utf-8'))
                else:
                    messagebox.showwarning("Input Error", "Input cannot be empty.")
                    return
            else:
                self.client_socket.send("all".encode('utf-8'))

            response = self.receive_data()
            self.display_response(response)
        except Exception as e:
            messagebox.showerror("Communication Error", f"An error occurred: {e}")

    def list_sources(self): # List sources
        self.clear_frame()

        tk.Label(self.master, text="List Sources", font=("Helvetica", 35, 'bold')).pack(pady=20)
        tk.Button(self.master, text="Search by Category", command=lambda: self.handle_sources("2.1"), font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="Search by Country", command=lambda: self.handle_sources("2.2"), font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="Search by Language", command=lambda: self.handle_sources("2.3"), font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="List All Sources", command=lambda: self.handle_sources("2.4"), font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self.master, text="Back", command=self.create_main_menu, font=("Helvetica", 14)).pack(pady=20)

    def handle_sources(self, option): # Handle sources options
        try:
            self.client_socket.send(b"2")
            self.client_socket.send(option.encode('utf-8'))

            if option in ["2.1", "2.2", "2.3"]:
                prompt = {
                    "2.1": "Enter a category (e.g., business):",
                    "2.2": "Enter a country code (e.g., us):",
                    "2.3": "Enter a language code (e.g., en):"
                }[option]
                param = self.get_user_input(prompt)
                if param:
                    self.client_socket.send(param.encode('utf-8'))
                else:
                    messagebox.showwarning("Input Error", "Input cannot be empty.")
                    return
            else:
                self.client_socket.send("all".encode('utf-8'))

            response = self.receive_data()
            self.display_response(response)
        except Exception as e:
            messagebox.showerror("Communication Error", f"An error occurred: {e}")

    def receive_data(self): # Receive data from server
        try:
            response = self.client_socket.recv(4069).decode('utf-8')
            return response
        except Exception as e:
            return f"Error receiving data: {e}"

    def display_response(self, response): # Display response
        self.clear_frame()

        tk.Label(self.master, text="Select a Source", font=("Helvetica", 20, 'bold')).pack(pady=20)

        try:
            items = response.split('\n')
            if len(items) > 15:
                items = items[:15]
            for item in items:
                if ':' in item:
                    title, details = item.split(':', 1)
                    tk.Button(
                        self.master,
                        text=title.strip(),
                        command=lambda d=details: self.show_details(d),
                        font=("Helvetica", 14),
                        wraplength=450,
                        anchor="w",
                        justify="left"
                    ).pack(pady=5, fill='x', anchor='w')
                else:
                    tk.Button(
                        self.master,
                        text=item.strip(),
                        command=lambda d="No details available": self.show_details(d),
                        font=("Helvetica", 14),
                        wraplength=450,
                        anchor="w",
                        justify="left"
                    ).pack(pady=5, fill='x', anchor='w')
        except Exception as e:
            tk.Label(self.master, text=f"Error parsing response: {e}", font=("Helvetica", 14), fg="red").pack(pady=10)

        tk.Button(self.master, text="Back", command=self.create_main_menu, font=("Helvetica", 14)).pack(pady=20)

    def show_details(self, details): # Show details of selected item
        self.clear_frame()

        tk.Label(self.master, text="Details", font=("Helvetica", 20, 'bold')).pack(pady=20)
        tk.Label(self.master, text=details, wraplength=550, justify="left", anchor="nw", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.master, text="Back", command=lambda: self.create_main_menu(), font=("Helvetica", 14)).pack(pady=20)

    def get_user_input(self, prompt): # Get user input
        return simpledialog.askstring("Input Required", prompt)

    def quit_app(self): # Quit application
        self.client_socket.close()
        self.master.destroy()

    def clear_frame(self): # Clear frame
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__": # Main function
    root = tk.Tk()
    app = NewsClientApp(root)
    root.mainloop()
