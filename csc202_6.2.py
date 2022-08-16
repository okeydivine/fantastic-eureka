class Employee:
    def __init__(self, name, id_num, dept, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__dept = dept
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_dept(self):
        return self.__dept

    def get_job_title(self):
        return self.__job_title

def main():
    e1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    e2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    e3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    employees = [e1, e2, e3]
    for i in employees:
        print("~Name: ", i.get_name(),\
            "|#ID: ", i.get_id_num(),\
            "|Department: ", i.get_dept(),\
            "|Job Title: ", i.get_job_title())
        print("")
main()
