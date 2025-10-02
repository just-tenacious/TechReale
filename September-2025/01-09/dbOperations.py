from connect import connection

cursor = connection.cursor()

def createTable():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
    )

def viewData():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No users found.")

def getId():
    cursor.execute("SELECT MAX(id) FROM users")
    id = cursor.fetchone()[0]
    return 0 if id is None else id

def validateInput(name, age):
    error = []
    if name.strip() == "":   # ✅ FIXED
        error.append("The name is empty. Please enter a name.")
    if age < 1 or age > 100:  # ✅ FIXED condition
        error.append("The age is invalid. Must be between 1 and 100.")
    return error

def insertData(name, age):
    try:
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    except Exception as e:
        print("Something went wrong:", e)

def updateData(id, name, age):
    try:
        cursor.execute(
            "UPDATE users SET name=%s, age=%s WHERE id=%s", (name, age, id)  # ✅ safe query
        )
    except Exception as e:
        print("Something went wrong:", e)

def deleteData(id):
    try:
        cursor.execute("DELETE FROM users WHERE id=%s", (id,))  # ✅ safe query
    except Exception as e:
        print("Something went wrong:", e)

def saveChanges():
    connection.commit()

createTable()
