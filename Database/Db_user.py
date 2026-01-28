import psycopg2
import bcrypt

def get_connection():
    return psycopg2.connect(
        dbname="python_db",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )


def create_user():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    query = """
    INSERT INTO app_user (username, email, password)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (username, email, hashed_password))
    conn.commit()

    print("User created successfully")

    cursor.close()
    conn.close()

def view_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username, email, created_at FROM app_user"
    )
    users = cursor.fetchall()

    if not users:
        print("No users found")
    else:
        for user in users:
            print(user)

    cursor.close()
    conn.close()

def update_user():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter username to update: ")
    new_email = input("Enter new email: ")
    new_password = input("Enter new password: ")

    hashed_password = bcrypt.hashpw(
        new_password.encode(),
        bcrypt.gensalt()
    ).decode()

    query = """
    UPDATE app_user
    SET email = %s, password = %s
    WHERE username = %s
    """

    cursor.execute(query, (new_email, hashed_password, username))

    if cursor.rowcount == 0:
        print("User not found")
    else:
        conn.commit()
        print("User updated successfully")

    cursor.close()
    conn.close()

def delete_user():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter username to delete: ")

    cursor.execute(
        "DELETE FROM app_user WHERE username = %s",
        (username,)
    )

    if cursor.rowcount == 0:
        print("User not found")
    else:
        conn.commit()
        print("User deleted successfully")

    cursor.close()
    conn.close()

def login_user():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute(
        "SELECT password FROM app_user WHERE username = %s",
        (username,)
    )

    result = cursor.fetchone()

    if not result:
        print("User not found")
    else:
        stored_hash = result[0].encode()
        if bcrypt.checkpw(password.encode(), stored_hash):
            print("Login successful")
        else:
            print("Incorrect password")

    cursor.close()
    conn.close()

def menu():
    while True:
        print("\n--- USER MANAGEMENT ---")
        print("1. Create user")
        print("2. View users")
        print("3. Update user")
        print("4. Delete user")
        print("5. Login")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            login_user()
        elif choice == "6":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Try again.")

menu()
