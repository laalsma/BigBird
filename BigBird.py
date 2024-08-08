from bird_functions import Bird
import datetime

print('Welcome to BigBird!')

bird_name = input('What\'s the name of the bird you want to add? ')
b1 = Bird(bird_name, 'clements-v2023-October-2023.csv', 'life_list.csv')
bird_type = b1.bird_exists()

if not bird_type:
    print(f'{bird_name} does not exist. Did you spell it correctly?')
    b1.close()
    quit()

if bird_type != 'species':
    cont = input(f'{bird_name} is a {bird_type}. Make sure to also add relevant species. Type any key to continue or Q to quit: ')
    if cont == 'Q':
        b1.close()
        quit()

prev_obs = b1.read_life_list()

if len(prev_obs) > 0:
    print(f'The {bird_name} was already seen by ' + ' and '.join([str(x) for x in prev_obs]) + '.')
    new_obs = input('Do you want to add a new observation (Y/N)? ')
    if new_obs == 'N':
        b1.close()
        quit()

bird_seen_by_str = input(f'Who saw the {bird_name}? Comma separate multiple names as Person1,Person2: ')
bird_seen_by = bird_seen_by_str.split(',')

same_obs = None

if len(bird_seen_by) > 1:
    same_obs = input(f'Did ' + ' and '.join([str(x) for x in bird_seen_by]) + f' see the {bird_name} at the same date/location? Answer Y/N: ')

    if same_obs not in ['Y','N']:
        print('Not a Y/N answer.')
        b1.close()
        quit()

for person in bird_seen_by:
    bird_date_str = input(f'What date did {person} see the {bird_name}? Use format YYYY-MM-DD: ')
    bird_date = datetime.datetime.strptime(bird_date_str, "%Y-%m-%d").date()

    bird_location_str = input(f'Where did {person} see the {bird_name}? Use format Country,State,Location: ')
    bird_location = bird_location_str.split(',')

    b1.date = bird_date
    b1.location = bird_location
    b1.seen_by = person

    if same_obs == 'N':
        b1.add_bird()
    else:
        for item in bird_seen_by:
            b1.seen_by = item
            b1.add_bird()
        b1.close()
        quit()
b1.close()