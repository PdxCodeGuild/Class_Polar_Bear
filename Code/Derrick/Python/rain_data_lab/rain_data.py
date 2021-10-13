from datetime import datetime 


date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')

rain_dict = {}

with open('post_office_rain.txt') as file:
    plain_text = file.read()
    plain_text = plain_text.replace('\n',' ')


        
    

    new_list = plain_text.split(' ')
    
    new_list_obj = filter(lambda x: x != "", new_list)

    new_list = list(new_list_obj)

for i in range(len(new_list)):
    if len(new_list[i]) == 11:
        rain_dict[new_list[i]] = int(new_list[i+1].rstrip())          

# Calculate mean
sum = 0
# for value in rain_dict.values():
#     print(value)


print(rain_dict)
# print(date)