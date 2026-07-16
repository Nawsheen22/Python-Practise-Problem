list_products = [
    {
        "name": "Hp Laptop",
        "brand": "HP",
        "price":1500000,
        "configuration":{
            "ram": "16GB",
            "ssd":"512GB",
        },
        "color":["red","green","blue"]

    },
    {
        "name": "Dell Laptop",
        "brand": "Dell",
        "price":1400000,
        "configuration":{
            "ram": "32GB",
            "ssd":"1TB",
        },
        "color":["red","green","blue"]

    }
]

for item in list_products:
  print(item)
  for color in item["color"]:
    print(color)