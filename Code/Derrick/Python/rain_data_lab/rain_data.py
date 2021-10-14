### 1 = .01 inches of rain ###

rain_dict = {}
rain_chart = 'post_office_rain.txt'
with open(rain_chart) as file:
    plain_text = file.read()
    plain_text = plain_text.replace('\n',' ')

    new_list = plain_text.split()

for i in range(len(new_list)):

    if len(new_list[i]) == 11:
        try:
            rain_dict[new_list[i]] = int(new_list[i+1])
        except ValueError:
            continue 
                
# Calculate mean
sum = 0
for value in rain_dict.values():
    sum += value
    mean = round(sum / len(rain_dict.values()),2)

earliest_date = list(rain_dict.keys())[-1]
location = ''
for i in rain_chart:
    location += i
    if i == '.':
        break

print(f'Starting from {earliest_date} the daily average rainfall for {location} is {round(mean * .01,2)} inches')
