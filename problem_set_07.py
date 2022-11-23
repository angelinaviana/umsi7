import csv
import pprint as pp

# PROBLEM 1
def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Accepts a file path for a .csv file to be read, creates a file object,
    and uses csv.DictReader() to return a list of dictionaries
    that represent the row values from the file.

    Parameters:
        filepath (str): path to csv file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                    or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line)
            #data.append(dict(line))
        return data
        
    


def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    Uses csv.DictWriter() to write a list of dictionaries to a target CSV file as row data.
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# PROBLEM 2
def clean_runtime(movie):
    """
    Accesses the value of the key Runtime (str) and separates the number value and the unit.
    Assigns only the number value back to the key 'Runtime'.

    Parameters:
        movie (dict): dictionary containing key-value pairs representing data for one movie
    Returns:
        dict: dictionary containing "key: value" pairs representing data for one movie
    """
    new_movie = movie
    try:
        new_movie['Runtime'] = int(new_movie['Runtime'].split(' min')[0].replace(',', ''))
    except:
        pass
    return new_movie


def convert_to_int(movie):
    """
    Loop through movie's key:value pairs and implement an error handling to
    check if each value can be converted to an integer.
    If possible, the value is converted and assigned back to its key.

    Parameters:
        movie (dict): dictionary containing key-value pairs representing data for one movie
    Returns:
        dict: dictionary containing key-value pairs representing data for one movie
    """
    new_movie = movie
    for key, value in new_movie.items():
        try:
            new_movie[key] = int(value)
        except:
            new_movie[key] = value
    return new_movie



def clean_row(movie):
    """
    Uses error handling to try to apply both helper functions < clean_runtime() >
    and < convert_to_int() > to the movie dictionary, if there is an error, only apply
    the < convert_to_int() > function.

    Parameter:
        movie (dict): dictionary containing key-value pairs representing data for one movie
    Returns:
        dict: dictionary containing key-value pairs representing data for one movie
    """
    try:
        movie = clean_runtime(movie)
        movie = convert_to_int(movie)
    except:
        movie = convert_to_int(movie)
    return movie

# PROBLEM 3
def filter_movie_by_genre(movies, genre):
    """
    Loops through movies (list) and check if genre (str) is included in the dictionary key: 'Genre'.
    Append the dictionary and all of its data to an empty list and return the final list.
    
    Parameters:
        movies (list): List of dictionaries representing all movies
        genre (str): Movie genre to check for
    Returns:
        list: List with movie dictionaries that include the supplied genre
    """
    genre_list = []

    for movie in movies:
        movie_genres = movie['Genre'].split(', ')
        for mg in movie_genres:
            if mg.lower() == genre.lower():
                genre_list.append(movie)
    return genre_list

# PROBLEM 4
def get_jumpscare_data(jumpscare_data, movie_name):
    """
    Loops through jumpscare data (list) and check to see if the value of `Movie Name` 
    matches the supplied movie_name (str) and returns the values of the keys 'Jump Count' 
    and `Jump Scare Rating` as a tuple

    Parameters:
        jumpscare_data (list): information about information about the movie's jump scares
        movie_name (str): value of the key `Title` from a movie dictionary
    Returns:
        tuple: A tuple with the first value representing a jump count and the second value
            representing a jump scare rating. Both of the tuple's values should be None if the
            movie name does not exist in the jumpscare_data list.
    """
    
    for movie in jumpscare_data:
        if movie['Movie Name'] == movie_name:
            return (movie['Jump Count'], movie['Jump Scare Rating'])
    return (None, None)

# PROBLEM 5
def filter_movies(movies, key_name, lower_limit, upper_limit):
    """
    Loops through a list of dictionaries and checks if the value of the supplied key name (str) is 
    between the integers passed to the lower_limit and upper_limit parameters (inclusively).

    Parameters:
        movies (list):  A list of movie dictionaries
        key_name (str): A dictionary key name
        lower_limit (int): The integer less than the value of the specified key
        upper_limit (int): The integer greater than the value of the specified key
    Returns:
        list: List of movie dictionaries that match thr conditional criteria
    """
    new_movies = []
    for movie in movies:
        if float(movie[key_name]) >= float(lower_limit) and float(movie[key_name]) <= float(upper_limit):
            new_movies.append(movie)
    return new_movies


