#creating class employee
class Employee:
    def __init__(self, emp_id, name, basic_salary, tax_rate, bonus=0):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.tax_rate = tax_rate
        self.bonus = bonus
#function to calculate net salary
    def calculate_net_salary(self):
        tax_deduction = self.basic_salary * self.tax_rate
        net_salary = self.basic_salary - tax_deduction + self.bonus
        return net_salary
#function to generate payslip
    def generate_payslip(self):
        payslip = f"""
        ============================
        Employee ID: {self.emp_id}
        Name: {self.name}
        Basic Salary: {self.basic_salary}
        Tax Deduction: {self.basic_salary * self.tax_rate}
        Bonus: {self.bonus}
        Net Salary: {self.calculate_net_salary()}
        ============================
        """
        return payslip
#initilizing value
employee1 = Employee(emp_id="E101", name="Abishek", basic_salary=50000, tax_rate=0.1, bonus=5000)
print(employee1.generate_payslip())
