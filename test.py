import api

api.update_item("Apple",0.1,12)
api.update_item("Orange",0.15,33)
api.update_item("Blueberry",0.20,6)
api.update_item("Raspberry",0.1,0)

print(api.fetch("Apple"))
print(api.fetch("Orange"))

api.purchase("Apple")
api.purchase("Raspberry")
api.purchase("Grape")
api.purchase("Orange")

print(api.fetch("Apple"))
print(api.fetch("Raspberry"))

print(api.fetch_all(1))
print(api.fetch_all(0))
