print("Enter the no.s  for  Matrix1 in row_wise order")
fisrtNumber = int(input("Enter 1st element of matrix: "))
secondNumber= int(input("Enter 2nd element of matrix: "))
thirdNumber = int(input("Enter 3rd element of matrix: "))
fourthNumber = int(input("Enter 4th element of matrix: "))
firstList = [fisrtNumber,secondNumber,thirdNumber,fourthNumber ]

print("Enter the no.s for matrix 2 in row_wise order!")
number1 = int(input("Enter 1st element of matrix: "))
number2 = int(input("Enter 2nd element of matrix: "))
number3 = int(input("Enter 3rd element of matrix: "))
number4 = int(input("Enter 4th element of matrix: "))
SecondList = [number1,number2,number3,number4]

def matrix_multiplication(list1, list2):
    a = list1[0]*list2[0] + list1[1]*list2[2]
    b = list1[0]*list2[1] + list1[1]*list2[3]
    c = list1[2]*list2[0] + list1[3]*list2[2]
    d = list1[2]*list2[1] + list1[3]*list2[3]
    result = [a,b,c,d]
    return result

print(matrix_multiplication(firstList,SecondList))

