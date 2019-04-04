from sympy import *
x1,x2,x3 = symbols('x1 x2 x3')
a11,a12,a13,a22,a23,a33 = symbols('a11 a12 a13 a22 a23 a33')
m = Matrix([[x1, x2, x3]])
n = Matrix([[a11, a12, a13], [a12, a22, a23], [a13, a23, a33]])
v = Matrix([[x1], [x2], [x3]])
# f = m * n * v
# print(f[0].subs({x1:1, x2:1, x3:1}))
f = m * n * v
print(f[0])


# from sympy import *
#
# f = Function('f')
# x = Symbol('x')
# print(dsolve(diff(f(x), x) - 2 * f(x) * x, f(x)))


# from sympy import *
# import pprint
#
# l = [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]},
#      {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]},
#      {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]
#
# pprint.pprint(l)
# print("----------------------")
# n = pprint.pformat(l)
# print(n)


# from sympy import *
#
# f = Function('f')
# x = Symbol('x')
# pprint(2*x-diff(f(x),x))


# from sympy import *
# x = Symbol('x')
# y = Symbol('y')
# print(solve([2 * x - y - 3, 3 * x + y - 7], [x, y]))
#
# from sympy import *
# n = Symbol('n')
# s = ((n+3)/(n+2))**n

#
# from sympy import *
# x = Symbol('x')
# print(limit(1/x**2, x, 0))
# #result
# #oo
# print(limit(x*(sqrt(x**2 + 1) - x), x, oo))
# #result
# #1/2

# from sympy import *
# n = Symbol('n')
# s = ((n+3)/(n+2))**n
# print(limit(s, n, oo))
# #result
# #E

# from sympy import *
# x = Symbol('x')
# print(integrate(6*x**5, x))
#
# t = Symbol('x')
# x = Symbol('x')
# m=integrate(sin(t)/(pi-t),(t,0,x))
# n = integrate(m,(x,0,pi))
# print(n)