import media
import fresh_tomatoes
toy_story=media.Movie("Toy Story", "Story of a boy and his toys","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar=media.Movie("Avatar","Story of another planet, and their quest to save themselves from humans","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
Jumanji=media.Movie("Jumanji","Story of a mythical game","https://upload.wikimedia.org/wikipedia/en/b/b6/Jumanji_poster.jpg","https://www.youtube.com/watch?v=5p18zqZmeiI")
Wonder_Woman=media.Movie("Wonder Woman","Story of a wonderfully powerful superwoman","https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg","https://www.youtube.com/watch?v=INLzqh7rZ-U")
Basic_Instinct=media.Movie("Basic Instinct","Story of a murderous and psycopathic woman","https://upload.wikimedia.org/wikipedia/en/f/f9/Basic_instinct.jpg","https://www.youtube.com/watch?v=wLGx5YT6sOg")
The_Godfather=media.Movie("The Godfather","Story of a sicilian crime family in New York","https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg","https://www.youtube.com/watch?v=sY1S34973zA")

#print(avatar.storyline)
#toy_story.showtrailer()
movies=[toy_story,avatar,Jumanji,Wonder_Woman,Basic_Instinct,The_Godfather]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALIDRATING)
