greeting = 'Hello World, don\'t be a jerk' # use escape character if using same quotes as apostrophy
message = "\nCoding is fun, y'all \nkeep on coding!\n" # use double quotes to use apostrophy

email = '\nDear recruiter,\n\n\tI\'d like to join your \"organization\".\n\nBest,\nGabe\n'

raw_string = r"The string prints anything in it \n \t includin those new line and tab. Can use with a file path for example."

message_2 = f'''Hello
this is a {2 + 1}
multi line string'''

file_path = r'User/gabeC/desktop/pdx_code/file.py'

file_path_sub_set = file_path[4:] # sub string from index 4 to end of string / [:4] gets from 0 to 3

file_path_sub_set2 = file_path[::-1] # Gives me string in reverse


greeting2 = 'Hello World'
start = greeting2.find('W') # Find gives the index of given string
sub_set = greeting2[start:]

user_string = 'Hello WOrlD'

# print(user_string.lower())
# print(user_string.upper())
# print(user_string.title())

# print(sub_set)

# print(user_string.startswith('e'))
# print(user_string.startswith('H'))
# print(user_string.endswith('a'))
# print(user_string.endswith('D'))

print('ello' in user_string)