#The Range Riddle
#task1 Write a program that prints off different moods for each day of the week.
 #"Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm"
#Using the range() function, loop through the days of the week and for each day, 
#randomly select a mood from the list and print it
#Ensure that your program includes the use of the random module to select the mood
mood_list = ["Happy", "Sad", "Energetic", "Calm"]
print(mood_list)
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
import random
for i in range(len(days_of_week)):
    mood = random.choice(mood_list)
    print(f"on [{days_of_week[i]}] you feel [{mood}]")

#2 Double Scoop with Nested Loops
mood_list = ["Happy", "Sad", "Energetic", "Calm"]
time_of_day = ["Morning", "Afternoon", "Evening"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#the outer loop should iterate over the days,
for day in days_of_week:
    for time in time_of_day: #the inner loop should iterate over the times of the day
        mood = random.choice(mood_list) #For each time, randomly select a mood from a predefined list and print it)
        print(f"on {day} {time} you felt {mood}")

# Loop Condition Logic
#task1 Write a while loop with a condition that will never be true (an infinite loop). Inside the loop, print a statement. 
#Then, use a break statement to exit the loop after 5 iterations.
iterations = 0
while True:
    print("you stuck")
    iterations += 1
    if iterations >= 5:
        break
# task2 Conditional Exit
iterations = 0
while iterations < 5:
    print("Hello")
    iterations += 1

#Python's Random Game Night
#task1Create a game where a player has a list of items. 
list_of_items = ["sword", "shield", "potion", "armor"]
#They have to guess which item in the list was selected.
selected_item = random.choice(list_of_items)
guess = input("Guess the item:")
if guess == selected_item:
    print("You guessed correctly!")
else:
    print("You guessed incorrectly!")

# Looping Lists - The Rhythm of Repetition
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
#task1write a for loop that prints out each genre with a custom message
for i in range(len(genres)):
    print("Song", i + 1, ": singing", genres[i])
#task2
#Convert the for loop from Task 1 into a while loop. Ensure it performs the same function 
#but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.
    i = 0
while i < len(genres):
    genre = genres[i]
    print("song", i + 1, ": singing", genre)
    if genre == 'Hip-hop':
        break
    i += 1
#task3 
for i in range(len(genres)):
    if genres[i] != 'Classical':
        print("Song", i + 1, ": Light show is suitable for ", genres[i])

#Advanced Looping Techniques
#task1
for genre in genres[1:4]:
    print(genre)

#task2
sublist_genres = [genre + " Music" for genre in genres]
print(sublist_genres)

#task3 
for i in range(10, 0, -1):
    print(i)
print("The beat drops now!")

