import os

_, filename = os.path.split("/home/luciano/.ssh/idrsa.pub")
#os.path.split() func builds a tuple(path, last_part)
print(filename)
print(_)

a, *body, c, d = range(5)
print(body)