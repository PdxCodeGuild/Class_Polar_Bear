# Create Contact ===============================================================
# Write a function that returns a dictionary representing a contact given their name and age.

def create_contact(name, age):
    person = {}
    person['name'] = name 
    person['age'] = age 
    return person

# print(create_contact('Bob', 67))  # {'name': 'Bob', 'age': 67}
# print(create_contact('Linda', 34)) # {'name': 'Linda', 'age': 34}

# Has Key ======================================================================
# Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.

def has_key(d, key):
    if d.get(key):
        return True 
    else:
        return False
# print(has_key({'a': 1, 'b': 2}, 'a')) # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False

# Is Empty =====================================================================
# Write a function that returns `True` if the given dictionary is empty, `False` otherwise.

def is_empty(d):
    if d == {}:
        return True 
    else:
        return False
# print(is_empty({})) # True
# print(is_empty({'a': 1, 'b': 2})) # False

# Find Key =====================================================================
# Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return `None`.

def find_key(d, value):
    keys = list(d.keys())
    values = list(d.values())
     
    try:
        value = values.index(value)
    except ValueError:
        return None
    
    key = keys[value]    

    return key
 

# print(find_key({'a': 1, 'b': 2}, 1)) # a
# print(find_key({'a': 1, 'b': 2}, 3)) # None

# Reverse Dict =================================================================
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

def reverse_dict(d):
    new = ()
    items = list(d.items())
    
    for item in items:
        new += item[::-1]
    return new

# print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}

# Merge ========================================================================
# Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.

def merge(list1, list2):
    new = {}
    
    if len(list1) == len(list2):
        for i in range(len(list1)):
            new[list1[i]] = list2[i]
    return new

# print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}


# Remove Less Than 10 =========================================================
# Write a function that takes a dictionary and returns a new dictionary without values less than 10.

def remove_less_than_10(d):
    values = list(d.values()) # [5,15,12]
    keys = list(d.keys()) # [a,b,c]
    newList = {}

    for value in values:
        if value > 10:
            key = keys[values.index(value)]
            newList[key] = value
    return newList

# print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12})) # {'b': 15, 'c': 12}

# Average ======================================================================
# Write a function to calculate the average of the lists in a dictionary.

def average_values(d):
    keys = list(d.keys())
    values = list(d.values())
    newList = d.copy()

    for items in values:
        sum = 0
        average = 0
        for value in items:
            sum += value
        
        average = (sum / len(items))
        newList[keys[values.index(items)]] = int(average)

    return newList
        
        


# print(average_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]})) # {'a': 4, 'b': 5, 'c': 3}

# Merge Dictionaries ===========================================================
# Write a function that takes two dictionaries and returns a new dictionary with the values from each added together if they have the same key

def merge_dictionaries(d1, d2):
    ...

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(merge_dictionaries(d1, d2)) # {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Count Votes ==================================================================
# Write a function that takes a list of strings and counts of the number of occurances.

def count_votes(votes):
    ...
# votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
# print(count_votes(votes)) # {'john': 4, 'johnny': 3, 'jackie': 2, 'jamie': 4}

# Problem 6 ====================================================================
# Write a function `cart_total` to calculate the total of a shopping cart given a list of dictionaries representing a cart and a dictionary representing prices.

def cart_total(prices, cart):
    ...
# prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
# cart = [{'item': 'apples', 'quantity': 3}, {'item': 'kiwis', 'quantity': 4}]
# print(cart_total(prices, cart)) # 11.0

