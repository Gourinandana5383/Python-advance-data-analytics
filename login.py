import csv
def load_users(file_name):
    users = {}
    try:
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users[row['name']] = {'password': row['password'], 'status': row['status']}
    except FileNotFoundError:
        pass
    return users
def save_user(file_name, name, password, status):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, password, status])
def register(users, file_name):
    name = input("Enter username: ")
    if name in users:
        print("User already exists.")
        return
    password = input("Enter password: ")
    status = "1"
    users[name] = {'password': password, 'status': status}
    save_user(file_name, name, password, status)
    print("Registration successful.")
def login(users):
    name = input("Enter username: ")
    password = input("Enter password: ")
    if name in users and users[name]['password'] == password:
        status = users[name]['status']
        status_text = "Active" if status == "1" else "Inactive"
        print(f"Login successful! User Status: {status_text} ({status})")
    else:
        print("Invalid username or password.")
def main():
    file_name = 'users.csv'
    users = load_users(file_name)
    while True:
        choice = input("\n1. Register\n2. Login\n3. Exit\nChoose an option: ")
        if choice == '1':
            register(users, file_name)
        elif choice == '2':
            login(users)
        elif choice == '3':
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()