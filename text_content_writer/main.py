import os

class text_writer:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "")

    def write_text(self):
        file_name = os.path.join(self.file_path, "mylife.txt")

        with open(file_name, "w") as file:
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")
                
                more_input = input("Are there more lines y/n? ").strip().lower()
                if more_input != "y":
                    break

text_writer().write_text()