# CREATING REALISTIC DATA TO TEST IN CLUSTERING ALGORITHM 

# interesting psychology to consider

### PRIMARY CHARACTERISTICS 

# socialness and intellect perhaps are more inversely related than one would expect
# being artistic is independent generally of all other factors
# being adventurous is directly related to ambition and inverse to intellect

### SECONDARY CHARACTERISTICS

# high intellect = higher chance of liking books and higher chacne of liking tech
# getting music is like 70% chance in general

from random import randint

# in order of 1, 2, 3, 4
intellect_weight = [0.1, 0.4, 0.3, 0.2]
artistic_weight = [0.1, 0.5, 0.3, 0.1]

# if high intellect (3 or 4)
social_weight_high = [0.3, 0.4, 0.2, 0.1]
adventure_weight_high = [0.3, 0.4, 0.2, 0.1]
ambition_weight_high = [0.1, 0.3, 0.4, 0.2]

# if lower intellect (1 or 2)
social_weight_low = [0.1, 0.2, 0.4, 0.3]
adventure_weight_low = [0.1, 0.2, 0.4, 0.3]
ambition_weight_low = [0.1, 0.4, 0.3, 0.2]

# categories
categories = ['books', 'crafting', 'fashion', 'gaming', 'movies', 'music', 'partying', 'pets', 'politics', 'religion', 'sports', 'tech']

number_to_name = {}
for ind in range(len(categories)):
    number_to_name[ind] = categories[ind]

# order of selection to fill out the 5 options
order_weight = [0.1, 0.08, 0.05, 0.05, 0.1, 0.15, 0.12, 0.11, 0.08, 0.15, 0.1, 0.12]

# create two dictionaries 

# weighting in order of 0, 1 (no, yes)
music_weight = [0.3, 0.7]
movie_weight = [0.4, 0.6]
religion_weight = [0.8, 0.2]

# if high intellect
book_weight = [0.3, 0.7]
tech_weight = [0.4, 0.6]
# if low intellect
book_weight_low = [0.7, 0.3]
tech_weight_low = [0.65, 0.35]

# if high social
partying_weight = [0.3, 0.7]
# if low social
partying_weight_low = [0.8, 0.2]

# if high artistic
crafting_weight = [0.3, 0.7]
fashion_weight = [0.3, 0.7]
# if low artistic
crafting_weight_low = [0.65, 0.35]
fashion_weight_low = [0.7, 0.3]

# if high adventurous
sports_weight = [0.4, 0.6]

def select_random_primary(weights):
    w = [int(100*num) for num in weights]
    w_sum = sum(w)
    rand_weight = randint(0, w_sum-1)
    total = 0
    for index in range(len(w)):
        total += w[index]
        if rand_weight < total:
            return index + 1 # gives the score for this category

def select_random_secondary(weights_sec, secondary_list, dict_weights):
    ind = select_random_primary(weights_sec) - 1
    if secondary_list[ind] == 1:
        return
    else:
        category_name = number_to_name[ind]
        bin_val = select_random_primary(dict_weights[category_name]) - 1
        secondary_list[ind] = bin_val
        return 

def select_set(prim):
    # given the primary characteristics, which set of secondary chars should the program use 
    secondary_dict = {}
    secondary_dict['music'] = music_weight
    secondary_dict['movies'] = movie_weight
    secondary_dict['religion'] = religion_weight
    if prim[0] == 3 or prim[0] == 4:
        secondary_dict['books'] = book_weight
        secondary_dict['tech'] = tech_weight
    else:
        secondary_dict['books'] = book_weight_low
        secondary_dict['tech'] = tech_weight_low
    if prim[2] == 3 or prim[2] == 4:
        secondary_dict['partying'] = partying_weight
    else:
        secondary_dict['partying'] = partying_weight_low
    if prim[1] == 3 or prim[1] == 4:
        secondary_dict['crafting'] = crafting_weight
        secondary_dict['fashion'] = fashion_weight
    else:
        secondary_dict['crafting'] = crafting_weight_low
        secondary_dict['fashion'] = fashion_weight_low
    if prim[3] == 3 or prim[3] == 4:
        secondary_dict['sports'] = sports_weight
    for cat in categories:
        if cat not in secondary_dict:
            secondary_dict[cat] = [0.5, 0.5]
    return secondary_dict

def create_data():
    person = []
    
    ''' ---------------------
     primary characteristics 
    --------------------- '''

    person.append(select_random_primary(intellect_weight))
    person.append(select_random_primary(artistic_weight))

    if person[0] == 3 or person[0] == 4:
        person.append(select_random_primary(social_weight_high))
        person.append(select_random_primary(adventure_weight_high))
        person.append(select_random_primary(ambition_weight_high))
    else:
        person.append(select_random_primary(social_weight_low))
        person.append(select_random_primary(adventure_weight_low))
        person.append(select_random_primary(ambition_weight_low))

    ''' -----------------------
     secondary characteristics 
    ----------------------- '''
    
    secondary = []
    for i in range(12):
        secondary.append(0)

    weight_dict = select_set(person)

    while sum(secondary) < 5:
        select_random_secondary(order_weight, secondary, weight_dict)
        
    return person + secondary


print("intellect, art, social, adventure, ambition")
print(['books', 'crafting', 'fashion', 'gaming', 'movies', 'music', 'partying', 'pets', 'politics', 'religion', 'sports', 'tech'])
for i in range(100):
    print(create_data())


