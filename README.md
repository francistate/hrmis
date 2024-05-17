# Human-Resource-Management-Information-System-HRMIS
### _04638A Programming Assignment 2_

The Human Resource Management Information System (HRMIS) is a Python-based application designed to manage employee information, attendance, and salaries within an organization. This system provides functionalities to add, update, and remove employees, record attendance, calculate salaries, and generate attendance reports and payslips.

---

## Table of Contents

- [Class Structure](#class_structure)
- [Methods](#methods)
- [Data Persistance Module](#data_persistence)
- [Usage](#usage)
- [Testing](#testing)
- [Contact Information](#contact_information)

---
## Class Structure

### Employee (Base Class)

The `Employee` class is the base class for all types of employees. It includes the following attributes:

- `employee_id`: A unique identifier for the employee.
- `first_name`: First name of the employee.
- `last_name`: Last name of the employee.
- `email`: Email address of the employee.
- `department`: Department of the employee.
- `base salary`: The annual salary of the employee in dollars.

It also includes the `__str__` method to display basic employee information and the `calculate_earnings` method which returns the salary for a regular employee.

### Manager (Derived Class)

The `Manager` class represents a manager with additional attributes `department` and `direct_reports`, the number of direct reports. A manager earns a management support allowance computed as a percentage(0-60) of the salary, plus the base salary.

### Director (Derived Class)

The `Director` class represents a director with attributes `department` and annual `bonus`. A director earns a bonus, on top of the salary.

### Intern (Derived Class)

The `Intern` class represents an intern with attributes `university` (name), `program` (name), and internship term duration.

### Salary (Contained Class)

The `Salary` class is encapsulated within the `Employee` class, inheriting attributes from both the `Employee` class and its subclasses. Its primary responsibility is to conduct salary calculations for all employees. This involves initially determining the applicable tax rate based on the range in which the base salary falls.

### Attendance (Contained Class)

The `Attendance` class is encapsulated within the `Employee` class, inheriting attributes from the `Employee` class and its subclasses. Its primary responsibility is to record the attendance of each employee by tracking the in-time and out-time for each workday. Additionally, it provides functionality to display both individual and team attendance records, offering insights into employees' work patterns.

### HRMIS Class

The `HRMIS` (Human Resource Management Information System) class serves as the central hub for effective HR administration and it allows the HR Manager to add, update, and remove employee records. The `HRMIS` facilitates `attendance tracking`, by capturing `in-time` and `out-time` data for each workday. The class also offers a report generation feature, providing insightful summaries on various aspects of employee management. With built-in 
serialization and deserialization capabilities, the HRMIS ensures persistent storage of employee data in JSON format, enhancing data integrity and accessibility.

---
## Methods
Relevant getter and setter methods are included in the `Employee` and its derived classes.

### Salary Class Methods
The `Salary` class has the following methods:
- `determine_tax_percentage()`: Determines the tax bracket based on the employee's base salary.
- `calculate_monthly_salary()`: Calculates the monthly salary, factoring in deductions and bonuses.
- `display_monthly_salary()`: Displays a breakdown of the monthly salary.

### Attendance Class Methods
The `Attendance` class has the following methods:
- `record_intime()`: Records the employee's work start time.
- `record_out_time()`: Records the employee's log-off time.
- `calculate_total_working_hours()`: Calculates the total daily working hours for an employee.
- `display_attendance_records()`: Displays the attendance records for each employee within a specified period.
-----
## Data Persistence Module
The Data Persistence Module has the following functions:

- `initialize_employee_data_files()`: Initializes employee data files by creating or overwriting a JSON file for storing employee data.
- `serialize_to_json()`: Serializes an employee object to a JSON file, capturing details such as type, ID, name, email, department, base salary, allowance rate, attendance records, and monthly salary.
- `deserialize_from_json()`: Deserializes employee data from a JSON file, reconstructing employee objects with associated details like type, ID, name, email, department, base salary, bonus (if applicable), attendance records, and monthly salary.
- `get_employee_record_from_file()`: Retrieves an employee's record from a JSON file based on the provided ID, including details like type, name, email, department, base salary, bonus (if applicable), attendance records, and monthly salary.
- `create_payslip()`: Generates a payslip for each employee with a salary breakdown.
- `load_all_employee_ids()`: Loads and returns all employee IDs stored in a text file, providing a list of IDs or returning None if the file is not found.
- `generate_new_id()`: Generates a new employee ID if it does not already exist.
- Other.

`__str__` methods are included for the `Employee` class and its derived classes. Those in derived classes call that in the super.

---
## Usage
### Prerequisites
1. Python
- Please ensure that you have Python installed on your system. Python can be downloaded from the [official Python website](https://www.python.org/downloads/).

2. Pytest
- To run the tests, make sure you have pytest installed. If not, you can install it  by running `pip install pytest` in your terminal.


3. Additional Considerations
- Editor/IDE - Using a code editor or integrated development environment is encouraged. Examples include Visual Studio, PyCharm, Atom, etc.
- Download Visual Studio - [Download Visual Studio here](https://code.visualstudio.com/download).


### Using this Code
To use this code:
1. open the project folder in an IDE of your choice
2. either run `python main.py` command in terminal OR open the `main.py` file and click run. However, the implementation accessible from this is incomplete.




---

## Testing
- This project includes a suite of tests using the pytest framework.
- After installing pytest, navigate to the project directory and run `pytest tests.py` in the terminal and this command will discover and execute all test cases in the project.
- The test cases cover various aspects of the classes and functionalities, validating the correctness and robustness of the HRMIS system.
- Some of the test cases are bundled together in functions according to functionality and associations.



## Contact Information
#### Contributor 1
* Name: _Francis Tatenda Chekure_
* GitHub: [@francistate](https://github.com/francistate)

#### Contributor 2
* Name: _Melinda Tatenda Mudzurandende_
* GitHub: [@melitatenda](https://github.com/melitatenda)
---
