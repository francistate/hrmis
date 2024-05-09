from employee import Employee


# Class definition
class Manager(Employee):

    # Class constructor
    def __init__(self,employee_id, first_name, last_name, 
                 email, department, direct_reports, 
                 base_salary, pct_allowance_rate) -> None:
        
        self.__direct_reports = direct_reports
        self.__pct_allowance_rate = pct_allowance_rate


        # Super class constructor call
        super().__init__(employee_id, first_name, last_name,
                         department, email,  base_salary)

    # Methods    
    def get_allowance_rate(self):
        """Returns the employee's percentage allowance rate"""
        return self.__pct_allowance_rate
    
    def get_direct_reports(self):
        """Returns the number of direct reports to the employee"""
        return self.__direct_reports
    
    def set_allowance_rate(self, new_rate):
        """Modifies the allowance rate percentage """        
        self.__pct_allowance_rate = new_rate

    def set_direct_reports(self, new_reps):
        """Modifies the number of direct reports to the employee"""
        self.__direct_reports = new_reps

    def __str__(self) -> str:
        return super().__str__() + f"\nNumber of Direct Reports: {self.__direct_reports}\
            \nAllowance rate: {self.__pct_allowance_rate}%"