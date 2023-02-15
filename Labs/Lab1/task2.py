Student1 = {'Name': 'Saher', 'HWMarks': [69, 62, 82, 59],'QuizMarks': [61, 38, 33, 39], 'ProjectMarks': [36, 37, 45, 34]}
Student2 = {'Name': 'Zeemal', 'HWMarks': [41, 64, 45, 34],'QuizMarks': [64, 30, 34, 34], 'ProjectMarks': [32, 34, 45, 34]}
Student3 = {'Name': 'Laiba', 'HWMarks': [48, 63, 45, 33],'QuizMarks': [66, 30, 34, 34], 'ProjectMarks': [33, 34, 45, 34]}
mylist = []
mylist.append(Student1)
mylist.append(Student2)
mylist.append(Student3)
print(mylist)
def print_students(arg):    
    for key in arg.keys():
        print(key,"=",arg[key])
print_students(Student1)
def average(arg):
    num = len(arg)
    sum = 0
    i = 0
    for i in range(num):
        sum = sum + arg[i]
    avg = sum/num
    return avg
avg = average(Student1)["QuizMarks"]
print(avg)
def get_avg_of_student(arg):
    HWMarks = average(arg["HomeworkMarks "])
    QuizMarks = average(arg["QuizMarks "])
    tuple(HWMarks,QuizMarks)
    return tuple
    
mytuple = get_avg_of_student(Student1)
print(mytuple)
def weightedAvg(arg1,arg2):
    w_avg = arg1[0]*0.25+arg1[1]*0.4+arg2*0.35
    return w_avg
weightMarks =weightedAvg(mytuple,Student1["ProjectMarks"])
print(weightMarks)
def get_letter_grade(arg):
        if (arg>80 and arg<100):
            grade = "A"
        elif(arg>69 and arg<80):
            grade = "B"
        elif(arg>59 and arg<70):
            grade = "C"
        elif(arg>49 and arg<60):
            grade = "D"
        else:
            grade = "F"
        studentGrade = get_letter_grade(weightMarks)
        print(studentGrade)
def  get_class_average(arg):
        number = len(arg)
        sum = 0
        i = 0
        for i in range(number):
            sum = sum + arg[i]
        average = sum/number
        return average

            
            

