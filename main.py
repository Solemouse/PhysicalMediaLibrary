import database


def main():
    print("Welcome to the Physical Media Database Manager.")
    print("Attempting to connect to the database. Please wait...")
    db_connection = database.connect_db()
    if (db_connection is None):
        exit(1)
    else:
        print("Connected to the database.")
        menu(db_connection)


def menu(db_connection):
    while True:

        print("-" * 80)
        print("Select an option: ")
        print("1. View Data")
        print("2. Add Location")
        print("3. Add Media")
        print("4. Add Media Type")
        print("5. Add Renter")
        print("6. Add Loan")
        print("7. Exit")

        choice = input("\n>")

        if choice == "1":
            while True:
                print("Viewing Data.")
                print("-" * 80)
                print("Select an option:")
                print("1. View Locations")
                print("2. View Media")
                print("3. View Media Types")
                print("4. View Renters")
                print("5. View Loans")
                print("6. Go Back")

                view_data_choice = input("\n>")

                if view_data_choice == "1":
                    location_data = database.pull_data(db_connection, "Locations")
                    for (id, name, address) in location_data:
                        print("Location #{}\n{}\nlocated at {}".format(id, name, address))
                elif view_data_choice == "2":
                    media_data = database.pull_data(db_connection, "Media_Names")
                    for (id, location_id, name, acquiry_date, quantity, type_id) in media_data:
                        print("Media #{}\n{}\nLocated at Location #{}\nAcquired on {}\nAmount Available: {}\nType ID={}".format(id, name, location_id, acquiry_date, quantity, type_id))
                elif view_data_choice == "3":
                    media_type_data = database.pull_data(db_connection, "Media_Types")
                    for (id, type, category) in media_type_data:
                        print("Media Type #{}\n{}\nPrimarily contains: {}".format(id, type, category))
                elif view_data_choice == "4":
                    renter_data = database.pull_data(db_connection, "Renters")
                    for (id, name, num_loans) in renter_data:
                        print("Renter ID#{}\n{}\nCurrently has {} loans.")
                elif view_data_choice == "5":
                    loan_data = database.pull_data(db_connection, "Active_Loans")
                    for (id, renter_id, media_id, home_id, check_out_date, loan_expiration) in loan_data:
                        print("Loan ID#{}\n Rented by Renter ID#{}, Media {} from location #{}\nChecked out on {}\n Due on {}")
                elif view_data_choice == "6":
                    break


main()
