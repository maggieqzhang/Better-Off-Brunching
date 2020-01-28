# CREATING REALISTIC DATA TO TEST IN CLUSTERING ALGORITHM 

''' 
create random data for primary and secondary attributes
generally, a "high" score in any category is 3 or 4, while a low score is 1 or 2
'''

from random import randint
import random as r
import numpy as np
import csv

# the probability of any given person of achieving each intelletualism score
# in order of 1, 2, 3, 4
intellect_weight = [0.1, 0.4, 0.3, 0.2]

# artistic weight depending on gender
artistic_weight_M = [0.1, 0.5, 0.3, 0.1]
artistic_weight_F = [0.1, 0.3, 0.4, 0.2]

# if high intellectualism (3 or 4)
social_weight_high = [0.3, 0.4, 0.2, 0.1]
adventure_weight_high = [0.3, 0.4, 0.2, 0.1]
ambition_weight_high = [0.1, 0.3, 0.4, 0.2]

# if lower intellectualism (1 or 2)
social_weight_low = [0.1, 0.2, 0.4, 0.3]
adventure_weight_low = [0.1, 0.2, 0.4, 0.3]
ambition_weight_low = [0.1, 0.4, 0.3, 0.2]

# demographics and secondary categories 

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

#if directed to any of the subcategories, choose at random 1-3 items
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

# weighting in selection probability in order of 0, 1 (no, yes)
music_weight = [0.3, 0.7]
movie_weight = [0.4, 0.6]
religion_weight = [0.8, 0.2]

# if high intellectual, more likely to like books and tech
book_weight = [0.3, 0.7]
tech_weight = [0.4, 0.6]
# if low intellectualism, less likely to enjoy books and tech
book_weight_low = [0.7, 0.3]
tech_weight_low = [0.65, 0.35]

# if high social, more likely to party
partying_weight = [0.3, 0.7]
# if low social, less likely to party
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
    """ 
    Randomly selects a score for a primary attribute given weighting probabilities
  
    Parameters: 
    weights (list): probability of getting a certain score in order of [1,2,3,4]
  
    Returns: 
    int: primary attribute score  
    """
    # general alg for random weighted selection is choosing a random number and seeing where it falls in the range
    w = [int(100*num) for num in weights] 
    w_sum = sum(w)
    rand_weight = randint(0, w_sum - 1)
    total = 0
    for index in range(len(w)):
        total += w[index]
        if rand_weight < total:
            return index + 1 # gives the score for category

def select_random_secondary(weights_sec, secondary_list, dict_weights):
    """ 
    Randomly selects a secondary attribute and then randomly decides if it is a characteristic of person
  
    Parameters: 
    weights_sec (dictionary): probability of selecting any given secondary char initially
    secondary_list (list): list with values of 0 or 1 representing secondary attributes 
    dict_weights (dictionary): a dictionary containing all secondary attribute and the probability that they turn up 0 or 1 
  
    Returns: 
    No returns. Directly modifies secondary_list with updated values 
    """
    sec_cat, sec_weight = zip(*weights_sec.items()) #unzips dictionary to give both var names and rel weightings
    ind = select_random_primary(sec_weight) - 1
    if secondary_list[ind] == 1: # secondary char was already chosen before
        return
    else: # category never chosen before
        category_name = sec_cat[ind] 
        if category_name == "watching sports": # category with subgenres 
            print("sport!")
            secondary_list[ind] = 1
            sub_secondary(secondary_list, 18, sports_sub) # first subgenre after 18 secondary char
        elif category_name == "movies": # category with subgenres 
            print("movie")
            secondary_list[ind] = 1
            sub_secondary(secondary_list, 25, movie_sub) # secondary subgenre afer sec and sports
        elif category_name == "music": # category with subgenres 
            print("music")
            secondary_list[ind] = 1
            sub_secondary(secondary_list, 34, music_sub) # third subgenre after sec, sports, and movies 
        else:
            bin_val = select_random_primary(dict_weights[category_name]) - 1 # just a normal category
            secondary_list[ind] = bin_val
        return 
    
def sub_secondary(sec_list, addition, sub_dict):
    """ 
    Given that an expanded secondary char was chosen, it deterines how many and which sub genres are chosen
  
    Parameters: 
    sec_list (list): list with values of 0 or 1 representing secondary attributes 
    addition (int): the amount added to the index. value shift
    sub_dict (dictionary): the dictionary of values and prob weights for genres
  
    Returns: 
    int: primary attribute score  
    """
    sub_cat, sub_weight = zip(*sub_dict.items())
    num_cats = randint(1,3)
    for i in range(num_cats):
        sub_ind = select_random_primary(sub_weight) - 1 + addition # accounts for index shift for subgenres
        sec_list[sub_ind] = 1

def select_set(prim):
    """ 
    Given a set of primary characteristics, selects which secondary characteristic weightings the program should use
  
    Parameters: 
    prim (dictionary): dictionary of primary attributes and associated values 
  
    Returns: 
    secondary_dict (dictionary): a dictionary with all secondary attributes and associated weightings 
    """
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
        if cat not in secondary_dict: # other secondary interests not dependent on gender/primary
            secondary_dict[cat] = [0.5, 0.5]
    return secondary_dict

def create_data(numMulti):
    """ 
    Creates a person with numMulti secondary char variations.
    
    Using the same set of randomly chosen primary characteristics, numMulti amount of people with differing secondary characteristics is created
  
    Parameters: 
    numMulti (int): number of people to create with the same generated set of primary characteristics
  
    Returns: 
    people (list): a list of numMulti number of lists each representing a "different" person
    """
    person = {}
    age = 0
    while age < 21 or age > 35: # person between 31 and 35 with normal distribution closer to young side
        age = round(np.random.normal(26, 4))
    
    ''' ---------------------
     primary characteristics 
    --------------------- '''
    # generates the random primary characteristics for this person 
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
    # creates a list of numMulti number of lists representing each person
    secondary = [[0 for i in range(42)] for j in range(numMulti)]
    
    weight_dict = select_set(person) # the weighted dictionary of secondary values 

    num_secondaries = [r.choices([8,9,10,11,12,13,14,15])[0] for i in range(numMulti)] # randomly choose between 8-15 secondary chars

    for i in range(numMulti):
        num_secondary = num_secondaries[i]
        while sum(secondary[i]) < num_secondary: #see if there is enough secondary char selected
            select_random_secondary(categories, secondary[i], weight_dict)
    
    person_cats, person_scores = zip(*person.items()) #unzips original person dictionary to be able to turn into lists
    person_scores = list(person_scores)
    people = []
    for sec in secondary:
        people.append((person_scores + sec))
    return people

# writing data to CSV file
with open("test_data.csv", mode = "w") as test_data:
    test_writer = csv.writer(test_data, delimiter = ",",quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    for i in range(100): # creates 100 randomly generated people 
        person_data = create_data(8)
        for val in person_data:
            test_writer.writerow(val)
