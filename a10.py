#A company decide to give a bonus of 5% to an employee if his/her years of service is more than 5 years write a program that
#reads an employee salary and years of service and decides whether employee gets bonus or not

year=eval(input("enter employee year of service: "))
salary=eval(input("enter employee salary: "))
if year>5:
    print("employee is eligible for bonus and employee salary is ",salary+0.05*salary)
else:
    print("employee is not eligible for bonus")
