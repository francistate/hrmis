
# Import the necessary modules and classes.
import pytest
from employee import Employee
from manager import Manager
from director import Director
from intern import Intern
from hrmis import HRMIS
import persistence
import os

def test_employee_creation():
    # Test the creation of different employee types
    manager1 = Manager(
        employee_id=122,
        first_name="James",
        last_name="Bond",
        email="j.bond@invi.org",
        department="HR",
        direct_reports=10,
        base_salary=75000,
        pct_allowance_rate=30.0
    )
    assert isinstance(manager1, Manager)

    intern1 = Intern(
        university="University of Kimironko",
        program="Computer Science",
        term_duration=6,
        employee_id=123,
        first_name="John",
        last_name="Downs",
        email="john@example.com",
        department="IT",
        base_salary=50000
    )
    assert isinstance(intern1, Intern)

    director1 = Director(
        employee_id=124,
        first_name="John",
        last_name="Doe",
        department="Academics",
        email="john@example.com",
        base_salary=80000,
        bonus=10000
    )
    assert isinstance(director1, Director)

    employee1 = Employee(
        employee_id=126,
        first_name="John",
        last_name="Doe",
        department="Accounting",
        email="john@example.com",
        base_salary=60000
    )
    assert isinstance(employee1, Employee)

    assert employee1.get_last_name() == "Doe"

def test_attendance_and_persistence():
    # Test attendance recording and persistence functions
    manager1 = Manager(
        employee_id=122,
        first_name="James",
        last_name="Bond",
        email="j.bond@invi.org",
        department="HR",
        direct_reports=10,
        base_salary=75000,
        pct_allowance_rate=30.0
    )
    start_date = "2023-10-01"
    end_date = "2023-10-31"

    # Record intime and out_time for specific dates
    manager1.attendance.record_intime("2023-10-27", "08:00:00")
    manager1.attendance.record_out_time("2023-10-27", "17:00:00")
    manager1.attendance.record_intime("2023-10-28", "08:00:00")
    manager1.attendance.record_out_time("2023-10-28", "16:00:00")

    # Test attendance functions
    assert manager1.attendance.get_attendance_record()  

    total_hours = manager1.attendance.calculate_total_working_hours(start_date, end_date)
    assert total_hours == 17 
     

    # Test persistence functions 
    persistence.serialize_to_json(manager1)
    loaded_manager = persistence.deserialize_from_json(manager1.get_employee_id())
    assert loaded_manager is not None

def test_payslip_generation():
    # Test payslip generation
    test_id = 101
    file_path = persistence.payslip_files_path + str(test_id) + ".txt"
    persistence.create_payslip(test_id)
    assert os.path.exists(file_path)

def test_validators():
    # Test validators for date and time 
    assert HRMIS.is_valid_date("2017-06-17")

    assert not HRMIS.is_valid_date("2017-16-17") 

    assert not HRMIS.is_valid_date("2017-16-dd")

    assert HRMIS.is_valid_time("16:43:56")

    assert HRMIS.is_valid_time("23:43:56")

    assert not HRMIS.is_valid_time("24:43:56")

def test_id_generator():

    assert persistence.generate_new_id()

def test_persistence_functions():

    assert persistence.load_all_employee_ids()

    assert persistence.load_all_employee_ids()

    assert persistence.load_employee_by_id(101)

    assert persistence.deserialize_from_json(101)

    assert persistence.get_employee_record_from_file(101)


def test_HRMIS():
    # >>>> PLEASE NOTE THAT MOST OFTHE METHODS OF HRMIS CLASS USE METHODS 
    # FROM OTHER CLASSES AND MODULES, SOME OF WHICH ARE TESTED HERE. HOWEVER,
    # THE MANNER OF THEIR IMPLEMENTATION MAKES IT HARDER TO IMPLEMENT 
    # AUTOMATIC TESTS FOR THEM AS THEY REQUIRE INPUT FROM USER.
    pass    


if __name__ == '__main__':
    pytest.main()