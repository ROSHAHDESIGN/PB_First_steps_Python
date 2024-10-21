CHICKEN = 10.35
FISH = 12.40
VEGGI = 8.15
DELIVERY = 2.50

chicken_orders = int(input())
fish_orders = int(input())
veggi_orders = int(input())

price_of_chiken_orders = chicken_orders * CHICKEN
price_of_fish_orders = fish_orders * FISH
price_of_veggi_orders = veggi_orders * VEGGI
total_order = price_of_chiken_orders + price_of_fish_orders + price_of_veggi_orders
dessert = 0.20 * total_order

price_of_all = total_order + dessert + DELIVERY
print(price_of_all)
