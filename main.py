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
        print("2. Modify Existing Data")
        print("3. Add New Data")
        # print("4. Add Media")
        # print("5. Add Media Type")
        # print("6. Add Renter")
        # print("7. Add Loan")
        print("4. Exit")

        choice = input("\n>")

        if choice == "1":
            print("Viewing Data.")
            while True:
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
                        print("Renter ID#{}\n{}\nCurrently has {} loans.".format(id, name, num_loans))
                elif view_data_choice == "5":
                    loan_data = database.pull_data(db_connection, "Active_Loans")
                    for (id, renter_id, media_id, home_id, check_out_date, loan_expiration) in loan_data:
                        print("Loan ID#{}\n Rented by Renter ID#{}, Media {} from location #{}\nChecked out on {}\n Due on {}".format(id, renter_id, media_id, home_id, check_out_date, loan_expiration))
                elif view_data_choice == "6":
                    break
                else:
                    print('Please input a valid option.')
        elif choice == "2":
            print("Modifying existing data.")
            while True:
                print("-" * 80)
                print("Select an option:")
                print("1. Modify Locations")
                print("2. Modify Media")
                print("3. Modify Media Types")
                print("4. Modify Renters")
                print("5. Modify Loans")
                print("6. Go Back")

                modify_data_choice = input("\n> ")

                if modify_data_choice == "1":
                    location_data = database.pull_data(db_connection, "Locations")
                    for (id, name, address) in location_data:
                        print("Location #{}\n{}\nlocated at {}".format(id, name, address))
                    entry_to_modify = input("Select an entry to modify.\n> ")
                    print("You may modify these fields.\n1. Name\n2. Address\n")
                    field_to_modify = input("Select an option.\n> ")
                    final_value = input("Please input the value you would like this field to have.\n> ")
                    if field_to_modify == "1":
                        field_to_modify_str = "name"
                    elif field_to_modify == "2":
                        field_to_modify_str = "address"
                    else:
                        print("Please input a valid option.")

                    database.update_data(db_connection, "Locations", entry_to_modify, field_to_modify_str, final_value)
                elif modify_data_choice == "2":
                    media_data = database.pull_data(db_connection, "Media_Names")
                    for (id, location_id, name, acquiry_date, quantity, type_id) in media_data:
                        print("Media #{}\n{}\nLocated at Location #{}\nAcquired on {}\nAmount Available: {}\nType ID={}".format(id, name, location_id, acquiry_date, quantity, type_id))
                    entry_to_modify = input("Select an entry to modify.\n> ")
                    print("You may modify these fields.\n1. Name\n2. Location\n3. Acquiry Date\n4. Quantity\n5. Type\n")
                    field_to_modify = input("Select an option.\n> ")
                    final_value = input("Please input the value you would like this field to have.\n> ")
                    if field_to_modify == "1":
                        field_to_modify_str = "name"
                    elif field_to_modify == "2":
                        field_to_modify_str = "location_id"
                    elif field_to_modify == "3":
                        field_to_modify_str == "acquiry_date"
                    elif field_to_modify == "4":
                        field_to_modify_str == "quantity"
                    elif field_to_modify == "5":
                        field_to_modify_str == "type_id"
                    else:
                        print("Please input a valid option.")

                    database.update_data(db_connection, "Media_Names", entry_to_modify, field_to_modify_str, final_value)
                elif modify_data_choice == "3":
                    media_type_data = database.pull_data(db_connection, "Media_Types")
                    for (id, type, category) in media_type_data:
                        print("Media Type #{}\n{}\nPrimarily contains: {}".format(id, type, category))
                    entry_to_modify = input("Select an entry to modify.\n> ")
                    print("You may modify these fields.\n1. Name\n2. Primary Contents\n")
                    field_to_modify = input("Select an option.\n> ")
                    final_value = input("Please input the value you would like this field to have.\n> ")
                    if field_to_modify == "1":
                        field_to_modify_str = "name"
                    elif field_to_modify == "2":
                        field_to_modify_str = "category"
                    else:
                        print("Please input a valid option.")

                    database.update_data(db_connection, "Media_Types", entry_to_modify, field_to_modify_str, final_value)
                elif modify_data_choice == "4":
                    renter_data = database.pull_data(db_connection, "Renters")
                    for (id, name, num_loans) in renter_data:
                        print("Renter ID#{}\n{}\nCurrently has {} loans.".format(id, name, num_loans))
                    entry_to_modify = input("Select an entry to modify.\n> ")
                    print("You may modify these fields.\n1. Name\n2. Number of active loans\n")
                    field_to_modify = input("Select an option.\n> ")
                    final_value = input("Please input the value you would like this field to have.\n> ")
                    if field_to_modify == "1":
                        field_to_modify_str = "name"
                    elif field_to_modify == "2":
                        field_to_modify_str = "num_loans"
                    else:
                        print("Please input a valid option.")

                    database.update_data(db_connection, "Renters", entry_to_modify, field_to_modify_str, final_value)
                elif modify_data_choice == "5":
                    loan_data = database.pull_data(db_connection, "Active_Loans")
                    for (id, renter_id, media_id, home_id, check_out_date, loan_expiration) in loan_data:
                        print("Loan ID#{}\n Rented by Renter ID#{}, Media {} from location #{}\nChecked out on {}\n Due on {}".format(id, renter_id, media_id, home_id, check_out_date, loan_expiration))
                    entry_to_modify = input("Select an entry to modify.\n> ")
                    print("You may modify these fields.\n1. Render ID#\n2. Media ID#\n3. Home Location\n4. Checkout Date\n5. Due Date\n")
                    field_to_modify = input("Select an option.\n> ")
                    final_value = input("Please input the value you would like this field to have.\n> ")
                    if field_to_modify == "1":
                        field_to_modify_str = "renter_id"
                    elif field_to_modify == "2":
                        field_to_modify_str = "media_id"
                    elif field_to_modify == "3":
                        field_to_modify_str == "home_id"
                    elif field_to_modify == "4":
                        field_to_modify_str == "check_out_date"
                    elif field_to_modify == "5":
                        field_to_modify_str == "loan_expiration"
                    else:
                        print("Please input a valid option.")

                    database.update_data(db_connection, "Active_Loans", entry_to_modify, field_to_modify_str, final_value)
                elif modify_data_choice == "6":
                    break
                else:
                    print("Please input a valid option.")
        elif choice == "3":
            print("Adding new data.")
            while True:
                print("-" * 80)
                print("Choose an option.\n1. Add Location\n2. Add Media\n3. Add Media Type\n4. Add Renter\n5. Add Loan\n6. Go Back\n")

                add_data_choice = input("\n> ")

                if add_data_choice == "1":
                    location_name = input("Please input the name of this location.\n> ")
                    location_address = input("Please input the address of this location.\n> ")

                    database.add_location(db_connection, location_name, location_address)
                elif add_data_choice == "2":
                    media_name = input("Please input the name of this media.\n> ")
                    media_acquiry_date = input("Please input the date this media was acquired. Use the format 'YYYY-MM-DD'.\n> ")
                    media_quantity = input("Please input the number of copies of this media available.\n> ")
                    media_location_id = input("Please input the location number where this media is located.\n> ")
                    media_type_id = input("Please input the Type ID for this media. If you don't know this, check the list of avaiable Media Types.\n> ")

                    database.add_media_name(db_connection, media_name, media_acquiry_date, media_quantity, media_location_id, media_type_id)
                    media_id_raw = database.get_media_id(db_connection, media_name, media_quantity, media_location_id)
                    for id in media_id_raw:
                        media_id = id[0]
                    database.add_media(db_connection, media_type_id, media_id)
                elif add_data_choice == "3":
                    media_type_name = input("Please input the name of this media type\n> ")
                    media_type_category = input("Please input what this type of media primarily contains.\n> ")

                    database.add_media_type(db_connection, media_type_name, media_type_category)
                elif add_data_choice == "4":
                    renter_name = input("Please input the name of this renter.\n> ")

                    database.add_renter(db_connection, renter_name, "0")
                elif add_data_choice == "5":
                    loan_renter_id = input("Please input the ID# of the renter this loan is for.\n> ")
                    loan_media_id = input("Please input the ID# of the media being rented.\n> ")
                    loan_check_out_date = input("Please input the checkout date for this loan. This is probably the current date. Use the format 'YYYY-MM-DD'.\n> ")
                    loan_expiration_date = input("Pleae input when this loan expires. Use the format 'YYYY-MM-DD'.\n> ")
                    loan_home_id = input("Please input the location number where this media is being rented from.\n> ")

                    database.add_loan(db_connection, loan_renter_id, loan_media_id, loan_check_out_date, loan_expiration_date, loan_home_id)
                    database.increment_loan_count(db_connection, loan_renter_id)
                elif add_data_choice == "6":
                    break
                else:
                    print("Please input a valid option.")
        elif choice == "4":
            db_connection.close()
            print("Disconnected from database.\nGoodbye!")
            break
        else:
            print("Please input a valid option.")


main()
