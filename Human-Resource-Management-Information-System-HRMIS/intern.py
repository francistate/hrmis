from employee import Employee

# Class definition.
class Intern(Employee):

    # Class constructor
    def __init__(self, university, program, term_duration,
                 employee_id, first_name, last_name, email, 
                 department, base_salary) -> None:
        
        self.__university = university 
        self.__program = program
        self.__term_duration = term_duration

        # Super class constructor call
        super().__init__(employee_id, first_name, last_name,
                         department, email, base_salary)

        
    def get_university(self):
        """Return the university where the intern is enrolled."""
        return self.__university

    def set_university(self, university):
        """Sets the university where the intern is enrolled."""
        self.__university = university

    def get_program(self):
        """Return the program of study for the intern."""
        return self.__program

    def set_program(self, program):
        """Sets the program of study for the intern."""
        self.__program = program

    def get_term_duration(self):
        """Returns the internship duration for an intern."""  
        return self.__term_duration

    def set_term_duration(self, term_duration):
        """Sets the internship duration for an intern."""
        self.__term_duration = term_duration  
    
    def __str__(self) -> str:
        return super().__str__() + f"\nUniversity: {self.__university}\
            \nStudy Program: {self.__program}\
            \nInternship Duration: {self.__term_duration}"