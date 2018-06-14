import re
# s = 'Shawnee, OK 074804'
# a = re.findall(r"\d\d\d\d\d", 'Shawnee, OK 74804')
# b = re.search(r"\d\d\d\d\d", s).group()
#
# print(a)
# print(b)
# print(type(b))
# # print(filter(str.isdigit(), s))

# s ="13/32/31 01/19/90"
#
# print (re.findall("(?: 0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|3[0-1])/\d\d", s))


# s = 'Find. The sentences? Yes!'
#
# print(re.findall(r'\d{3}(?:\s|-)\d{2}(?:\s|-)\d{4}', s, re.IGNORECASE))


# s = input("input a string:")
# s = 'a123b\
#     123ab\
#     ab123'
# print(s)
# print("===>")
# print(re.findall(r'\d+', s, re.M))
#
#


s = 'condiexpression, condiexpllll, expressions, explllll'
print(s)
# s = '*'

# pa = re.compile(r"\b((0[0-9]|1[0-2])|([01]\d|2[0-3])):[0-5]\d:?([0-5]\d)?\b")

pa = re.compile(r'(condi)?exp(?(1)ressions|lllll)')
m = pa.search(s)
# m = pa.findall(s)
# n = pa.sub(r"(\1) \2-\3", s)
# print(n)
print(m)
# print(m.start())





