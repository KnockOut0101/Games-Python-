import random

Movie_File = open("movie.txt","r")

movies = Movie_File.readlines()

movies_full = []
movies_guess = []

#print(movies,"\n")

Movie_File.close()

for i in range(len(movies)):
    answer = movies[i].split(";")
    movies_full.append(answer[0])
    movies_guess.append(answer[1])

#print(movies_full,"\n",movies_guess)

# for some reason the mummy has some form of weird text before it therefor mannually changing it

movies_full[0] = 'The Mummy'

#print(movies_full)

def check_index(movie_guess_name):
    for i in range(len(movies_guess)):
        if(movies_guess[i] == movie_guess_name):
            return i

#def check_blanks(User_guess):


def game():
    lives = 8
    count = 0

    while(lives > 0 and count < 10):

        movie_guess = random.choice(movies_guess)
        print(movie_guess)
        User_input = input("Guess the above movie :-")
        index = check_index(movie_guess)
        if(User_input == movies_full[index]):
            count = count + 1
            print(count,"You got it")
        else:
            lives = lives - 1
            print(lives,"Nah ! try again")
    if(lives == 0):
        print("You failed Score:-%d"%(count))
    if(count == 10):
        print("You won")

game()