def days():
    day_names = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    while True:
        for day in day_names:
            yield day

gen = days()

for _ in range(100000000000000000000):
    print(next(gen))