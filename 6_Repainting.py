# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър
COVER = 1.5
PAINT = 14.5
THINNER = 5.0
BAGS = 0.4

needed_cover = int(input()) #+2 кв.м. найлон отгоре
needed_paint = int(input()) #+ 10% от количеството боя отгоре
needed_thinner = int(input())
work_hours = int(input())

cost_cover = (needed_cover + 2 )* COVER
cost_paint = (needed_paint +( needed_paint * 0.1)) * PAINT
cost_thinner = needed_thinner * THINNER
cost_supplies = cost_cover +cost_paint +cost_thinner + BAGS

#за 1 час работа, е равна на 30% от сбора на всички разходи за материали
cost_hour_work = (cost_supplies * 0.30)* work_hours
cost_repainting = cost_supplies + cost_hour_work
print(cost_repainting)
