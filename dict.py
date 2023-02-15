a = {"name": "Hari", "Age": 24, "Place": "Kerala"}

a["name"] = "John"
print(a)

for x, y in a.items():
    print(x, y)

b = a.copy()
print(b)