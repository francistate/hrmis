

from datetime import datetime

class Attendance:
    # Class Constructor
    def __init__(self, employee):
        self.__employee_id = employee.get_employee_id()
        self.__employee = employee
        self.__attendance_records = {}  

    def record_intime(self, date, intime):
        """Records the date and the time an employee logged-in."""
        date = datetime.strptime(date, "%Y-%m-%d")
        date = str(date.date())

        if date not in self.__attendance_records:
            self.__attendance_records[date] = {"intime": intime}
        else:
            self.__attendance_records[date]["intime"] = intime

    # def record_intime(self):
    #     current_time = datetime.now()
    #     date = datetime.now().date()
    #     intime = current_time.strftime("%H:%M:%S")

    #     if date not in self.__attendance_records:
    #         self.__attendance_records[date] = {"intime": intime}
    #     else:
    #         self.__attendance_records[date]["intime"] = intime

    def record_out_time(self, date, out_time):
        """Records the time an employee logs-off work."""
        date = datetime.strptime(date, "%Y-%m-%d")
        date = str(date.date())

        if date in self.__attendance_records:
            self.__attendance_records[date]["out_time"] = out_time

    # def record_out_time(self):
    #     current_time = datetime.now()
    #     date = datetime.now().date()
    #     out_time = current_time.strftime("%H:%M:%S")

    #     if date in self.__attendance_records:
    #         self.__attendance_records[date]["out_time"] = out_time


    def get_attendance_record(self):
        """Returns attendance records."""
        return self.__attendance_records

    def calculate_total_working_hours(self, start_date, end_date):   
        """Calculates the total daily working hours of an employee.""" 
        total_working_hours = 0
        for date, record in self.__attendance_records.items():
            if start_date <= str(date) <= end_date:
                if "intime" in record and "out_time" in record:
                    intime = datetime.strptime(record["intime"], "%H:%M:%S")
                    out_time = datetime.strptime(record["out_time"], "%H:%M:%S")
                    time_difference = out_time - intime
                    total_working_hours += time_difference.total_seconds()/3600

        return total_working_hours
    
    def set_attendance_records(self, records):
        """Sets a previously saved attendance records."""
        self.__attendance_records = records
        
    def display_attendance_records(self):
        """Displays the individual employees' attendance records."""
        print(f"Attendance records for {self.__employee.get_first_name()}"\
            f" {self.__employee.get_last_name()} "\
            f"\nID Number:{self.__employee.get_employee_id()} \n"\
            f"_______________________________________________"  
            )
        for date, record in self.__attendance_records.items():
            print(f"Date: {date}")
            if 'intime' in record:
                print(f"Intime: {record['intime']}")
            if 'out_time' in record:
                print(f"OutTime: {record['out_time']}")
            print()  
        print(f"_______________________________________________")


