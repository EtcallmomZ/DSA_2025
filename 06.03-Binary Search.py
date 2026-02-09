import json
class Student:
    def __init__(self,std_id,name,gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return  self.gpa

    def print_details(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

def binary_search(data, name):
    left = 0
    right = len(data) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if data[mid].name == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {comparisons}")
            return

        elif data[mid].name < name:
            left = mid + 1
        else:
            right = mid - 1

    print(f"{name} does not exists.")
    print(f"Comparisons times: {comparisons}")




def main():
    data_input = input()
    search_name = input()

    json_data = json.loads(data_input)

    students = []
    for item in json_data:
        students.append(Student(item["id"], item["name"], item["gpa"]))

    binary_search(students, search_name)


main()