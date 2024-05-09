
from employee import Employee
from manager import Manager
from director import Director
from intern import Intern
import persistence
from datetime import datetime
import re
from collections import defaultdict

class HRMIS:
    # Class Constructor
    def __init__(self):
        self.employees = {}   
        persistence.initialize_employee_data_files()

    @classmethod    
    def is_valid_date(cls, date_string, date_format="%Y-%m-%d"):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
        
    @classmethod    
    def is_valid_time(cls, time_string):
        """ Checks if time matches"HH:MM:SS" format using regular expressions
         Returns True if match, False if none match """
        time_pattern = r'^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
        return re.match(time_pattern, time_string) is not None

    def add_ordinary_employee(self, new_id):
        """Add an ordinary employee to the HRMIS system.""" 
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        department = input("Enter department: ")
        email = input("Enter email: ")
        base_salary = float(input("Enter base salary: "))
        
        emp = Employee(
            employee_id=new_id,
            first_name=first_name,
            last_name=last_name,
            department=department,
            email=email,
            base_salary=base_salary,            
            )
        persistence.serialize_to_json(emp)

    def add_director(self, new_id):
        """Add a director to the HRMIS system.""" 
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        department = input("Enter department: ")
        email = input("Enter email: ")
        base_salary = float(input("Enter base salary: "))
        bonus = float(input("Enter bonus: "))

        director = Director(
            employee_id=new_id,
            first_name=first_name,
            last_name=last_name,
            department=department,
            email=email,
            base_salary=base_salary,
            bonus=bonus
        )
        persistence.serialize_to_json(director)

    def add_manager(self, new_id):    
        """Add a manager to the HRMIS system."""        
        # Taking input from the user to instantiate the class
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        department = input("Enter department: ")
        direct_reports = int(input("Enter number of direct reports: "))
        base_salary = float(input("Enter base salary: "))
        pct_allowance_rate = float(input("Enter percentage allowance rate: "))

        manager = Manager(
            employee_id=new_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department,
            direct_reports=direct_reports,
            base_salary=base_salary,
            pct_allowance_rate=pct_allowance_rate
        )
        persistence.serialize_to_json(manager)

    def add_intern(self, new_id):
        """Add an intern to the HRMIS system."""
        university = input("Enter university: ")
        program = input("Enter program: ")
        term_duration = int(input("Enter term duration: "))          
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        department = input("Enter department: ")
        base_salary = float(input("Enter base salary: "))

        intern = Intern(
            university=university,
            program=program,
            term_duration=term_duration,
            employee_id=new_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department,
            base_salary=base_salary
        )
        persistence.serialize_to_json(intern)

    def display_employee_list(self):
        employees_data = persistence.load_all_serialized_employees()
        print(f"\nFull Name\tID \t Email\n_____________________________")
        for id, employee_data in employees_data.items():
            first_name = employee_data['first_name']
            last_name = employee_data['last_name']
            email = employee_data['email']
            print(f"{first_name} {last_name} \t{id}\t{email}")
        print()
    
    def display_salary_summary(self):
        employees_data = persistence.load_all_serialized_employees()
        print(f"\nFull Name\tID\tBase Salary\t"
              f"Deductions(Tax)\t Net Pay"
              f"\n_____________________________________________________"
              )
                      
        for id, employee_data in employees_data.items():
            first_name = employee_data['first_name']
            last_name = employee_data['last_name']
            monthly_salary = employee_data['monthly_salary']
            base_salary = monthly_salary["Base Salary"]
            deducts = monthly_salary['Deductions']
            net = monthly_salary['Net Earnings']

            print(f"{first_name} {last_name}\t{id}\t${base_salary:.2f}\t"
                f"${deducts:.2f}   \t${net:.2f}"
                )
        print()

    def validate_employee_id(self):
        all_ids = persistence.load_all_employee_ids()
        valid = False
        while not valid:
            try:
                id = int(input("Enter ID number of Employee from List:  "))
            except Exception as e:
                print(f"Error {e}")
                continue
            if id in all_ids:
                valid = True
            else:
                print("invalid ID entered\n")
        return id

    def display_salary_for_employee(self):

        print("Available Users:\n")
        self.display_employee_list()

        id = self.validate_employee_id()
        employee_data =persistence.load_employee_by_id(id)
        first_name = employee_data['first_name']
        last_name = employee_data['last_name']
        monthly_salary = employee_data['monthly_salary']
        base_salary = monthly_salary["Base Salary"]
        allow = monthly_salary['Allowances']
        bonuses = monthly_salary['Bonuses']
        deducts = monthly_salary['Deductions']
        net = monthly_salary['Net Earnings']

        print(f'Full Name: {first_name} {last_name}')
        print(f'Base Salary: ${base_salary:.2f}')
        print(f'Allowances: ${allow:.2f}')
        print(f'Bonuses: ${bonuses:.2f}')
        print(f'Deductions: ${deducts:.2f}')
        print(f'Net Earnings: ${net:.2f}')

    def calculate_working_hours(self):
        print("Available Users:\n")
        self.display_employee_list()
        emp_id = self.validate_employee_id()
        emp = persistence.deserialize_from_json(emp_id)
        valid = False
        while not valid:
            start_date = input("Enter start date (YYYY-MM-DD): ")
            valid = HRMIS.is_valid_date(start_date)

        valid = False
        while not valid:
            end_date = input("Enter start date (YYYY-MM-DD): ")
            valid = HRMIS.is_valid_date(end_date)  


        working_hours = emp.attendance.calculate_total_working_hours(
            start_date, end_date)
        print(f"{emp.get_first_name()} {emp.get_last_name()} worked for "
              f"{working_hours} hours between {start_date} and {end_date}")  

    def record_attendance(self):
        print("Available Users:\n")
        self.display_employee_list()
        emp_id = self.validate_employee_id()
        emp = persistence.deserialize_from_json(emp_id)
        valid = False
        while not valid:
            date = input("Enter start date (YYYY-MM-DD): ")
            valid = HRMIS.is_valid_date(date)

        valid = False
        while not valid:
            in_time = input("Enter a time (HH:MM:SS): ")    
            valid = HRMIS.is_valid_time(in_time)

        valid = False
        while not valid:
            out_time = input("Enter a time (HH:MM:SS): ")    
            valid = HRMIS.is_valid_time(out_time)
        emp.attendance.record_intime(date, in_time)
        emp.attendance.record_out_time(date, out_time)
        
    def update_employee(self):
        """Update employee information"""
        print("Update Employee. >>>\n")
        print("Available Users:\n")
        self.display_employee_list()

        id = self.validate_employee_id()
        employee_data =persistence.load_employee_by_id(id)
        emp = persistence.deserialize_from_json(id)
        print(f"current data\n {emp}")
        
        print("\n\nEnter the new values:\n")
        new_first_name = input("Enter new first name: ")
        new_last_name = input("Enter new last name: ")
        new_department = input("Enter new department: ")
        new_email = input("Enter new email: ")
        new_base_salary = float(input("Enter new annual base salary: "))

        emp.set_first_name(new_first_name)
        emp.set_last_name(new_last_name)
        emp.set_department(new_department)
        emp.set_email(new_email)
        emp.set_base_salary(new_base_salary)
        persistence.serialize_to_json(emp)


    def remove_employee(self):
        """Remove an employee from the system"""
        self.display_employee_list()
        id = self.validate_employee_id()
        employees_data = persistence.load_all_serialized_employees()
        del employees_data[str(id)]
        persistence.write_all_employees_to_json(employees_data)
        print(f"user with id: {id} deleted")

    def display_attendance_for_employee(self):
        print("Display attendance records for user >>>\n")
        self.display_employee_list()
        id = str(self.validate_employee_id())
        employees_data = persistence.load_all_serialized_employees()        
        if id in employees_data:
            employee_info = employees_data[id]
            if "attendance" in employee_info:
                attendance = employee_info["attendance"]
                print(f"Attendance for Employee ID {id}:")
                for date, data in attendance.items():
                    if "intime" in data and "out_time" in data:
                        intime = data["intime"]
                        out_time = data["out_time"]
                        print(f"Date: {date}, In Time: {intime}, Out Time: {out_time}")
            else:
                print(f"No attendance records found for Employee ID {id}")
        else:
            print(f"Employee with ID {id} not found.")

    def generate_summary_reports(self):
        """Generate and display reports"""
        employees_data = persistence.load_all_serialized_employees()
        total_base_salaries = 0.0
        total_allowances = 0.0
        total_bonuses = 0.0
        total_deductions = 0.0

        for employee_info in employees_data.values():
            if "monthly_salary" in employee_info:
                monthly_salary = employee_info["monthly_salary"]
                total_allowances += monthly_salary.get("Allowances", 0)
                total_bonuses += monthly_salary.get("Bonuses", 0)
                total_deductions += monthly_salary.get("Deductions", 0)
                total_base_salaries += monthly_salary.get("Base Salary", 0)

        print(f"Total Base Salary for Whole Team: ${total_base_salaries:.2f}")
        print(f"Total Allowances for Whole Team: ${total_allowances:.2f}")
        print(f"Total Bonuses for Whole Team: ${total_bonuses:.2f}")
        print(f"Total Deductions the Whole Team: ${total_deductions:.2f}")

        attendance_summary = defaultdict(int)

        for employee_info in employees_data.values():
            if "attendance" in employee_info:
                attendance = employee_info["attendance"]
                for date, data in attendance.items():
                    if "intime" in data and "out_time" in data:
                        attendance_summary[date] += 1
   
        print("\n Attendance Summary for the Whole Team:")
        for date, count in attendance_summary.items():
            print(f"Date: {date}, Total Employees Present: {count}")

    def display_attendance_for_whole_team(self):
        
        print("Attendance for the Whole Team>>>\n")
        employees_data = persistence.load_all_serialized_employees()
        for employee_id, employee_info in employees_data.items():
            if("attendance" in employee_info) and employee_info["attendance"]:
                attendance = employee_info["attendance"]
                print(f"Attendance for Employee with ID {employee_id}:")
                
                for date, data in attendance.items():
                    if "intime" in data and "out_time" in data:
                        intime = data["intime"]
                        out_time = data["out_time"]
                        print(f"Date: {date}, In Time: {intime}, Out Time: {out_time}")
            else:
                print(f"No attendance records found for Employee ID {employee_id}")

    

    def Menu(self):
        """Display and handle user interaction with the HRMIS menu options."""
        while True:
            print("\n________________________________________")
            print("\n##########  HRMIS Menu ##########")
            print("1. Add Employee")
            print("2. Update Employee")
            print("3. Remove Employee")
            print("4. Record Attendance")
            print("5. Display Individual Attendance")
            print("6. Display Team Attendance")
            print("7. Calculate Working Hours For Employee")
            print("8. Display Salary For An Employee")
            print("9. Display Salary Summary for Whole Team")
            print("10. Display Employee List")
            print("11. Generate Summaries of Records")
            print("-1. Exit")

            choice = input("Enter your choice: ")
            print(f"___________________________________________")

            if choice == "1":
                valid = False
                while not valid:
                    print("1. Add Ordinary Employee")
                    print("2. Add Director")
                    print("3. Add Manager")
                    print("4. Add Intern")
                    choice = input("Enter choice: ")
                    if choice in ["1", "2", "3", "4"]:
                        print("valid choice")
                        valid = True
                    else:
                        print("Invalid choice. Please select a valid option.")

                if valid:
                    new_id = persistence.generate_new_id()
                    if new_id == None:
                        new_id = 100

                    if choice == "1":
                        self.add_ordinary_employee(new_id)
                    if choice == "2":
                        self.add_director(new_id)
                    if choice == "3":
                        self.add_manager(new_id)
                    if choice == "4":
                        self.add_intern(new_id)
                    
                    
            elif choice == "2":
                self.update_employee()
                
            elif choice == "3":
                self.remove_employee()
                                
            elif choice == "4":
                self.record_attendance()
               
            elif choice == "5":
                self.display_attendance_for_employee()
                               
            elif choice == "6":
                self.display_attendance_for_whole_team()
               
            elif choice == "7":
                self.calculate_working_hours()

            elif choice == "8":
                self.display_salary_for_employee()                

            elif choice == "9":
                self.display_salary_summary()

            elif choice == "10":
                self.display_employee_list()
                
            elif choice == "11":
                self.generate_summary_reports()
                                
            elif choice == "-1":
                print("Exiting HRMIS...")
                break
            else:
                print("Invalid choice. Please select a valid option.")



