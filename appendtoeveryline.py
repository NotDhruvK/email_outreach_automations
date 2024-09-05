# Get the file path and text to append from the user
file_path = input("Enter the path of the file: ")
append_text = input("Enter the text to append: ")

# Open the file for reading and writing
with open(file_path, 'r') as file:
    lines = file.readlines()

# Add the text to each line and write back to the same file
with open(file_path, 'w') as file:
    for line in lines:
        modified_line = f"{line.strip()}, {append_text}\n"
        file.write(modified_line)

print(f"The file '{file_path}' has been updated successfully.")