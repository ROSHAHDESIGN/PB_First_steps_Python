#Кв. метри, които ще бъдат озеленени
square_m = float(input())

#един кв. м. е 7.61 лв със ДДС.нейният двор
# е доста голям, фирмата предлага 18% отстъпка от крайната цена
final_price_without_discount = square_m * 7.61

discount = final_price_without_discount * 0.18

final_price = final_price_without_discount - discount

print(f"The final price is: {final_price} lv.")
print(f"The final price is: {discount} lv.")