# PROBLEM 6
def search_movie_plot(movie, search_terms):
    """
    Loops through the search terms and uses a conditional statement to check whether each
    search term appears in the movie's plot. If the search term is in the movie's plot 
    this function returns True, if the search term is not in the movie's plot, 
    this function will return False.

    Parameters:
        movie (dict): A dictionary containing information about one movie.

        search_terms (list):  A list of search terms as strings

    Returns:
        bool: True if term appears in the plot, otherwise False
    """
    
    for term in search_terms:
        if term.lower() in movie['Plot'].lower():
            return True
    return False

# PROBLEM 7
def extract_kv_pair(movie, key_name):
    """
    Takes in a movie dictionary and loops over its key-value pairs.
    Uses a conditional statement to check if the key is the same as the supplied key name parameter.
    Returns a tuple with the movie title and the value of the specified key name.

    Parameters:
        movie (dictionary): A dictionary containing information about one movie.

        key_name (str): A dictionary key to compare

    Returns:
        tuple: A tuple with the first element as the movie's title and the second element as the
        value from the specified key.
    """

    for key, value in movie.items():
        if key == key_name:
            return (movie['Title'], value)
    #if movie.has_key(key_name):
        #return movie['Title'], movie[key_name]
    return (None, None)


def total_runtime_hrs(data):
    """
    Uses the dict.values() method, takes a dictionary of runtime values and returns the total runtime 
    converted from mins to hours. The return value is a whole a number (no fractional component).

    Parameters:
        data (dict): A dictionary of key:value pairs from multiple movies

    Returns:
        int: representing the total number of hours of all key-value pairs in the dictionary
    """
    minutes = 0
    for rt in data.values():
        minutes += rt
    hours = minutes//60
    return hours



def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """
    # PROBLEM 1
    print("\nProblem 01")
    horror_movies = read_csv_to_dicts("./assignments/ps_07/horror_movies.csv")
    jumpscare_data = read_csv_to_dicts("./assignments/ps_07/movie_jumpscares.csv")
    #print(horror_movies)

    #  PROBLEM 2
    print("\nProblem 02")

    for movie in horror_movies:
        clean_row(movie)
    
    for movie in jumpscare_data:
        clean_row(movie)
    #print(horror_movies)
   
    # PROBLEM 3
    print("\nProblem 03")
    
    action_movies = filter_movie_by_genre(horror_movies, 'Action')
    horror_movies = filter_movie_by_genre(horror_movies, 'Horror')

    #print(action_movies)

    # PROBLEM 4
    print("\nProblem 04")
    
    for i in range(len(horror_movies)):
        jumpcount, jumpscarescore = get_jumpscare_data(jumpscare_data, horror_movies[i]['Title'])
        horror_movies[i]['Jump Count'] = jumpcount
        horror_movies[i]['Jump Scare Rating'] = jumpscarescore
    print(f'Horror movie with jump scare data:\n{horror_movies[0]}')

    # PROBLEM 5
    print("\nProblem 05")
    short_movies = filter_movies(horror_movies, 'Runtime', 30,90)
    print(f'Short horror movies:\n{short_movies}')



    # PROBLEM 6
    print("\nProblem 06")
    ghost_terms = ['paranormal', 'Haunted', 'ghost', 'Ghosts']
    ghost_movies = []
    for movie in horror_movies:
        has_ghosts = search_movie_plot(movie, ghost_terms)
        if has_ghosts == True:
            ghost_movies.append(movie)
    print(f'Ghost movies:\n{ghost_movies}')
    
    high_jumpscare_ghost_movies = filter_movies(ghost_movies, 'Jump Count', 10,30)
    
    print(f'\nHigh jumpscare ghost movies:\n{high_jumpscare_ghost_movies}')
    
    # PROBLEM 7
    print("\nProblem 07")
    movie_runtimes = {}
    for movie in high_jumpscare_ghost_movies:
        title, runtime = extract_kv_pair(movie, 'Runtime')
        movie_runtimes[title] = runtime
    print(f'Movie runtimes dictionary:\n{movie_runtimes}')
    
    total_runtime = total_runtime_hrs(movie_runtimes)
    print(f'\nTotal runtime for ghost movies with high number of jump scares:\n{total_runtime}')

    write_dicts_to_csv('stu_jumpscare_ghost_movies.csv', high_jumpscare_ghost_movies, high_jumpscare_ghost_movies[0].keys())

if __name__ == '__main__':
    main()