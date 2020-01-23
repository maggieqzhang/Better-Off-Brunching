# CREATING REALISTIC DATA TO TEST IN CLUSTERING ALGORITHM 

# interesting psychology to consider

### PRIMARY CHARACTERISTICS 

# socialness and intellect perhaps are more inversely related than one would expect
# being artistic is independent generally of all other factors
# being adventurous is directly related to ambition and inverse to intellect

### SECONDARY CHARACTERISTICS'

# high intellect = higher chance of liking books and higher chacne of liking tech
# getting music is like 70% chance in general

from random import randint
import random as r
import numpy as np

# fix the random output
##r.seed(a=4)

# in order of 1, 2, 3, 4
intellect_weight = [0.1, 0.4, 0.3, 0.2]

# artistic depending on gender
artistic_weight_M = [0.1, 0.5, 0.3, 0.1]
artistic_weight_F = [0.1, 0.3, 0.4, 0.2]

# if high intellect (3 or 4)
social_weight_high = [0.3, 0.4, 0.2, 0.1]
adventure_weight_high = [0.3, 0.4, 0.2, 0.1]
ambition_weight_high = [0.1, 0.3, 0.4, 0.2]

# if lower intellect (1 or 2)
social_weight_low = [0.1, 0.2, 0.4, 0.3]
adventure_weight_low = [0.1, 0.2, 0.4, 0.3]
ambition_weight_low = [0.1, 0.4, 0.3, 0.2]

# categories
#categories = ['books', 'crafting', 'fashion', 'gaming', 'movies', 'music', 'partying', 'pets', 'politics', 'religion', 'sports', 'tech']
#order_weight = [0.1,    0.08,       0.05,      0.05,      0.1,       0.15,   0.12,      0.11,     0.08,      0.15,       0.1,      0.08]

gender = ['M', 'F']

categories = {'crafting':0.08,
              'fashion':0.05,
              'fitness/health':0.12,
              'cooking/baking':0.1,
              'dancing':0.09,
              'music':0.15,
              'watching sports':0.1,
              'playing sports': 0.11,
              'partying': 0.12,
              'board games':0.04,
              'politics':0.08,
              'tech':0.08,
              'gaming':0.05,
              'pets':0.11,
              'food':0.14,
              'religion':0.07,
              'photography':0.05,
              'movies':0.12}

#if directed to any of the subcategories, choose at random 1-3 items assume each has 50% chance of liking the sport chosen  
sports_sub = {'basketball':0.2,
              'baseball':0.25,
              'football':0.4,
              'soccer':0.16,
              'tennis':0.12,
              'golf':0.1,
              'hockey':0.1}

movie_sub = {'action':0.25,
             'drama':0.15,
             'adventure':0.2,
             'horror':0.1,
             'thriller':0.2,
             'comedy':0.3,
             'romance':0.2,
             'scifi':0.25,
             'musicals':0.15}

music_sub = {'pop':0.4,
             'rap':0.3,
             'country':0.1,
             'EDM':0.1,
             'classical':0.1,
             'kpop':0.05,
             'rock':0.1,
             'jazz':0.1}

'''
number_to_name = {}
for ind in range(len(categories)):
    number_to_name[ind] = categories[ind]
'''
# order of selection to fill out the thing 
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

# if female
female_sports_watch = [0.6, 0.4]
female_dancing_weight = [0.4, 0.6]
female_cooking_weight = [0.3, 0.7]
female_gaming_weight = [0.7, 0.3]

# if male
male_sports_watch = [0.3, 0.7]
male_dancing_weight = [0.6, 0.4]
male_cooking_weight = [0.6, 0.4]
male_gaming_weight = [0.3, 0.7]

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
    #ind = select_random_primary(weights_sec) - 1 # do it manually using dictionary style aiyahhhh
    sec_cat, sec_weight = zip(*weights_sec.items())
    ind = select_random_primary(sec_weight) - 1
    if secondary_list[ind] == 1:
        return
    else:
        category_name = sec_cat[ind]
        if category_name == "watching sports":
            print("sport!")
            secondary_list[ind] = 1
            sub_secondary(secondary_list, 18, sports_sub)
        elif category_name == "movies":
            print("movie")
            secondary_list[ind] = 1
            sub_secondary(secondary_list, 25, movie_sub)
        elif category_name == "music":
            print("music")
            secondary_list[ind] = 1
            sub_secondary(secondary_list, 34, music_sub)
        else:
            bin_val = select_random_primary(dict_weights[category_name]) - 1
            secondary_list[ind] = bin_val
        return 
    
