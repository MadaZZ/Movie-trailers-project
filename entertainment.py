import media
import fresh_tomatoes
toy_story=media.Movie("Toy Story", "Story of a boy and his toys","https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar=media.Movie("Avatar","Story of another planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
jumanji=media.Movie("Jumanji","Story of a mythical game","https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg","https://www.youtube.com/watch?v=5p18zqZmeiI")
jumanji1=media.Movie("Jumanji","Story of a mythical game","http://www.imdb.com/title/tt2283362/mediaviewer/rm4093126400","https://www.youtube.com/watch?v=5p18zqZmeiI")
jumanji2=media.Movie("Jumanji","Story of a mythical game","http://www.imdb.com/title/tt2283362/mediaviewer/rm4093126400","https://www.youtube.com/watch?v=5p18zqZmeiI")
jumanji3=media.Movie("Jumanji","Story of a mythical game","http://www.imdb.com/title/tt2283362/mediaviewer/rm4093126400","https://www.youtube.com/watch?v=5p18zqZmeiI")

#print(avatar.storyline)
#toy_story.showtrailer()
movies=[toy_story,avatar,jumanji,jumanji1,jumanji2,jumanji3]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALIDRATING)
