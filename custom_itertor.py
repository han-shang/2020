"""
自定义学生类 重写类函数理清for遍历原理

"""
class StudentInterator:
    def __init__(self,data):
        self.__data = data
        self.index = -1

    def __next__(self):
        if self.index == len(self.__data)-1:
            raise StopIteration()
        self.index += 1
        return self.__data[self.index]
class StudentController:
    def __init__(self):
        self.__student_list = []

    def add_student(self,student):
        self.__student_list.append(student)

    def __iter__(self):
        return StudentInterator(self.__student_list)

controller = StudentController()
controller.add_student("小明")
controller.add_student("小红")
controller.add_student("小芳")
controller.add_student("小白")

interator = controller.__iter__()
while True:
    try:
        item = interator.__next__()
        print(item)
    except StopIteration:
        break