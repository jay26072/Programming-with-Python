import datetime
filename="reservations.txt"
def reserve_ticket():
    try:
        with open(filename, "a") as file:
            # Get passenger details
            passenger_name = input("Enter passenger name: ")
            train_number = input("Enter train number: ")
            departure_station = input("Enter departure station: ")
            arrival_station = input("Enter arrival station: ")
            travel_date = datetime.datetime.now().strftime("%Y-%m-%d")

            # Create a reservation record
            record = f"{passenger_name},{train_number},{departure_station},{arrival_station},{travel_date}\n"

            # Write the record to the file
            file.write(record)

        print("Ticket reserved successfully!")

    except Exception as e:
        print(f"Error reserving ticket: {e}")


def list_reservations_for_today():
    try:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        reservations = []

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(",")
                    if len(data) == 5 and data[4] == today:
                        reservations.append(data)

        if reservations:
            print("Reservations for today:")
            for reservation in reservations:
                print(
                    f"Passenger: {reservation[0]}, Train: {reservation[1]}, "
                    f"Departure: {reservation[2]}, Arrival: {reservation[3]}"
                )
        else:
            print("No reservations found for today.")

    except FileNotFoundError:
        print("Reservations file not found.")
    except Exception as e:
        print(f"Error listing reservations: {e}")


# Main program loop
while True:
    print("\nRailway Reservation System")
    print("1. Reserve Ticket")
    print("2. List Reservations for Today")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        reserve_ticket()
    elif choice == "2":
        list_reservations_for_today()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")