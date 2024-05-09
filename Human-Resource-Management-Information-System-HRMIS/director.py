from employee import Employee

# Class definition.
class Director(Employee):

    
    # Class constructor
    def __init__(self,employee_id, first_name, 
                 last_name, department, email, 
                 base_salary, bonus) -> None:
        
        self.__bonus = bonus
       
        # Super class constructor call
        super().__init__(employee_id, first_name, last_name, 
                         department, email, base_salary)
        
    
    # Methods
    def set_bonus(self, new_bonus):
        """Sets new bonus"""
        self.__bonus = new_bonus
    
    def get_bonus(self):
        """Returns a director's bonus"""  
        return self.__bonus 
    
    def __str__(self) -> str:
        return super().__str__() + f"\nAnnual Bonus: #{self.__bonus:.2f}"