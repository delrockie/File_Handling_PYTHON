# File creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("This is a test file.\n")
        file.write("12345\n")
except Exception as e:
    print("Error creating file:", e)
    
# File reading and display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
except Exception as e:
    print("Error reading file:", e)

# File appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is a new line.\n")
        file.write("Another line.\n")
        file.write("And another line.\n")
except Exception as e:
    print("Error appending file:", e)

# Error handling
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
except FileNotFoundError:
    print("my_file.txt not found.")
except PermissionError:
    print("Permission denied to access my_file.txt.")
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("File handling complete.")