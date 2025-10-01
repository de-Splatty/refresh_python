current_movie = {"Infinity castle" : "4:30pm",
                 "The lost city" : "6:30pm",
                 "Spiderman" : "8:30pm",
                 "Black Adam" : "10:30pm"
                 }

print("Current movies available are: ")
for key in current_movie:
    print(key)

movie = input("Enter the movie you want to watch: \n")

showtime = current_movie.get(movie)

if showtime == None:
    print("Sorry, we don't have that movie.")
    print("Available movies are:")
    for key in current_movie:
        print(key)
else:
    print("The showtime for", movie, "is", showtime)