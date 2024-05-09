

class Salary:
    # Class Constructor
    def __init__(self, employee):
    
        self.__employee = employee
        self.__employee_id = employee.get_employee_id()
        self.__base_salary = employee.get_base_salary()
        if (type(self.__employee).__name__) == "Director":
            self.__bonus = employee.get_bonus()
            self.__term_duration = 12
            self.__pct_allowance_rate = 0
        elif (type(self.__employee).__name__) == "Manager":
            self.__bonus = 0
            self.__term_duration = 12
            self.__pct_allowance_rate = employee.get_allowance_rate()

        elif (type(self.__employee).__name__) == "Intern":
            self.__bonus = 0
            self.__term_duration = employee.get_term_duration()
            self.__pct_allowance_rate = 0
        else:
            self.__bonus = 0
            self.__term_duration = 12
            self.__pct_allowance_rate = 0    
        
        self.__deductions = 0 


    def get_base_salary(self):
        """Returns an employees' base salary."""
        return self.__base_salary
    
    def determine_tax_percentage(self):
        """Calculates and returns the tax pecentage based on base salary"""
        base_salary = self.__employee.get_base_salary()
        tax_bands = [0, 20000, 50000, 75000, 100000, 150000, 200000]
        band_percentages = [5, 7.5, 10, 13, 18, 25]
        if base_salary >= 200000:
            tax_perc = band_percentages[-1]
        else:
            for index in range(len(tax_bands)-1):
                if (base_salary >= tax_bands[index]) and (base_salary < tax_bands[index + 1]) :
                    tax_perc = band_percentages[index]
        return tax_perc

    def calculate_monthly_salary(self):
        """Calculates the monthly salary of an employee and returns its breakdown as a dictionary"""
        self.__deductions = self.__base_salary * self.determine_tax_percentage()/100
        allowances = (self.__pct_allowance_rate*self.__base_salary/100)
        monthly_earnings = (self.__base_salary + self.__bonus + allowances - self.__deductions )/12
        return {"Base Salary": self.__base_salary/12,
                "Allowances": allowances/12,
                "Bonuses": self.__bonus/12,
                "Deductions": self.__deductions/12,
                "Net Earnings": monthly_earnings}
        

    def display_monthly_salary(self):
        """Displays the monthly salary of an employee and its breakdown as a dictionary."""
        calc_salary = self.calculate_monthly_salary()
        for key, value in calc_salary.items():
            print(f"{key}: ${value:.2f}")

    





