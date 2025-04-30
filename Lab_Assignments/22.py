# 22.Create Web Database Application “Event Registration” with options to 
# a) Event Registration 
# b) Cancel Registration 
# c) display a record 


import mysql.connector

# MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="eventdb"
    )

# a) Register for event
def register_event():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    event = input("Enter event name: ")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registrations (name, email, event) VALUES (%s, %s, %s)", (name, email, event))
    conn.commit()
    conn.close()
    print("Registration successful!")

# b) Cancel registration
def cancel_registration():
    display_records()
    id = input("Enter the ID of the registration to cancel: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registrations WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    print("Registration cancelled.")

# c) Display all registrations
def display_records():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registrations")
    results = cursor.fetchall()

    print("\n--- Event Registrations ---")
    print(f"{'ID':<5} {'Name':<20} {'Email':<25} {'Event':<20}")
    print("-" * 70)
    for row in results:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<25} {row[3]:<20}")
    conn.close()

while True:
    print("\n=== Event Registration System ===")
    print("1. Register for Event")
    print("2. Cancel Registration")
    print("3. Display All Registrations")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_event()
    elif choice == '2':
        cancel_registration()
    elif choice == '3':
        display_records()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")