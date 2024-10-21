
deposit_sum = float(input())
deposit_term = int(input())
interest_rate = float(input())

interest_rate_percentage = interest_rate / 100
final_sum = deposit_sum + deposit_term * ((deposit_sum * interest_rate_percentage)/12)

print(final_sum)
