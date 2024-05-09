import json
from datetime import datetime
from employee import Employee
from manager import Manager
from director import Director
from intern import Intern
import os.path


employee_files_path = "./employee_data_files/employee_data.json"
payslip_files_path = "./payslips/"


def initialize_employee_data_files():
    """Initializes employee data file by creating a JSON if not existing"""
    #check if file exists
    file_exists = os.path.isfile(employee_files_path)
    employees_data_all = {}
    if not file_exists:
        with open(employee_files_path, "w") as data_file:
            json.dump(employees_data_all, data_file, indent=4)

def load_all_serialized_employees():
    """Load employee data from file"""
    filename = employee_files_path 
    try:
        # Read the JSON file and parse its contents
        with open(filename, "r") as json_file:
            employees_data_all = json.load(json_file)
        return employees_data_all
    except FileNotFoundError:
         print(f"File {filename} not found. Returning None.")
    return None

def serialize_to_json(employee):
    """Serializes an employee object to a JSON file."""
    filename = employee_files_path
    try:
        # Determine the type of employee and convert it to a dictionary
        if isinstance(employee, Manager):
            employee_dict = {
                "employee_type": type(employee).__name__, 
                "employee_id": employee.get_employee_id(),
                "first_name": employee.get_first_name(),
                "last_name": employee.get_last_name(),
                "email": employee.get_email(),
                "department": employee.get_department(),
                "direct_reports": employee.get_department(),
                "base_salary": employee.get_base_salary(),
                "pct_allowance_rate": employee.get_allowance_rate(),
                "attendance": employee.attendance.get_attendance_record(),
                "monthly_salary": employee.salary.calculate_monthly_salary()
            }
        elif isinstance(employee, Director):
            employee_dict = {
                "employee_type": type(employee).__name__, 
                "employee_id": employee.get_employee_id(),
                "first_name": employee.get_first_name(),
                "last_name": employee.get_last_name(),
                "email": employee.get_email(),
                "department": employee.get_department(),
                "base_salary": employee.get_base_salary(),
                "bonus": employee.get_bonus(),
                "attendance": employee.attendance.get_attendance_record(),
                "monthly_salary": employee.salary.calculate_monthly_salary()
            }
        elif isinstance(employee, Intern):
            employee_dict = {
                "employee_type": type(employee).__name__, 
                "employee_id": employee.get_employee_id(),
                "first_name": employee.get_first_name(),
                "last_name": employee.get_last_name(),
                "email": employee.get_email(),
                "department": employee.get_department(),
                "university": employee.get_university(),
                "program": employee.get_program(),
                "term_duration": employee.get_term_duration(),
                "base_salary": employee.get_base_salary(),
                "attendance": employee.attendance.get_attendance_record(),
                "monthly_salary": employee.salary.calculate_monthly_salary()
            }
        elif isinstance(employee, Employee):
            employee_dict = {
                "employee_type": type(employee).__name__, 
                "employee_id": employee.get_employee_id(),
                "first_name": employee.get_first_name(),
                "last_name": employee.get_last_name(),
                "email": employee.get_email(),
                "department": employee.get_department(),
                "base_salary": employee.get_base_salary(),
                "attendance": employee.attendance.get_attendance_record(),
                "monthly_salary": employee.salary.calculate_monthly_salary()
            }
        else:
            raise ValueError("Invalid employee type")

        with open(filename, "r") as json_file:
            employees_data_all = json.load(json_file)

        employees_data_all[str(employee.get_employee_id())] = employee_dict
        
        # Serialize the employee dictionary to JSON and write it to the file
        with open(filename, "w") as json_file:
            json.dump(employees_data_all, json_file, indent=4)

        print(f"employee serialized to {filename} successfully.")
        
    except Exception as e:
        print(f"Serialization error: {str(e)}")

