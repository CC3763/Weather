count = 1
cit = []
number = []
g = open('city.txt',encoding='utf-8')
for each_line in g:
    (num,ci) = each_line.split(':')
    cit.append(ci[:-1])
    number.append(num)
city = dict(zip(cit,number))
