import chars

## Questions ##
upper_count = input(f'How many {chars.options[0]} do you want?')
lower_count = input(f'How many {chars.options[1]} do you want?')
symbol_count = input(f'How many {chars.options[2]} do you want?')
num_count = input(f'How many {chars.options[3]} do you want?')

## functions ##
chars.allChars(upper_count,lower_count,symbol_count,num_count)