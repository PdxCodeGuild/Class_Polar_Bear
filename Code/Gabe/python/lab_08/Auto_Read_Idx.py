ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

book = 'the_power_of_music.txt'

with open('the_power_of_music.txt') as file:
  chars = file.read()
chars = ' '.join(filter(None,chars.split(' ')))
chars = ' '.join(filter(None,chars.split('\n')))
chars = ' '.join(filter(None,chars.split(' ')))
chars = ''.join(filter(None,chars.split(' ')))
num_of_characters = len(chars)

with open('the_power_of_music.txt') as file:
  words = file.read()
words = ' '.join(filter(None,words.split(' ')))
words = ' '.join(filter(None,words.split('\n')))
words = ' '.join(filter(None,words.split(' ')))
words = words.split(' ')
num_of_words = len(words)

with open('the_power_of_music.txt') as file:
  sentences = file.read()
sentences = ' '.join(filter(None,sentences.split(' ')))
sentences = ' '.join(filter(None,sentences.split('\n')))
sentences = ' '.join(filter(None,sentences.split(' ')))
sentences = sentences.split('.')
num_of_sentences = len(sentences) - 1


ari = (4.71 * (num_of_characters / num_of_words)) + (0.5 * (num_of_words / num_of_sentences)) - 21.43


print(
f'''
{'-' * 56}
The ARI for {book} is {round(ari)}
This corresponds to a(n) {ari_scale[round(ari)]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[round(ari)]['ages']} years old.
{'-' * 56}
'''
)
