import os

def create_file():
    filename = input("Enter the filename: ")
    if os.path.isfile(filename):
        print("File already exists!")
    else:
        file = open(filename, "w")
        file.write("This is a sample text.")
        file.close()
        print("File created successfully!")

def list_files():
    files = os.listdir(".")
    if len(files) == 0:
        print("No files found.")
    else:
        print("Files in directory:")
        for filename in files:
            print(filename)

def delete_file():
    filename = input("Enter the filename: ")
    if os.path.isfile(filename):
        os.remove(filename)
        print("File deleted successfully!")
    else:
        print("File not found.")

if __name__=="__main__":
    while True:
        print("\nSingle Level Directory File Organization Technique\n")
        print("1. Create a new file")
        print("2. List all files")
        print("3. Delete a file")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_file()
        elif choice == "2":
            list_files()
        elif choice == "3":
            delete_file()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


