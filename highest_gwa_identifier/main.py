class student_record:
    def highest_gwa(self):
        with open("student_record.json", "r") as file:
            highest_name = ""
            highest_gwa = 0

        print("Student with highest GWA:")
        print(highest_name, "-", highest_gwa)