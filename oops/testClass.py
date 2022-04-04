from classBasics import Student;
from classBasics import Complex;
from classBasics import Triangle;

num1 = Complex(4,5)
num2 = Complex(-3,4)
result  = num1.add(num2);
print(result.real, result.imag)


st1 = Student('Gulam Mustafa',28,'Male','gulam@tesseract.in')
details = st1.studentDetails()
print(details)

t1 = Triangle(4,5,6);
area = t1.areaOfTrangle();
print(area)