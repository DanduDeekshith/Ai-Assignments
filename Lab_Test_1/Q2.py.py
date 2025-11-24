from statistics import mean

students = {}

count = int(input("How many students? ").strip())
for _ in range(count):
    name = input("Student name: ").strip()
    mark = float(input(f"Mark for {name}: ").strip())
    students[name] = mark

avg = mean(students.values())
above_mean = [name for name, mark in students.items() if mark > avg]

print(f"\nMean mark: {avg:.2f}")
print("Students above mean:", ", ".join(above_mean) if above_mean else "None")