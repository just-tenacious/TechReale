import dbOperations as db

while True:
  print("\n=== User Database Menu ===")
  print("1. View all users")
  print("2. Insert user")
  print("3. Update user")
  print("4. Delete user")
  print("5. Exit")

  choice = input("Enter your choice (1-5): ")

  if choice == "1":
    db.viewData()

  elif choice == "2":
    name = input("Enter name: ").strip()
    age = int(input("Enter age: "))
    errors = db.validateInput(name, age)
    if errors:
      for e in errors:
        print("Error:", e)
    else:
      db.insertData(name, age)
      db.saveChanges()
      print("User inserted successfully!")

  elif choice == "3":
    id = int(input("Enter user ID to update: "))
    name = input("Enter new name: ").strip()
    age = int(input("Enter new age: "))
    errors = db.validateInput(name, age)
    if errors:
      for e in errors:
        print("Error:", e)
    else:
      db.updateData(id, name, age)
      db.saveChanges()
      print("User updated successfully!")

  elif choice == "4":
    id = int(input("Enter user ID to delete: "))
    db.deleteData(id)
    db.saveChanges()
    print("User deleted successfully!")

  elif choice == "5":
    print("Exiting program...")
    break

  else:
    print("Invalid choice. Please try again.")
