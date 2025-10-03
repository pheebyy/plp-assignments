#Read and write challenge assignment
def modify_content(content):
    """
    Example modification function:
    Converts text to uppercase.
    You can change this logic as needed.
    """
    return content.upper()

def main():
    # Ask user for a filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified = modify_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified)

        print(f"✅ File successfully modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print(" Error: Permission denied. You cannot read this file.")
    except Exception as e:
        print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()
