from employee import Employee

class Company:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
        
    def display_employees(self):
        print("Employees in the company:")
        for i in self.employees:
            print(i.first_name, i.last_name)
            print("-------------------------")
            
    def pay_employees(self):
        print("Paying employees:")
        for i in self.employees:
            print("Paycheck for:", i.first_name, i.last_name)
            print("Amount:", i.calculate_paycheck())
            print("-------------------------")
        
def main():
    my_company = Company()
    
    employee1 = Employee("Tom", "Mwangi", 50000)
    my_company.add_employee(employee1)
    employee2 = Employee("Jane", "Doe", 60000)
    my_company.add_employee(employee2)
    employee3 = Employee("John", "Nyachuka", 25000)
    my_company.add_employee(employee3)
    
    my_company.display_employees()
    my_company.pay_employees()

main()