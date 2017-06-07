import fresh_tomatoes
import media

inception = media.Movie("Inception","Dream within a dream","https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg","https://www.youtube.com/watch?v=YoHD9XEInc0")
#print (toy_story.storyline)
#toy_story.show_trailer()
interstellar = media.Movie("Interstellar","Save earth","https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg","https://www.youtube.com/watch?v=M-xglYg-TTw")
wolverine = media.Movie("The Wolverine","Mutant soldier in Japan","http://t2.gstatic.com/images?q=tbn:ANd9GcQc9ZET5WDJK3KsCIG-YCL24Ge8rRTtORNzmLewFiaasbtNnx24","https://www.youtube.com/watch?v=Rh1LdTFkm7I")
wonderwoman = media.Movie("Wonder Woman","End the war","http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H","https://www.youtube.com/watch?v=INLzqh7rZ-U")


movies = [inception, interstellar, wolverine, wonderwoman]
fresh_tomatoes.open_movies_page(movies)
