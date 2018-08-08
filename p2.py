#!D:/python/python.exe
import cgi
print ("Content-type: text/html\n")
form=cgi.FieldStorage()
operator=form["cal"].value
#num1=form["Num1"].value
num1=form.getvalue("Num1")
num2=form["Num2"].value
number1=int(num1)
number2=int(num2)
sum1=0
sum2="0"
print("<html>")
print("<h1>Calculator</h1>")
print("<b>Number1 : </b>"+form["Num1"].value+" ")
print("(")

if operator == "1" :
    sum1=number1-number2
    sum2=str(sum1)
    print("-")
elif operator == "2" :
    sum1=number1+number2
    sum2=str(sum1)
    print("+")
elif operator == "3" :
    sum1=number1*number2
    sum2=str(sum1)
    print("*")
elif operator == "4" :
    sum1=number1 / number2
    sum2=str(sum1)
    print("/")
else:
    print("<h1>Error</h1>")
print(")")
print("&nbsp<b>Number2 : </b>"+form["Num2"].value+"<br>")
print("<h4>Result : "+sum2+"</h4>")
print("</html>")
