def total_salary(path):
    try:
        with open(path, 'r') as file:
            total = 0
            counter = 0
            for line in file:
                parts = line.strip().split(',')
                salary = int(parts[1])
                total += salary
                counter += 1
            average = total / counter
            return total, average
    except FileNotFoundError:
        print("Error")

total, average = total_salary('e:\\python\\Homework\\goit-algo-hw-04\\1ex\\salaries.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")