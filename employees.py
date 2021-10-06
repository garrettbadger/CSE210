class Address:
    def __init__(self):
        self.house_number = 0
        self.street = ""
        self.city =""
        self.state = ""
        self.zip = ""

class Employee:
    def __init__(self):
        self.first = ""
        self.last = ""
        self.id =""
        self.salary = 0
        self.home_address = Address()

    def print_email_signature(self, greeting):
        print(f"{greeting}, {self.first}")


def print_paycheck(emp):
    print(f"Printing paycheck for {emp.first} {emp.last}")

def main():
    print("Hello World")
    emp1 = Employee()
    emp1.first = "Jim"
    emp1.last ="Bob"
    emp1.id = "12abc"
    emp1.salary = 80000

    emp1.print_email_signature("Best regards")

    emp2 = Employee()
    emp2.first ="George"
    emp2.last ="Bush"
    emp2.id ="34def"
    emp2.salary = 1

    emp2.print_email_signature("Cool dude")

    print_paycheck(emp1)
    print_paycheck(emp2)





if __name__ == "__main__":
    main()