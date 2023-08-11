def average_temperature():
    days = int(input("How many day's temperature ? "))
    all_temp_list = []
    for i in range(days):
        value = int(input(f"Day {i+1}'s high temp:"))
        all_temp_list.append(value)    
    average = round(sum(all_temp_list)/len(all_temp_list), 2)
    print(f"Average {average}")
    above_average_temp = [i for i in all_temp_list if i > average]
    print(f"{len(above_average_temp)} day's above average")
    
average_temperature()
