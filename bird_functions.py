import csv

class Bird:

    def __init__(self, name, clements_file, life_list):
        self.clements_file = open(clements_file, 'r')
        self.life_list = open(life_list, 'r+')
        self.name = name
        self.date = None
        self.seen_by = None
        self.location = None
        self.comment = None
        self.fieldnames = ['Name', 'Date', 'Location', 'Seen By', 'Comment']

    def close(self):
        self.clements_file.close()
        self.life_list.close()
    def bird_exists(self):  # Checks if the bird name exists in the clements list
        if self.name == '':
            print('Bird name cannot be empty.')
            quit()
        else:
            clements_reader = csv.DictReader(self.clements_file)
            for row in clements_reader:
                if self.name == row['English name']:
                    return row['category']
            return False

    def read_life_list(self):
        life_reader = csv.DictReader(self.life_list)
        persons = []
        for row in life_reader:
            if self.name == row['Name']:
                persons.append(row['Seen By'])
        return persons

    def add_bird(self):
        writer = csv.DictWriter(self.life_list, fieldnames=self.fieldnames)
        writer.writerow({'Name': self.name, 'Date': self.date, 'Location': self.location, 'Seen By': self.seen_by, 'Comment': self.comment})
        print(f'{self.name} added successfully.')


