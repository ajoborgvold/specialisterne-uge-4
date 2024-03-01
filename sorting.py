from names_data import names

#===========================#
# * Sort names by their length:
# 1. Length of the whole name
# 2. Length of first name
# 3. Length of last name
# 4. Reversed order
#===========================#
total_length = sorted(names, key=len)

def get_first_name_length(name):
    return len(name.split()[0])

def get_last_name_length(name):
    return len(name.split()[-1])

first_name_length = sorted(names, key=get_first_name_length)
last_name_length = sorted(names, key=get_last_name_length)

# * Print the names list sorted by length of whole, first and last name
# print("Sorted by length of the whole name:", total_length)
# print("----------------------------")
# print("Sorted by length of first name:", first_name_length)
# print("----------------------------")
# print("Sorted by length of last name:", last_name_length)

# * Print the names list sorted by length, but reversed
# print("Reversed, sorted by length of the whole name:", list(reversed(total_length)))
# print("----------------------------")
# print("Reversed, sorted by length of first name:", list(reversed(first_name_length)))
# print("----------------------------")
# print("Reversed, sorted by length of last name:", list(reversed(last_name_length)))


#==========================#
# * Sort names alphabetically
# 1. Sort by first name
# 2. Sort by last name
# 3. Reversed order
#==========================#
def get_last_name(full_name):
    return full_name.split()[-1]

first_name_alphabet = sorted(names, key=str)
last_name_alphabet = sorted(names, key=get_last_name)

# * Print the names list sorted alphabetically by first and last name
# print("Sorted alphabetically by first name:", first_name_alphabet)
# print("----------------------------")
# print("Sorted alphabetically by last name:", last_name_alphabet)

# * Print the alphabetically sorted names list, by first and last name, but reversed
# print("Reversed, sorted alphabetically by first name:", list(reversed(first_name_alphabet)))
# print("----------------------------")
# print("Reversed, sorted alphabetically by last name:", list(reversed(last_name_alphabet)))


#==========================================#
# * Count letters
# 1. Print dict sorted alphabetically
# 2. Print dict sorted by descending value
#==========================================#
letter_count = {}
for name in names:
    name_lower = name.lower()
    for letter in name_lower:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1

def sort_dict_alphabetically(count):
    return dict(sorted(count.items()))

def sort_by_value_descending(item):
    return (-item[1], item[0])

def sort_by_value_ascending(item):
    return (item[1], item[0])

def sort_dict_by_count_descending(count):
    return dict(sorted(count.items(), key=sort_by_value_descending))

def sort_dict_by_count_ascending(count):
    return dict(sorted(count.items(), key=sort_by_value_ascending))

# * Print the sorted letter count dictionary
# print(sort_dict_alphabetically(letter_count))
# print("----------------------------")
# print(sort_dict_by_count_descending(letter_count))
# print("----------------------------")
# print(sort_dict_by_count_ascending(letter_count))


#====================================================================#
# * List of dictionaries with name lengths and their frequencies
# 1. Remove whitespace from names to avoid counting space between first and last name as a character
# 2. Sort the names by length
# 3. Create the dictionaries with length and frequency
# 4. Calculate average name length
# 5. Calculate median name length
#====================================================================#

def remove_whitespace(names):
    return [name.replace(" ", "") for name in names]

def create_names_length_dict(names):
    return {name: len(name) for name in names}

names_no_whitespace = remove_whitespace(names)
sorted_names = sorted(names_no_whitespace, key=len)
names_length_dict = create_names_length_dict(sorted_names)

def create_length_count_list(names_length_dict):
    """Create a list of dictionaries that has two key value-pairs:
    length: the name length,
    count: frequency in names_length_dict of the given name length
    """
    length_count_list = []
    for length in names_length_dict.values():
        found = False
        for item in length_count_list:
            if item["length"] == length:
                item["count"] += 1
                found = True
                break
        if not found:
            length_count_list.append({"length": length, "count": 1})
    return length_count_list

def get_average_length(names):
    """Calculate average name length and limit the result to 3 decimal places for better readability"""
    total_length = sum(len(name) for name in names)
    average_length = total_length / len(names)
    return round(average_length, 3)

def get_median_length(sorted_names, names_length_dict):
    """Calculate the median name length for name lists of odd/even length.
    1. Get the length of the sorted_names list
    2. Get the index of the middle element in sorted_names
    3. Get the value, i.e. the length, corresponding with this middle index in the names_length_dict
    """
    
    n = len(sorted_names)
    
    if n % 2 == 0: # The length of the list is an even number
        median_length = (names_length_dict[sorted_names[n // 2]] + names_length_dict[sorted_names[n // 2 -1]]) / 2
        # The median length will always be a whole number but is display as a float. The int() function solves this problem.
        return int(median_length)
    else: # The length of the list is an odd number
        return names_length_dict[sorted_names[n // 2]]
    
    
# * Print names length dictionary, average and median length
# print(create_length_count_list(names_length_dict))
# print("----------------------------")
# print("Average name length:", get_average_length(names_no_whitespace))
# print("----------------------------")
# print("Median name length:", get_median_length(sorted_names, names_length_dict))