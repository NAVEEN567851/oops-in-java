class Company:
    def company_name(self):
        return 'IBM'

class Employee(Company):
    def info(self):
        c_name = super().company_name()
        print("Naveen works at", c_name)

# Creating object of child class
emp = Employee()
emp.info()
