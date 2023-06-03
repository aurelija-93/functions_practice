# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    return get_total_cash(pet_shop)

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num_of_pets):
    pet_shop["admin"]["pets_sold"] += num_of_pets
    return get_pets_sold(pet_shop)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets = []
    index = 0
    for pet in pet_shop["pets"]:
        pet_breed = pet_shop["pets"][index]["breed"]
        if pet_breed == breed:
            pets.append(pet)
        index += 1
    return pets

def find_pet_by_name(pet_shop, name):
    index = 0
    for pet in pet_shop["pets"]:
        pet_name = pet_shop["pets"][index]["name"]
        if pet_name == name:
            return(pet)
        index += 1

def remove_pet_by_name(pet_shop, name):
    index = 0
    for pet in pet_shop["pets"]:
        pet_name = pet_shop["pets"][index]["name"]
        if pet_name == name:
            del pet_shop["pets"][index]
            index -= 1
        index += 1

def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    return get_customer_cash(customer)

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

# --- OPTIONAL ---

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False