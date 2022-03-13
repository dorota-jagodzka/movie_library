from random import random


class MovieLibrary():

    def __init__(self, title, date, genre, replay_number):
        self.title = title
        self.date = date
        self.genre = genre
        self.replay_number = replay_number

    def movie_info(self):
        print(f"{self.title} {self.date}")

    def increase_reply_number(self):
        reply_number_increase = self.replay_number + 1
        return reply_number_increase

class SeriesLibrary(MovieLibrary):

    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def series_info(self):
        print(f"{self.title} {self.episode_number}{self.season_number}")


    def increase_reply_number(self):
        reply_number_increase = self.replay_number + 1
        return reply_number_increase


def get_movies_or_series(list_to_filtr, class_filter):
    result_list = []
    for element in list_to_filtr:
        if isinstance(element, class_filter):
            result_list.append(element)
    return result_list

def search(list_to_filtr, title): 
    for element in list_to_filtr:
        if element.title == title:
            return element

def generate_views(list):
    chosen_element = random.choice(list)
    chosen_element.replay_number += random.randint(1, 100)
    return chosen_element

def generate_views_ten_times(list):
    list_with_increased_views = []
    for i in range(0,10):
        element = generate_views(list)
        list_with_increased_views.append(element)
    return list_with_increased_views

def top_titles(list, count):
    sorted(list, key=lambda MovieLibrary: MovieLibrary.replay_number)
    result_list = []
    for i in range(0, count):
        result_list.append(list[i])
    return result_list


def print_result(str_or_list):
    result = ""
    if isinstance(str_or_list, list):
        for element in str_or_list:
            result += element.title + " "
    else:
        result = str_or_list.title
        
    return result


friends_series = SeriesLibrary(title = "Friends", date = "(1990)", genre = "comedy", replay_number = 50, episode_number= "E15", season_number= "S05")
house_series = SeriesLibrary(title = "Dr. House", date = "(2001)", genre = "drama", replay_number = 30, episode_number= "E13", season_number= "S02")
the_Office_series = SeriesLibrary(title = "The Office", date= "(2010", genre = "comedy", replay_number = 20, episode_number= "E12", season_number= "S04")
pulp_Fiction_movie = MovieLibrary(title = "Pulp Fiction", date = "(1994)", genre = "action", replay_number = 12)
infiltration_movie = MovieLibrary(title= "Inflitration", date= "(1990)", genre = "crime story", replay_number= 2)
fight_club_movie = MovieLibrary(title = "Fight Club", date = "(1980", genre = "psychological", replay_number= 4)

MovieLibrary.movie_info(pulp_Fiction_movie)
# print(Friends_series)

SeriesLibrary.series_info(friends_series)
# print(Friends_series)

print(SeriesLibrary.increase_reply_number(friends_series))
print(MovieLibrary.increase_reply_number(pulp_Fiction_movie))


list_to_filtr = []
list_to_filtr.append(friends_series)
list_to_filtr.append(house_series)
list_to_filtr.append(the_Office_series)
list_to_filtr.append(pulp_Fiction_movie)
list_to_filtr.append(infiltration_movie)
list_to_filtr.append(fight_club_movie)

print(list_to_filtr)

series_filter_result = get_movies_or_series(list_to_filtr, SeriesLibrary)
movies_filter_result = get_movies_or_series(list_to_filtr, MovieLibrary)
search_result = search(list_to_filtr,"Pulp Fiction");
# generate_views_one_time = generate_views(list_to_filtr)
# generate_views_ten_times_result = generate_views_ten_times(list_to_filtr)
top_titles_result = top_titles(list_to_filtr, 2)
print("Filter result:")
print(print_result(series_filter_result))
print(print_result(movies_filter_result))
# print(print_result(generate_views) + " " + generate_views.replay_number)

# print("Movies or series that replay number had been increased")
# print(print_result(generate_views_ten_times_result))
# print(print_result(top_titles_result)

print(print_result(search_result))

# 1. 

# if issubclass(SeriesLibrary, MovieLibrary):
#   print("TAK")

# def costam(lista_jakas, JAKAS_KLASA):
#   pusta = []
#   for element in lista_jakas:
#     if isinstance(element, JAKAS_KLASA): 
#       pass
#       #do_something
      

# # A -> B -> C

# isinstance(OBKIEKT_KLASY_A, C)
# type(jakis_obiekt_klasy_a) == C # fałsz

# result = isinstance(Pulp_Fiction_movie, MovieLibrary)
# print(result)

# items_in_the_library = [Friends_series, Pulp_Fiction_movie]
    
# movies = filter(lambda MovieLibrary: MovieLibrary.title, items_in_the_library)
# print(movies)