import xml.etree.ElementTree as ET
import defusedxml.ElementTree

# Load XML file
def load_xml(file_path):
    tree = defusedxml.ElementTree.parse(file_path)
    root = tree.getroot()
    return root

# Create new employee
def create_employee(root, name, age, department):
    employee = ET.SubElement(root, 'employee')
    employee.set('id', str(len(root) + 1))
    ET.SubElement(employee, 'name').text = name
    ET.SubElement(employee, 'age').text = str(age)
    ET.SubElement(employee, 'department').text = department

# Read employee by ID
def read_employee(root, employee_id):
    for employee in root.findall('employee'):
        if employee.get('id') == employee_id:
            return employee
    return None

# Update employee
def update_employee(root, employee_id, name=None, age=None, department=None):
    employee = read_employee(root, employee_id)
    if employee:
        if name:
            employee.find('name').text = name
        if age:
            employee.find('age').text = str(age)
        if department:
            employee.find('department').text = department

# Delete employee
def delete_employee(root, employee_id):
    employee = read_employee(root, employee_id)
    if employee:
        root.remove(employee)

# Save XML file
def save_xml(root, file_path):
    tree = ET.ElementTree(root)
    tree.write(file_path)

# Example usage:
file_path = 'employees.xml'
root = load_xml(file_path)

# Create new employee
create_employee(root, 'Bob Johnson', 35, 'Sales')

# Read employee by ID
employee = read_employee(root, '2')
print(employee.find('name').text)  # Output: Jane Smith

# Update employee
update_employee(root, '1', name='John D.', age=31)

# Delete employee
delete_employee(root, '3')

# Save XML file
save_xml(root, file_path)
