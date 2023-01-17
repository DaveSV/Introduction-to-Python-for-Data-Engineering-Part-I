## 1. If Statements ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = []
rating = 0
price = 0

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price == 0.0:
        ratings.append(rating)

avg_rating_free =sum(ratings) / len(ratings)
print(avg_rating_free)

## 2. Booleans ##

a_price = 0

if a_price == 0:
    print('This is free')
    
if a_price == 1:
    print('This is not free')

## 3. The Average Rating of Non-free Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_free_apps_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    
    if price != 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

## 4. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_games_ratings = []
rating = 0.0
genre = ""

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    
    if genre != "Games":
        non_games_ratings.append(rating)
    
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)
print(avg_rating_non_games)

## 5. Multiple Conditions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

free_games_ratings = []
rating = 0.0
price = 0.0
genre = ""

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    
    if price == 0.0 and genre == "Games":
        free_games_ratings.append(rating)
    
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)
print(avg_rating_free_games)

## 6. The or Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

games_social_ratings = []
rating = 0.0
price = 0.0
genre = ""

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)
    
avg_games_social = sum(games_social_ratings) / len(games_social_ratings)
print(avg_games_social)

## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_free_games_social_ratings = []
rating = 0.0
price = 0.0
genre = ""

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0.0:
        non_free_games_social_ratings.append(rating)
    
avg_non_free = sum(non_free_games_social_ratings) / len(non_free_games_social_ratings)
print(avg_non_free)

## 8. The Not Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_free_games_social_ratings = []
rating = 0.0
price = 0.0
genre = ""

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    
    if not (genre == 'Social Networking' or genre == 'Games') and price != 0.0:
        non_free_games_social_ratings.append(rating)
    
avg_non_free_non_sn_games = sum(non_free_games_social_ratings) / len(non_free_games_social_ratings)
print(avg_non_free_non_sn_games)

## 9. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

ratings = []
rating = 0.0
price = 0.0
genre = ""

n_apps_more_9 = 0
n_apps_less_9 = 0

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price > 9.0:
        ratings.append(rating)
        n_apps_more_9 = n_apps_more_9 + 1

n_apps_less_9 = len(apps_data[1:]) - n_apps_more_9
avg_rating = sum(ratings) / len(ratings)

## 10. The else Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')
        
apps_data[0].append('free_or_not')

print(apps_data)

## 11. The elif Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0.0:
        app.append('free')
    elif price > 0.0 and price < 20:
        app.append('affordable')
    elif price > 20 and price < 50:
        app.append('expensive')
    elif price > 50:
        app.append('very expensive')
        
apps_data[0].append('price_label')

print(apps_data)