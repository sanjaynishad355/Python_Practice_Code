print("Print Demo")
print() # for leaving line
print("Welcome")
print(print()) # None
print("-------------------")
print("Python Features")
print("Highlevel",end=",") # end for continuing in same line
print("Interpretive") # ans - Highlevel,Interpretive
print("Integrated")
features=print("Easy to code or learn or debug") # ans - Easy to code or learn or debug
# print(features) # None
print("-----------------------------")
end="," # local variable
print("works of end =",end)
print("Robustness")
print("Platform Independent")
print("------------------------------")
year=2024
print(year,print(print("Welcome")))
'''ans of print(year,print(print("Welcome"))) - 
welcome
None
2024 None'''
print("--------------------------------")
print("1python is easy language",sep='') # ans - 1python is easy language
print("2python","is","easy","language") # ans - 2python is easy language
print("3python","is","easy","language",sep=" ") # ans - 3python is easy language
print("4python","is","easy","language",sep="") # ans - 4pythoniseasylanguage
print("5python","is","easy","language",sep=",") # ans - 5python,is,easy,language
msg="python","is","easy","language"
print(msg) # ans - ('python', 'is', 'easy', 'language')
print("Hi","Hello",sep=' ',end=' ')
print("welcome") # ans - Hi Hello welcome

print("========inputsmt===========")

name=input()
age=input()
print(name)
print(age)
# name,age=input() # error
#name,age="aaa" # error 
name="zzz"
age=23
print(name)
print(age)

print("Name=",name)
print("Age=",age)

print("========keywords==========")

import keyword

print(keyword.kwlist)

print(len(keyword.kwlist))

print("------Student Marksheet--------")

name=input("enter your name=")
rollno=input("enter your rollno=")
print("Enter marks for below subjects=")
python=int(input("python="))
html=int(input("html="))
js=int(input("js="))
sql=int(input("sql="))
css=int(input("css="))
total=python+html+js+sql+css
per=total/5
print("------------------")
print("Name=",name)
print("Rollno=",rollno)
print("Total marks=",total)
print("Percentage=",per)