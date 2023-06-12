# lst = []
# # проблема late building
# for i in (1,2):
#     def inner(x):
#         return x ** i
#     lst.append(inner)
# # хотим получить список степени 5

# # for p in lst:
# #     print(p(5))



# def sum(x:int, y:int)-> int: #x,y параметры
#     return x + y

# def foo(x,y,operation):
#     return operation

# print(foo(2,3,sum(5,3)))
def foo():
    for i in range(10):
        yield i**2

print(list(foo()))

s = "asdf"

print(dir(iter(s)))

# for i in foo:      
    # print(foo())