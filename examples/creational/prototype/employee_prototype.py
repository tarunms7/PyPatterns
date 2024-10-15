import copy
from creational.prototype import Prototype

class Employee(Prototype):
    def __init__(self, name, department, skills):
        self.name = name
        self.department = department
        self.skills = skills  # List of skills (mutable)

    def __str__(self):
        return f"Employee(name={self.name}, department={self.department}, skills={self.skills})"

    def clone(self):
        """Perform deep copy of the Employee object."""
        return copy.deepcopy(self)

if __name__ == "__main__":
    # Original employee with skills
    emp1 = Employee("John", "Engineering", ["Python", "C++", "Machine Learning"])

    # Cloning the employee
    emp_clone = emp1.clone()

    # Modify the clone's skills
    emp_clone.skills.append("Deep Learning")

    print("Original Employee:", emp1)
    print("Cloned Employee:", emp_clone)
