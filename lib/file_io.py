def write_file(file_name, file_content):
    """Creates or overwrites a .txt file with the provided content"""
    with open(f'{file_name}.txt', "w") as file: 
        file.write(file_content)

def append_file(file_name, file_content):
    """Append the provided contnet to a .txt file. If the file does not exist, it will be cvreated"""
    with open(f'{file_name}.txt', "a") as file:
        file.write(file_content)
def read_file(file_name):
    """Reads and returns the content of a .text file."""
    with open (f"{file_name}.txt", "r") as file:
        return file.read()