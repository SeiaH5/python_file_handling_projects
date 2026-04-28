import os

class even_odd_identifier:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "")
        self.even = []
        self.odd = []

    def create_numbers_file(self):
        print("\n\033[31mnumbers.txt not found.\033[0m")
        print("Plaese enter integers to create the file.")

        with open(self.file_path + "numbers.txt", "w") as file:
            while True:
                try:
                    num = int(input("Press a non-numerical character to stop.\nEnter a number:"))
                    file.write(str(num) + "\n")
                        
                except ValueError:
                    break

        print("\n\033[32mnumbers.txt created successfully.\033[0m\n")

    def numbers_separator(self):
        if not os.path.exists(self.file_path + "numbers.txt"):
            self.create_numbers_file()

        with open(self.file_path + "numbers.txt", "r") as file:
            numbers = file.readlines()

        even_file = open(self.file_path + "even.txt", "w")
        odd_file = open(self.file_path + "odd.txt", "w")

        for num in numbers:
            n = int(num.strip())

            if n % 2 == 0:
                self.even.append(n)
                even_file.write(str(n) + "\n")
            else:
                self.odd.append(n)
                odd_file.write(str(n) + "\n")

        even_file.close()
        odd_file.close()

        print("\nEven numbers:", self.even)
        print("Odd numbers :", self.odd)
        print("\nTotal Even numbers:", len(self.even))
        print("Total Odd numbers :", len(self.odd))

        print("\n\033[32mFiles created successfully.\033[0m")

even_odd_identifier().numbers_separator()