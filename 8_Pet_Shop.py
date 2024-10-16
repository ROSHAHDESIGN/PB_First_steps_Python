#input
one_pack_for_dog = float(input())
one_pack_for_cat = int(input())

# one_pack_for_dog = 2.5
# one_pack_for_cat = 4
price_of_dogs_pack = one_pack_for_dog * 2.5
price_of_cats_pack = one_pack_for_cat * 4

#"{крайната сума} lv."
pet_cost = price_of_dogs_pack + price_of_cats_pack
print(f"{pet_cost} lv.")