name = input("Add Your Name: ")
age = input("Add Your age: ")
phone = input("Add Your phone: ")
address = input("Add Your address: ")

thisdict = {
    "name": "BBB",
    "age": "25",
    "phone": "0790222",
    "address": "Amman"
    }

print(thisdict)

thisdict["name"] = name
thisdict["age"] = age
thisdict["phone"] = phone
thisdict["address"] = address

print(thisdict)

def age_valdation(age):
    if int(age) >= 18:
        print("welcome in Python class")
    else:
        print("sorry")
    return age

age_valdation(thisdict["age"])
