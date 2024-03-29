# 14) Create a class named Notes for handling text-based file operations. Class should contain methods "write", "read" and then "append" as instance methods or class methods. (Can contain any other methods if you wish) Use a single file for saving the notes. You can set the file name as a constant somewhere in the program (Or as a class variable). write method should
# create the if it doesn't exist, Then it should overwrite the older contents with the user input if the user plans to overwrite the file. read method should read the whole file contents and return it. If the file doesn't exist, then it should return "No notes found" append method should take the user input value and it must add the value to the end of the file. It must not overwrite the file. Now create a program to utilize this class.
# The program should repeatedly ask the user for these 4 choices:
# 1- Write Note (Overwrite existing).
# 2- Add more Notes (Append).
# 3- Read Notes.
# 4-Exit


class Notes:
    file_name = "1.txt"

    @classmethod
    def write(cls):
        with open(cls.file_name, "w") as file:
            content = input("Enter your note (this will overwrite existing notes): ")
            file.write(content)
        print("Note written successfully.")

    @classmethod
    def read(cls):
        try:
            with open(cls.file_name, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "No notes found."
        
    @classmethod
    def append(cls):
        with open(cls.file_name, "a") as file:
            content = input("Enter your note to append: ")
            file.write("\n" + content)
        print("Note appended successfully.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1- Write Note (Overwrite existing).")
        print("2- Add more Notes (Append).")
        print("3- Read Notes.")
        print("4- Exit.")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            Notes.write()
        elif choice == "2":
            Notes.append()
        elif choice == "3":
            print("\nNotes:\n", Notes.read())
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")



