pages_per_book = int(input())
pages_per_hour = int(input())
days = int(input())

needed_time = pages_per_book // pages_per_hour
needed_time_a_day = needed_time / days

print(needed_time_a_day)
