import os
import json

class student_record:
    def __init__(self):
        self.file_path = os.path.dirname(__file__)

    def highest_gwa(self):
        record_file = os.path.join(self.file_path, "student_record.json")

        with open(record_file, "r") as file:
            record = file.read().strip()

            if not record:
                print("Error: JSON file is empty.")
                return

            students = json.loads(record)

        highest_student = None
        highest_gwa = float('inf')

student_record().highest_gwa()