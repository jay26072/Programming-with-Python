# 21.Create Web Database Application “Address Book” with options to 
# a) add/ insert a record 
# b) modify a record 
# c) display a record 
# d) delete a record 

import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="addressbook"
    )

# Add a record
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    conn.commit()
    conn.close()
    print("Contact added.")

# Display all records
def display_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    print("\n--- Contact List ---")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")
    conn.close()

# Modify a record
def modify_contact():
    display_contacts()
    id = input("Enter ID of the contact to modify: ")
    name = input("Enter new name: ")
    phone = input("Enter new phone: ")
    email = input("Enter new email: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s", (name, phone, email, id))
    conn.commit()
    conn.close()
    print("Contact updated.")

# Delete a record
def delete_contact():
    display_contacts()
    id = input("Enter ID of the contact to delete: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    print("Contact deleted.")


while True:
    print("\nAddress Book Menu")
    print("1. Add Contact")
    print("2. Modify Contact")
    print("3. Display Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        modify_contact()
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid option. Please try again.")

