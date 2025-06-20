employees = [
    {"id" : "1", "name" : "Karthik", "rateperhour" : 100, "manager" : "Sunil"},
    {"id" : "2", "name" : "Baskar", "rateperhour" : 150, "manager" : "Lenny"},
    {"id" : "3", "name" : "Raja", "rateperhour" : 100, "manager" : "Baskar"},
    {"id" : "4", "name" : "Subha", "rateperhour" : 100, "manager" : "Baskar"},
    {"id" : "5", "name" : "Shambhu", "rateperhour" : 80, "manager" : "Baskar"},
    {"id" : "6", "name" : "Anoosheh", "rateperhour" : 140, "manager" : "Baskar"},
    {"id" : "7", "name" : "Bhargav", "rateperhour" : 60, "manager" : "Sunil"},
    {"id" : "8", "name" : "Kaushik", "rateperhour" : 120, "manager" : "Baskar"},
    {"id" : "9", "name" : "Nikhil", "rateperhour" : 160, "manager" : "Munish"},
    {"id" : "10", "name" : "Renju", "rateperhour" : 70, "manager" : "Baskar"}

]

def main():
    name = input("Enter the name to find Annual Salary: ")
    print("The Annual Salary of", name, "is", find_salary(name))
    print("The number of employees", count_of_employees())
    print("Employee with highest billing rate is", max_rate())

def find_salary(n):
    for employee in employees:
        if(employee["name"] == n):
            return employee["rateperhour"] * 2000

def count_of_employees():
    count = 0
    for employee in employees:
        count += 1
    return count

def max_rate():
    m = employees[0]["rateperhour"]
    for employee in employees:
        if(employee["rateperhour"] > m):
            m = employee["rateperhour"]
            name = employee["name"]
    return name

def manager_dashboard():
    

main()