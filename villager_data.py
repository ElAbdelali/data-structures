"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unique_species = set()

    data = open(filename)
    for line in data:
        species = line.rstrip().split("|")[1]
        unique_species.add(species)

    return unique_species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    
    file = open(filename)
    
    for line in file:
        if search_string == "All":
            villagers.append(line.strip.split("|")[0])
        elif search_string in line:
            villagers.append(line.strip.split("|")[0])
        

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    
    Fitness = []
    Nature = []
    Education = []
    Music = []
    Fashion = []
    Play = []
    
    
    
    for line in open(filename):
        villager = line.strip().split("|")
        name_of_villager = villager[0]
        hobby_of_villager = villager[3]
        
        if hobby_of_villager == "Fitness":
            Fitness.append(name_of_villager)
        elif hobby_of_villager == "Nature":
            Nature.append(name_of_villager)
        elif hobby_of_villager == "Education":
            Education.append(name_of_villager)
        elif hobby_of_villager == "Music":
            Music.append(name_of_villager)
        elif hobby_of_villager == "Fashion":
            Fashion.append(name_of_villager)
        elif hobby_of_villager == "Play":
            Play.append(name_of_villager)
    
    return [sorted(Fitness), sorted(Nature), sorted(Education), sorted(Music), sorted(Fashion), sorted(Play)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    
    
    
    for line in open(filename):
        villager = line.strip().split("|")
        name, species, personality, hobby, motto = villager
        all_data.append((name , species, personality, hobby, motto)) #double () created a tuple
        
        

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    for line in open(filename):
        villager = line.strip().split('|')
        villagers_name = villager[0]
        villagers_motto = villager[4]
        
        if villagers_name == villager_name:
            return villagers_motto
        else:
            return None
    

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    likeminded = set()

    target_personality = None
    for villager_data in all_data(filename):
        name, _, personality = villager_data[:3]

        if name == villager_name:
            target_personality = personality
            break

    if target_personality:
        for villager_data in all_data(filename):
            name, _, personality = villager_data[:3]
            if personality == target_personality:
                likeminded.add(name)

    return likeminded
