from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 37, (35, 139))


print(tokyo)


print(City._fields)
