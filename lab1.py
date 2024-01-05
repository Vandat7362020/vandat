class Employee:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class EmployeeManagementSystem:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.employee_list:
            if employee.id == employee_id:
                self.employee_list.remove(employee)
                return True
        return False

    def update_employee(self, employee_id, new_name, new_age):
        for employee in self.employee_list:
            if employee.id == employee_id:
                employee.name = new_name
                employee.age = new_age
                return True
        return False

    def view_all_employees(self):
        for employee in self.employee_list:
            print(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}")

# Sử dụng phần mềm quản lý nhân viên
ems = EmployeeManagementSystem()

# Thêm nhân viên
employee1 = Employee(1, "John Smith", 30)
ems.add_employee(employee1)

employee2 = Employee(2, "Jane Doe", 25)
ems.add_employee(employee2)

# Xem tất cả nhân viên
ems.view_all_employees()
# Kết quả:
# ID: 1, Name: John Smith, Age: 30
# ID: 2, Name: Jane Doe, Age: 25

# Cập nhật thông tin nhân viên
ems.update_employee(2, "Jane Johnson", 26)

# Xem lại danh sách nhân viên sau khi cập nhật
ems.view_all_employees()
# Kết quả:
# ID: 1, Name: John Smith, Age: 30
# ID: 2, Name: Jane Johnson, Age: 26

# Xóa nhân viên
ems.remove_employee(1)

# Xem lại danh sách nhân viên sau khi xóa
ems.view_all_employees()
# Kết quả:
# ID: 2, Name: Jane Johnson, Age: 26
