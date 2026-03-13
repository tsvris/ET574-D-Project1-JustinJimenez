import tracker


def menu():

    while True:

        print("\nWelcome to Study Session Tracker!")
        print("1. Add Study Session")
        print("2. View Summary")
        print("3. View All Sessions")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            tracker.add_session()

        elif choice == "2":
            tracker.view_summary()

        elif choice == "3":
            tracker.view_all()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


menu()