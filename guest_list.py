def get_guest_list():
    guest_list = []
    while True:
        print("1. Add guest")
        print("2. Delete guest")
        print("3. Show guests")
        print("4. Upload guests from file")
        print("5. Save guest list to file")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_guest(guest_list)
        elif choice == '2':
            delete_guest(guest_list)
        elif choice == '3':
            show_guests(guest_list)
        elif choice == '4':
            upload_file(guest_list)
        elif choice == '5':
            save_guest_list(guest_list)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
    return guest_list

def add_guest(guest_list):
    name = input("Enter guest's name: ")
    email = input("Enter guest's email: ")
    for guest in guest_list:
        if guest['name'] == name or guest['email'] == email:
            print("Guest already exists.")
            return
    guest_list.append({'name': name, 'email': email})

def delete_guest(guest_list):
    name = input("Enter the name of the guest to delete: ")
    for guest in guest_list:
        if guest['name'] == name:
            guest_list.remove(guest)
            print("Guest deleted.")
            return
    print("Guest not found.")

def show_guests(guest_list):
    for guest in guest_list:
        print(f"Name: {guest['name']}, Email: {guest['email']}")

def upload_file(guest_list):
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, email = line.strip().split(',')
                guest_list.append({'name': name, 'email': email})
    except FileNotFoundError:
        print("File not found.")

def save_guest_list(guest_list):
    with open('guest_list.txt', 'w') as file:
        for guest in guest_list:
            file.write(f"{guest['name']},{guest['email']}\n")