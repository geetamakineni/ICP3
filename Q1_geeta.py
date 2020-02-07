salary_list=[]
class Employee:
    emp_count=0
    def __init__(self,name,family,salary,department):
        self.name=name
        self.family=family
        self.salary=salary
        salary_list.append(salary)
        self.department=department
        Employee.emp_count+=1

    def average_salary(self):
        avg=sum(salary_list)/len(salary_list)
        print("Average Salary of Employees:",avg)

class Fulltime_employee(Employee):
    def __init__(self,name,family,salary,department):
        Employee.__init__(self,name,family,salary,department)

emp1=Employee("Satya","Kanugolu",1333,"CS")
emp2=Employee("Akhi","Kanugolu",3333,"CS")
emp3=Fulltime_employee("Padma","Makineni",7555,"CS")
emp4=Fulltime_employee("Seeta","Makineni",4245,"CS")
print ("Employee Count from Employee: %d" % Employee.emp_count)
print ("Employee Count from Full time: %d" % Fulltime_employee.emp_count)
emp2.average_salary()
emp4.average_salary()