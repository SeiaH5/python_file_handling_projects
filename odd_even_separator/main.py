import os

class even_odd_separator:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "")
        self.even = []
        self.odd = []

    def create_numbers_file(self):
        print("\n\033[31mnumbers.txt not found.\033[0m")
        print("Plaese enter integers to create the file.")

        numbers = []

        while True:
            try:
                num = int(input("Press a non-numerical character to stop.\nEnter a number:"))
                numbers.append(num)
            except ValueError:
                break

        numbers.sort()

        with open(self.file_path + "numbers.txt", "w") as file:
            for num in numbers:
                file.write(str(num) + "\n")

        print("\nnumbers.txt created successfully (sorted).\n")

    def numbers_identifier_separator(self):
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

even_odd_separator().numbers_identifier_separator()