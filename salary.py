class Employee:  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.emp_count)
        
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))  
  
  
empa = Employee("Emir", 3000)  
empb = Employee("David", 2000)  
empa.display_employee()  
empb.display_employee()  
print("Всего сотрудников: %d" % Employee.emp_count)