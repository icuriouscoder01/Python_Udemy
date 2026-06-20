hours = [7,9,8,3,6,3,9]
wage_per_hr = 45

total_hours = sum(hours)
print(f"Total Hours Worked : {total_hours}")

if total_hours > 40:
    overtime = total_hours - 40
    total_wages = overtime * 45 * 2 + total_hours * 45
    print(f"overtime : {overtime}")
else:
    total_wages = total_hours * 45

print(f"Total Wages : {total_wages}")

