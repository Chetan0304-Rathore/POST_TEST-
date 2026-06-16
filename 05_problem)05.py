try:
    # Ask user for filename
    filename = input("Enter filename: ")

    # Open and read file
    with open(filename, "r") as file:
        content = file.readlines()

        # Check if file is empty
        if len(content) == 0:
            print("File is empty!")
        else:
            print("Total number of lines in file:", len(content))

# Handle file not found error
except FileNotFoundError:
    print("File does not exist!")

# Finally block
finally:
    print("Operation complete!")