def deserialize_from_json(employee_id):
    """Deserializes employee data from a JSON file."""
    filename = employee_files_path 
    try:
        # Read the JSON file and parse its contents
        with open(filename, "r") as json_file:
            employees_data_all = json.load(json_file)
        employee_data = employees_data_all[str(employee_id)]
        # Determine the employee type and create a new instance
        if employee_data["employee_type"] == "Manager":
            employee = Manager(
                employee_id = employee_data["employee_id"],          
                first_name = employee_data["first_name"],
                last_name = employee_data["last_name"],
                email = employee_data["email"],
                department = employee_data["department"],
                direct_reports= employee_data["direct_reports"],  
                base_salary = employee_data["base_salary"],
                pct_allowance_rate= employee_data["pct_allowance_rate"],
            )
            employee.attendance.set_attendance_records(employee_data["attendance"])

        elif employee_data["employee_type"] == "Director":
            employee = Director(
                employee_id = employee_data["employee_id"],          
                first_name = employee_data["first_name"],
                last_name = employee_data["last_name"],
                department = employee_data["department"],
                email = employee_data["email"],  
                base_salary = employee_data["base_salary"],
                bonus = employee_data["bonus"]
            )
            employee.attendance.set_attendance_records(employee_data["attendance"])

        elif employee_data["employee_type"] == "Intern":
            employee = Intern(
                university= employee_data["university"],
                program=employee_data["program"],
                term_duration= employee_data["term_duration"],
                employee_id = employee_data["employee_id"],
                first_name = employee_data["first_name"],
                last_name = employee_data["last_name"],
                email = employee_data["email"],
                department = employee_data["department"],
                base_salary = employee_data["base_salary"]
            )
            employee.attendance.set_attendance_records(employee_data["attendance"])

        elif employee_data["employee_type"] == "Employee":
            employee = Employee(
                employee_id = employee_data["employee_id"],          
                first_name = employee_data["first_name"],
                last_name = employee_data["last_name"],
                department = employee_data["department"],
                email = employee_data["email"],  
                base_salary = employee_data["base_salary"]
            )
            employee.attendance.set_attendance_records(employee_data["attendance"])
        else:
            raise ValueError("Invalid employee type in JSON data")

        print(f"employee deserialized from {filename} successfully.")
        return employee
    except FileNotFoundError:
        print(f"File {filename} not found. Returning None.")
    except Exception as e:
        print(f"Deserialization error: {str(e)}. Returning None.")
    return None

def get_employee_record_from_file(employee_id):
    """Reads an employee file and parses its contents."""
    filename = employee_files_path 
    try:
        # Read the JSON file and parse its contents
        with open(filename, "r") as json_file:
            employees_data_all = json.load(json_file)
        employee_data = employees_data_all[str(employee_id)]
        return employee_data
    except FileNotFoundError:
        print(f"File {filename} not found. Returning None.")
    except Exception as e:
        print(f"Deserialization error: {str(e)}. Returning None.")
    return None

def create_payslip(emp_id):
    """Generates employee payslip."""
    employee_id = str(emp_id)
    payslip_file = payslip_files_path + employee_id + ".txt"
    
    
    employee_data = get_employee_record_from_file(employee_id)
    if employee_data != None:
        date = datetime.now().date()
        payslip_data = (
            f"\t\t  PAYSLIP\n\t\t{date}\n\n"\
            f"<< {employee_data['first_name']}"\
            f" {employee_data['last_name']} >> \n\n"\
            f"Dept: {employee_data['department']}\n"\
            f"Gross Salary:"\
            f" ${employee_data['monthly_salary']['Base Salary']:.2f}\n"\
            f"Allowances:"\
            f" ${employee_data['monthly_salary']['Allowances']:.2f}\n"\
            f"Bonuses:"\
            f" ${employee_data['monthly_salary']['Bonuses']:.2f}\n"\
            f"Tax Deductions:"\
            f" ${employee_data['monthly_salary']['Deductions']:.2f}\n"\
            f"Net Earnings:"\
            f" ${employee_data['monthly_salary']['Net Earnings']:.2f}\n"\
            )
                        
        
        with open(payslip_file, "w") as txt_file:
            txt_file.write(payslip_data)

        print("Payslip successfully generated.")
    else:
        print("Error!!! Payslip not generated.")

def load_all_employee_ids():
    """Loads all employee IDs from employee data"""
    emp_data = load_all_serialized_employees()
    if emp_data != None:
        ids_list = [int(x) for x in emp_data.keys()]
        return ids_list
    else:
        return None

def generate_new_id():    
    """Generate a new employee ID if it does not exist already."""
    saved_ids = load_all_employee_ids()

    if saved_ids:
        saved_ids = [int(x) for x in saved_ids]
        new_id =  max(saved_ids) + 1  
        return new_id           
    else:
        print("Error!!! Saved Employees not Loaded.")
        return None
    
def load_employee_by_id(emp_id):
    emps = load_all_serialized_employees()
    return emps[str(emp_id)]

def write_all_employees_to_json(employees):
    try:
        with open(employee_files_path, "w") as data_file:
            json.dump(employees, data_file, indent=4)
    except Exception as e:
        print(f"Error!, {e}")
        