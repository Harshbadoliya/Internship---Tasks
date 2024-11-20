import tkinter as tk
from tkinter import messagebox
import pickle

# Function to load contacts from file
def load_contacts():
    try:
        with open('contacts.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Function to save contacts to file
def save_contacts(contacts):
    with open('contacts.pkl', 'wb') as f:
        pickle.dump(contacts, f)

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    if name and phone:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        refresh_contacts_list()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required fields")

# Function to refresh the list of contacts displayed
def refresh_contacts_list():
    contacts_list.delete(0, tk.END)
    for contact in contacts:
        contacts_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search contacts
def search_contact():
    search_query = entry_search.get()
    contacts_list.delete(0, tk.END)
    for contact in contacts:
        if search_query.lower() in contact['name'].lower() or search_query in contact['phone']:
            contacts_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to update contact details
def update_contact():
    selected_contact_index = contacts_list.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contacts[index]['name'] = entry_name.get()
        contacts[index]['phone'] = entry_phone.get()
        contacts[index]['email'] = entry_email.get()
        contacts[index]['address'] = entry_address.get()
        refresh_contacts_list()
    else:
        messagebox.showwarning("Selection Error", "Select a contact to update")

# Function to delete a contact
def delete_contact():
    selected_contact_index = contacts_list.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contacts_list.delete(index)
        contacts.pop(index)
    else:
        messagebox.showwarning("Selection Error", "Select a contact to delete")

# Setup main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("377x550+650+110")  # Set window size to 600x400 pixels
root.resizable(0, 0)
root.configure(bg="#B5E5CF")

# Define the UI elements
frame = tk.Frame(root)
frame.pack(pady=20)

# Name input
tk.Label(frame, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1)

# Phone input
tk.Label(frame, text="Phone:").grid(row=1, column=0)
entry_phone = tk.Entry(frame, width=30)
entry_phone.grid(row=1, column=1)

# Email input
tk.Label(frame, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=2, column=1)

# Address input
tk.Label(frame, text="Address:").grid(row=3, column=0)
entry_address = tk.Entry(frame, width=30)
entry_address.grid(row=3, column=1)

# Add contact button
btn_add_contact = tk.Button(frame, text="Add Contact", command=add_contact)
btn_add_contact.grid(row=4, columnspan=2, pady=10)

# Listbox for displaying contacts
contacts_list = tk.Listbox(root, width=50, height=10)
contacts_list.pack(pady=20)

# Search input and button
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search:").grid(row=0, column=0)
entry_search = tk.Entry(search_frame, width=30)
entry_search.grid(row=0, column=1)
btn_search = tk.Button(search_frame, text="Search", command=search_contact)
btn_search.grid(row=0, column=2)

# Update and delete buttons
btn_update_contact = tk.Button(root, text="Update Contact", command=update_contact)
btn_update_contact.pack(pady=5)

btn_delete_contact = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete_contact.pack(pady=5)

# Load initial contacts
contacts = load_contacts()
refresh_contacts_list()

# Run the main event loop
root.mainloop()

# Save contacts on exit
save_contacts(contacts)
