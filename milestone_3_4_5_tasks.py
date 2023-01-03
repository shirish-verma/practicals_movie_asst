# Milestone 3, Task 1 - Load in the Full Movies Dataset from a File
import json

movie_file = open('movies.json')
movie_list = json.load(movie_file)
print(type(movie_list))
for item in movie_list:
    print(item)
print('End of Milestone 3, Task 1', end='\n\n')

# Milestone 3, Task 2 - What are the Unique Genres?

def get_unique_genres():
    genre_list = [main_item['genre'] for main_item in movie_list]
    genre_set = set(genre_list)
    return genre_set

print(get_unique_genres())
print('End of Milestone 3, Task 2', end='\n\n')

# Milestone 3, Task 3 - Filter by genre

def get_movies_in_genre(selected_genre):
    filtered_by_genre = [item for item in movie_list if item['genre'].lower() == selected_genre.lower()]
    return filtered_by_genre

print(get_movies_in_genre('Horror'))
print('End of Milestone 3, Task 3', end='\n\n')

# Milestone 4, Task 1 - Ask user for interested genre

def get_user_genre_choice():
    print('Please select the genre you are interested in from the below:')
    unique_genres = get_unique_genres()
    for items in unique_genres:
        print(items)
    while True:
        try:
            genre_choice = input('Selected Genre: ')
            if genre_choice.title() in unique_genres:
                return genre_choice
            else:
                raise ValueError
        except ValueError:
            print('This is not a valid genre.')
    

print('End of Milestone 4, Task 1 & Milestone 5, Tasks 1, 2 & 3', end='\n\n')

# Milestone 4, Task 2 - Show the movies in selected genre

genre_choice = get_user_genre_choice()
print('')
filtered_movies = get_movies_in_genre(genre_choice)
filtered_movies_titles = [titles['title'] for titles in filtered_movies]

print(f'The movies in your chosen genre "{genre_choice}" are: ')
for f_index, f_title in enumerate(filtered_movies_titles):
    f_index_user = f_index + 1
    print(f'{f_index_user}. {f_title}')

print('End of Milestone 4, Task 2', end='\n\n')

# Milestone 4, Task 3 - Ask user to select one movie, display details

def get_movie_by_index(genre_choice):
    print(f'The movies in your chosen genre "{genre_choice}" are: ')
    filtered_movies = get_movies_in_genre(genre_choice)
    filtered_movies_titles = [titles['title'] for titles in filtered_movies]
    for f_index, f_title in enumerate(filtered_movies_titles, 1):
        print(f'{f_index}. {f_title}')
    selected_movie_index = int(input('Select a movie by entering its index number here: '))
    selected_movie_title = filtered_movies_titles[selected_movie_index - 1].lower()
    for movie in filtered_movies:
        if movie['title'].lower() == selected_movie_title:
            for key, value in movie.items():
                print(f'{key.title()}: {value}, ','')

get_movie_by_index(genre_choice)

print('End of Milestone 4, Task 3', end='\n\n')
