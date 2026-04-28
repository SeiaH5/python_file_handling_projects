
class even_odd_identifier:
    def __init__(self):
        self.file_path = "C:\\Users\\User\\Documents\\Coding\\Projects\\simple_file_handling_projects\\odd_even_separator\\" #file directory
        self.even = []
        self.odd = []

    def numbers_separator(self):
        with open(self.file_path + "numbers.txt", "r") as file:
            numbers = file.readlines()

        even_numbers = open(self.file_path + "even.txt", "w")
        odd_numbers = open(self.file_path + "odd.txt", "w")

        for num in numbers:
            n = int(num.strip())
            if n % 2 == 0:
                even_numbers.write(str(n) + "\n")
            else:
                odd_numbers.write(str(n) + "\n")

        even_numbers.close()
        odd_numbers.close()
        print("Even and odd numbers saved successfully.")

even_odd_identifier().numbers_separator()