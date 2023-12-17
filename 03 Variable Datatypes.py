# comments- documentation section
# single line and Multiline
# Single-line represented by #
# Multi-line represented by triple quotes(single''' ''' or double""" """)

# n=5+6
"""m=324
k=3423
paral="dfdffd
dffdf
dfdgfgf
fgfgfgfg
fgfgf" """

#------working of quotes in variables--------
name = "rrrr"
myname = "aaaaaa"
fname = "gggggg"
lname = """ddddd"""
print(name, myname, fname, lname)
print(name)
name1 = '"welcome"'
print(name1)
msg = "Python isn't fast? is it true"
print(msg)
msg1 = "Python isn't fast? is it true"
print(msg1)

features = """1)python is fast
2)independent
3)customize
4)more libraries
5)easy debug"""
print(features)

expression1 = 23 + 43 / 45 * 234 - 23 / 4 * 34
print(expression1)

# ------ escape chahracter sequence
# \' , \\, \n, \t, \a, \r
print("It's alright")
print("\ This will insert backslash(\\)")
i = "\ This will insert backslash(\\)"
print(i)
print("Hello\nworld")
print("Hello\tworld")
print("Hello\rworld")
msg = "good\rmorning"
print(msg)

# datatypes
# Built in Datatypes
n = 45
print("type of n=", type(n),id(n)) # int
n = 77
print(id(n))
m = 45.35684
print("type of m=", type(m)) # float
c = 234j + 34
print("type of c=", type(c), c) # complex
s = "aaa"
print("type of s=", type(s), s) # string
chr = "A"
print("type of chr=", type(chr), chr) # string
msg = "2351jgff##%%"
print("type of msg=", type(msg), msg) # string
t = True
print("type of t=", type(t), t) # boolean
f =  False
print("type of f=", type(f), f) # boolean
q = None
print("type of q=", type(q), q) # None
h = ""
print("type of h=", type(h), hasattr) # string
k = "\n"
print("type of k=", type(k), k) # string

# Collection datatypes
color = ["red", 345, "blue"]
print("type of color=", type(color), color) # list
color1 = {"red", 345, "blue"}
print("type of color1=", type(color1), color1)  # set
color2 = ("red", 345, "blue")
print("type of color2=", type(color2), color2)  # tuple
users = {1: "aaaa", 2: "bbbb"}
print("type of users=", type(users), users)  # dictionary

# variables - identifier or label which used to store some value

# Rules
# Variables cannot start with digits or special character except _(underscore)
# White spaces are not allowed in variable name
# keywords name cannot be used for variable name
# cannot use special character except _(underscore)
# Always start variable name with upper or lower characters
# Whenever value is string or special char then put it in quotes

_ = 67
print(_)
___ = 3568
print(___)
print(_, ___)
# 1name = "kjdkjdfdk"
# name = "kjdkjdf" comment
# _&name = "jdbjs" invalid
# name&rollno = "jdbjfbjf"&34 invalid

# _rollno_name = 12_"dfdfdf" error
_rollno_name = "12_djkfdj" # correct

# name rollno = "hjdfdj" 12 invalid

name, rollno = "cdkjd", 12 # multi assign variable
namerollno = "cxjc", 12
print(namerollno)
# name1, rollno1 = "sjjkds 12" error cannot assign one value to multiple variable
# print(name1, rollno1)

# def = 3565 error keyword name cannor be used
_def = 3562 # correct variable