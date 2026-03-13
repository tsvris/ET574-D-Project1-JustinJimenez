import data


def add_session():
    print("\nAdd Study Session")

    subject = input("Enter subject/course: ")

    while True:
        try:
            mins = int(input("Enter minutes studied: "))
            if mins <= 0:
                print("Minutes must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    location = input("Enter location (Home/Library/Lab/Other): ")

    note = input("Enter notes (optional): ")

    data.subjects.append(subject)
    data.minutes.append(mins)
    data.locations.append(location)
    data.notes.append(note)

    print("Session added.")


def view_all():

    print("\nAll Study Sessions")

    if len(data.subjects) == 0:
        print("No sessions recorded.")
        return

    for i in range(len(data.subjects)):
        print("--------------------------------")
        print("Session", i + 1)
        print("Subject:", data.subjects[i])
        print("Minutes:", data.minutes[i])
        print("Location:", data.locations[i])
        print("Notes:", data.notes[i])


def view_summary():

    print("\nStudy Summary")

    if len(data.minutes) == 0:
        print("No sessions recorded.")
        return

    total_sessions = len(data.minutes)
    total_minutes = sum(data.minutes)
    average_minutes = total_minutes / total_sessions
    longest_session = max(data.minutes)
    shortest_session = min(data.minutes)

    print("Total sessions:", total_sessions)
    print("Total minutes studied:", total_minutes)
    print("Average minutes per session:", round(average_minutes, 2))
    print("Longest session:", longest_session)
    print("Shortest session:", shortest_session)