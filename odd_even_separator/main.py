


class even_odd_identifier:
    def __init__(self):
        self.file_path = "C:\\Users\\User\\Documents\\Coding\\Projects\\simple_file_handling_projects\\odd_even_separator\\" #file directory
        self.even = []
        self.odd = []

    def separate_numbers(self):
        with open("numbers.txt", "r") as file:
            numbers = file.readlines()

        even_numbers = open("even.txt", "w")
        odd_numbers = open("odd.txt", "w")

        for num in numbers:
            n = int(num.strip())

            if n % 2 == 0:
                even_numbers.write(str(n) + "\n")
            else:
                odd_numbers.write(str(n) + "\n")

        even_numbers.close()
        odd_numbers.close()
        print("Even and odd numbers saved successfully.")