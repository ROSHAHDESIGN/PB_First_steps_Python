# #•	Баскетболни кецове – цената им е 40% по-малка от
# таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на топка


# Вход
# От конзолата се четe 1 ред:
# Годишната такса за тренировки по баскетбол – цяло число в интервала [0… 9999]
annual_tax = int(input())

trainers = annual_tax * 0.6
cloths = trainers * 0.8
ball = cloths * 0.25
bascetball_adds = ball * 0.2

bascetball_costs = annual_tax + trainers + cloths + ball + bascetball_adds
print(bascetball_costs)

