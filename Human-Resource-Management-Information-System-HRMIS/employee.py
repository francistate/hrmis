from salary import Salary
from attendance import Attendance

# Class Definition.
class Employee:

    # Constructor.
    def __init__(self, employee_id, first_name, 
                 last_name, department, email, 
                 base_salary) -> None:
        
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__department = department
        self.__email = email
        self.__base_salary = base_salary


        self.salary = Salary(self)
        self.attendance = Attendance(self)
        
    # Methods
    def get_employee_id(self) -> str:
        """Returns employee's work ID"""
        return self.__employee_id
            
    def get_first_name(self) -> str:
        """Returns employee's first name"""
        return self.__first_name
    
    def get_last_name(self) -> str:
        """Returns employee's last name"""
        return self.__last_name
    
    def get_email(self) -> str:
        """Returns employee's email address"""
        return self.__email
    
    def get_base_salary(self) -> float:
        """Returns employee's basic salary"""
        return self.__base_salary 
    

    def set_first_name(self, first_name):
        """Set the employee's first name."""
        self.__first_name = first_name

    def set_last_name(self, last_name):
        """Set the employee's last name."""
        self.__last_name = last_name

    def set_email(self, email):
        """Set the employee's email address."""
        self.__email = email

    def set_base_salary(self, base_salary):
        """Set the employee's basic salary."""
        self.__base_salary = base_salary
       
    def get_department(self):
        """Return the department where the employee works."""
        return self.__department

    def set_department(self, department):
        """Sets the department where the employee works."""
        self.__department = department
            
    def __str__(self) -> str:
        return f"\nFull Name: {self.__first_name} {self.__last_name}\
                \nEmployee ID: {self.__employee_id }\
                \nDepartment: {self.__department}\
                \nEmail: {self.__email}\
                \nBasic Annual Salary: ${self.__base_salary:.2f}"