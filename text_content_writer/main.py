import os

class text_writer:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "")

    def write_text(self):
        file_name = os.path.join(self.file_path, "mylife.txt")
        print("\n\033[1mMY LIFE TEXT\033[0m")

        with open(file_name, "w") as file:
            while True:
                line = input("\nEnter line: ")
                file.write(line + "\n")
                
                while True:
                    more_input = input("Are there more lines y/n? ").strip().lower()
                    if more_input in ["y", "n"]:
                        break
                    else:
                        print("\n\033[31mY or N only. Try again\033[0m\n")
                        continue
                
                if more_input == "n":
                        print("\n\033[1m---END---\033[0m")
                        break
        

text_writer().write_text()