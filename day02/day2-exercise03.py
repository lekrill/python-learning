#Devices List

#Nested List & Dictionary Declaration
devices = [ 
    {"name": "MSI Ryzen 5", "type01": "Laptop","type02": "AMD"},
    {"name": "Dell Optiplex Micro", "type01": "Server","type02": "Intel"},
    {"name": "Potato Mk. 3", "type01": "Desktop","type02": "AMD"}
]

for devx in devices:
     print(devx["name"], devx["type01"])


#Filter

for devx in devices:
    if devx["type02"] == "AMD":
        print(devx["name"], "is AMD")
    else:
        print(devx["name"], "is Intel")