def sub_secondary(sec_list, addition, sub_dict):
    sub_cat, sub_weight = zip(*sub_dict.items())
    num_cats = randint(1,3)
    for i in range(num_cats):
        sub_ind = select_random_primary(sub_weight) - 1 + addition
        sec_list[sub_ind] = 1

def select_set(prim):
    # given the primary characteristics, which set of secondary chars should the program use 
    secondary_dict = {}
    g = prim['gender']
    
    secondary_dict['music'] = music_weight
    secondary_dict['movies'] = movie_weight
    secondary_dict['religion'] = religion_weight
    if prim['intellect'] == 3 or prim['intellect'] == 4:
        secondary_dict['books'] = book_weight
        secondary_dict['tech'] = tech_weight
    else:
        secondary_dict['books'] = book_weight_low
        secondary_dict['tech'] = tech_weight_low
    if prim['social'] == 3 or prim['social'] == 4:
        secondary_dict['partying'] = partying_weight
    else:
        secondary_dict['partying'] = partying_weight_low
    if prim['artistic'] == 3 or prim['artistic'] == 4:
        secondary_dict['crafting'] = crafting_weight
        secondary_dict['fashion'] = fashion_weight
    else:
        secondary_dict['crafting'] = crafting_weight_low
        secondary_dict['fashion'] = fashion_weight_low
    if prim['adventure'] == 3 or prim['adventure'] == 4:
        secondary_dict['playing sports'] = sports_weight
    if g == "F":
        secondary_dict['watching sports'] = female_sports_watch
        secondary_dict['dancing'] = female_dancing_weight
        secondary_dict['cooking/baking'] = female_cooking_weight
        secondary_dict['gaming'] = female_gaming_weight
    else:
        secondary_dict['watching sports'] = male_sports_watch
        secondary_dict['dancing'] = male_dancing_weight
        secondary_dict['cooking/baking'] = male_cooking_weight
        secondary_dict['gaming'] = male_gaming_weight
        
    for cat in categories:
        if cat not in secondary_dict:
            secondary_dict[cat] = [0.5, 0.5]
    return secondary_dict

def create_data():
    numMulti = 8
    person = {}
    
    age = 0
    while age < 21 or age > 35:
        age = round(np.random.normal(26, 4))
    
    ''' ---------------------
     primary characteristics 
    --------------------- '''
    person['gender'] = gender[randint(0,1)]
    person['age'] = age
    person['intellect'] = select_random_primary(intellect_weight)
    if person['intellect'] == 3 or person['intellect'] == 4:
        person['social'] = select_random_primary(social_weight_high)
        person['adventure'] = select_random_primary(adventure_weight_high)
        person['ambition'] = select_random_primary(ambition_weight_high)
    else:
        person['social'] = select_random_primary(social_weight_low)
        person['adventure'] = select_random_primary(adventure_weight_low)
        person['ambition'] = select_random_primary(ambition_weight_low)
    if person['gender'] == "M":
        person['artistic'] = select_random_primary(artistic_weight_M)
    else:
        person['artistic'] = select_random_primary(artistic_weight_F)

    ''' -----------------------
     secondary characteristics 
    ----------------------- '''
    
    secondary = [[0 for i in range(42)] for j in range(numMulti)]
    
    weight_dict = select_set(person)

    num_secondaries = [r.choices([8,9,10,11,12,13,14,15])[0] for i in range(numMulti)]

    for i in range(numMulti):
        num_secondary = num_secondaries[i]
        while sum(secondary[i]) < num_secondary:
            select_random_secondary(categories, secondary[i], weight_dict)
    
    person_cats, person_scores = zip(*person.items())
    person_scores = list(person_scores)
    for sec in secondary:
        print(person_scores + sec)
    #return person_scores + [d for sec in secondary for d in sec]

import csv

'''
with open('testData.csv', mode='w') as employee_file:
    testDataWriter = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ## xd i didn't finish this part 
    for i in range(100):
        testDataWriter.writerow(create_data())

'''

#print(create_data())
