import os
import json

class student_record:
    def __init__(self):
        self.file_path = os.path.dirname(__file__)

    def highest_gwa(self):
        record_file = os.path.join(self.file_path, "student_record.json")

        try:
            with open(record_file, "r") as file:
                record = file.read().strip()
                students = json.loads(record)
        
        except json.JSONDecodeError:
            print("\n\033[31mJSON file is empty or invalid.\033[0m\n")
            return

        except FileNotFoundError:
            print("\n\033[31mFile not found.\033[0m\n")
            return

        if not students:
            print("\n\033[31mNo student records found.\033[0m\n")
            return

        highest_name = None
        highest_gwa = float(5.00)

        for student in students:
            if student["gwa"] < highest_gwa:
                highest_gwa = student["gwa"]
                highest_name = student["name"]

        print("\n\033[1mStudent with highest GWA:\033[0m")
        print(highest_name, "-", highest_gwa, "\n")

student_record().highest_gwa()