import csv

def species_observed_by(*args): # Count unique species observed by 'person1,person2'
    obs_set = set()

    with open('life_list.csv', 'r') as bird_file: # Turns out to be more convenient to not use dictreader here. Would like to fix in the future
        with open('clements-v2023-October-2023.csv', 'r') as all_bird_file:
            reader_all = list(csv.reader(all_bird_file, delimiter=','))
            reader = list(csv.reader(bird_file, delimiter=','))

            name_index = reader[0].index('Name')
            seen_index = reader[0].index('Seen By')
            category_index_all = reader_all[0].index('category')
            name_index_all = reader_all[0].index('English name')

            for row in reader:
                for row2 in reader_all:
                    if args == None and row[name_index] == row2[name_index_all] and row2[category_index_all] == 'species':
                        obs_set.add(row[name_index])
                    elif row[seen_index] in args and row[name_index] == row2[name_index_all] and row2[category_index_all] == 'species':
                        obs_set.add(row[name_index])
    return obs_set
