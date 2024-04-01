def map(keys): 
    current_room = ""
    if "s" in keys: 
        current_room = "shop"
    if current_room == "shop": 
        print("your in a shop")