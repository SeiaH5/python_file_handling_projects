import os

class even_odd_multiplier:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "")
        self.double_even = []
        self.triple_odd = []

    def integers_identifier(self):
        with open(self.file_path + "integers.txt", "r") as file:
            numbers = file.readlines()

        double_even_file = open(self.file_path + "double.txt", "w")
        triple_odd_file = open(self.file_path + "triple.txt", "w")

        for num in numbers:
            n = int(num.strip())

            if n % 2 == 0:
                self.double_even.append(n ** 2)
                double_even_file.write(str(n ** 2) + "\n")
            else:
                self.triple_odd.append(n ** 3)
                triple_odd_file.write(str(n ** 3) + "\n")

        double_even_file.close()
        triple_odd_file.close()

        print("\nEven (squared):", self.double_even)
        print("Odd (cubed):", self.triple_odd)

        print("\nTotal Even numbers:", len(self.double_even))
        print("Total Odd numbers :", len(self.triple_odd))

        print("\n\033[32mFiles created successfully.\033[0m")

even_odd_multiplier().integers_identifier()