from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Full dataset of 10 award-winning films
films = {
    "1": {
        "id": "1",
        "title": "Anora",
        "year": "2024",
        "trailer": "https://www.youtube.com/watch?v=p1HxTmV5i7c",
        "poster": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTUrnFpWoBX-BQqEzH_FJMrwnxUboIKz871hMm3ECVa3WWKR1rv",
        "summary": "Anora, a young sex worker from Brooklyn, gets her chance at a Cinderella story when she meets and impulsively marries the son of an oligarch. Once the news reaches Russia, her fairytale is threatened as the parents set out for New York to get the marriage annulled.",
        "director": ["Sean Baker"],
        "stars": ["Mikey Madison", "Mark Eydelshteyn", "Yura Borisov"],
        "running_time": "139",
        "metacritic_score": "91",
        "genres": ["Comedy", "Drama", "Romance"],
        "languages": ["English"],
        "festival_wins": ["Palme d'Or (Cannes 2024)", "Best Picture (Oscars 2025)"],
        "where_to_watch": ["Amazon Prime Video", "Apple TV+"],
        "similar_movie_ids": ["2", "5", "7"]
    },
    "2": {
        "id": "2",
        "title": "The Substance",
        "year": "2024",
        "trailer": "https://www.youtube.com/watch?v=LNlrGhBpYjc",
        "poster": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTIx9upFCbgEVt9eJ3dzSrogBbwMCpx8d4Jc82yWbjQmSCNX1uN",
        "summary": "The Substance is a 2024 body horror film written and directed by Coralie Fargeat. It follows a fading celebrity, Elisabeth Sparkle (Demi Moore), who, after being fired by her producer (Dennis Quaid) due to her age, uses a black market drug that creates a younger version of herself (Margaret Qualley) with unexpected side effects.",
        "director": ["Coralie Fargeat"],
        "stars": ["Demi Moore", "Margaret Qualley", "Dennis Quaid"],
        "running_time": "141",
        "metacritic_score": "78",
        "genres": ["Drama", "Horror", "Sci-Fi"],
        "languages": ["English"],
        "festival_wins": ["Best Actress (Oscars 2025)", "Best Screenplay (Cannes 2024)"],
        "where_to_watch": ["MUBI"],
        "similar_movie_ids": ["1", "4", "6"]
    },
    "3": {
        "id": "3",
        "title": "Emilia Pérez",
        "year": "2024",
        "trailer": "https://www.youtube.com/watch?v=4h7j_EcZ5fU",
        "poster": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS_giq-Fdb2wZXhHCWtKk8csWmCRLAMcmRkd7PZYeOQihy-W7j6",
        "summary": "Overqualified and undervalued, Rita is a lawyer at a large firm that is more interested in getting criminals off the hook than bringing them to justice. One day, she is given an unexpected way out, when cartel leader Manitas hires her to help him withdraw from his business and realize a plan he has been secretly preparing for years: to become the woman he has always dreamt of being.",
        "director": ["Jacques Audiard"],
        "stars": ["Zoe Saldaña", "Selena Gomez", "Adriana Paz"],
        "running_time": "132",
        "metacritic_score": "70",
        "genres": ["Musical", "Crime", "Drama"],
        "languages": ["Spanish", "English"],
        "festival_wins": ["Best Supporting Actress (Oscars 2025)", "Jury Prize (Cannes 2024)"],
        "where_to_watch": ["Netflix"],
        "similar_movie_ids": ["2", "4", "8"]
    },
    "4": {
        "id": "4",
        "title": "A Real Pain",
        "year": "2024",
        "trailer": "https://www.youtube.com/watch?v=b2et8Vpu7Ls",
        "poster": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRoLP12wbeFEO4VqSea7Jv-bBTnoixlLxrM-AJ1f9a2QRaeIBq",
        "summary": "Mismatched cousins David and Benji reunite for a tour through Poland to honor their beloved grandmother. The adventure takes a turn when the pair’s old tensions resurface against the backdrop of their family history.",
        "director": ["Jesse Eisenberg"],
        "stars": ["Kieran Culkin", "Jesse Eisenberg", "Emma Stone"],
        "running_time": "90",
        "metacritic_score": "85",
        "genres": ["Comedy", "Drama"],
        "languages": ["English"],
        "festival_wins": ["Best Supporting Actor (Oscars 2025)"],
        "where_to_watch": ["Hulu"],
        "similar_movie_ids": ["1", "3", "7"]
    },
    "5": {
        "id": "5",
        "title": "Dreams (Sex Love)",
        "year": "2024",
        "trailer": "https://www.youtube.com/watch?v=TMspz330NiE",
        "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Dreams_2024_film_poster.jpg/220px-Dreams_2024_film_poster.jpg",
        "summary": "Dreams (Sex Love) (Norwegian: Drømmer) is a 2024 Norwegian drama film written and directed by Dag Johan Haugerud. After Sex and Love, it is the third part of a trilogy by Haugerud that deals with the complexity of human relationships, sexuality and social norms. The film follows Johanne's (Ella Øverbye) infatuation with her french teacher Johanna (Selome Emnetu), which ignite tensions within her family, as her mother and grandmother confront their own unfulfilled dreams and desires.",
        "director": ["Dag Johan Haugerud"],
        "stars": ["Ella Øverbye", "Selome Emnetu", "Ane Dahl Torp"],
        "running_time": "110",
        "metacritic_score": "86",
        "genres": ["Drama", "Romance"],
        "languages": ["Norwegian"],
        "festival_wins": ["Golden Bear (Berlin 2025)"],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["1", "6", "9"]
    },
    "6": {
        "id": "6",
        "title": "The Blue Trail",
        "year": "2025",
        "trailer": "https://www.youtube.com/watch?v=M2TlfZsN6q4",
        "poster": "https://www.hollywoodreporter.com/wp-content/uploads/2025/02/THE_BLUE_TRAIL_Still_1Guillermo_Garza_Desvia.jpg?crop=0px%2C428px%2C4608px%2C2578px&resize=450%2C253",
        "summary": "Tereza, 77, has lived her whole life in a small industrialised town in the Amazon, until one day she receives an official government order to relocate to a senior housing colony. The colony is an isolated area where the elderly are brought to “enjoy” their final years, freeing the younger generation to focus fully on productivity and growth. Tereza refuses to accept this imposed fate. Instead, she embarks on a transformative journey through the rivers and tributaries of the Amazon to fulfil one last wish before her freedom is taken away – a decision that will change her destiny forever.",
        "director": ["Gabriel Mascaro"],
        "stars": ["Denise Weinberg", "Rodrigo Santoro", "Miriam Socorrás"],
        "running_time": "85",
        "metacritic_score": "82",
        "genres": ["Adventure", "Fantasy", "Sci-Fi"],
        "languges": ["Portuguese"],
        "festival_wins": ["Silver Bear Grand Jury Prize (Berlin 2025)"],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["2", "5", "8"]
    },
    "7": {
        "id": "7",
        "title": "Living the Land",
        "year": "2025",
        "trailer": "https://www.youtube.com/watch?v=R2tu42L7khQ",
        "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Living_the_Land_film_poster.jpg/220px-Living_the_Land_film_poster.jpg",
        "summary": "It is 1991, and China’s socio-economic transformation is profoundly affecting the lives of individual families across the vast nation. Peasant farmers face challenges and technological advances that are radically reshaping their rural way of life. In response, ten-year-old Chuang’s parents have opted to move away to seek work in the city, leaving their third child behind to be raised by extended family and neighbours in their countryside village community.",
        "director": ["Huo Meng"],
        "stars": ["Wang Shang", "Zhang Chuwen", "Zhang Yanrong"],
        "running_time": "132",
        "metacritic_score": "84",
        "genres": ["Drama"],
        "languges": ["Mandarin"],
        "festival_wins": ["Best Director (Berlin 2025)"],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["4", "6", "9"]
    },
    "8": {
        "id": "8",
        "title": "If I Had Legs, I'd Kick You",
        "year": "2025",
        "trailer": "https://www.youtube.com/watch?v=UqQG4Ky-kT0",
        "poster": "https://m.media-amazon.com/images/M/MV5BODdmZWZlZmYtZGM5OS00YjZiLTkxMGQtYTc0NThmN2E4NGQzXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
        "summary": "A character-driven drama featuring a powerful performance by Rose Byrne. With her life crashing down around her, Linda attempts to navigate her child’s mysterious illness, her absent husband, a missing person, and an increasingly hostile relationship with her therapist.",
        "director": ["Mary Bronstein"],
        "stars": ["Rose Byrne", "Conan O'Brien", "Danielle Macdonald"],
        "running_time": "113",
        "metacritic_score": "82",
        "genres": ["Drama", "Comedy"],
        "languages": ["English"],
        "festival_wins": ["Best Leading Performance (Berlin 2025)"],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["3", "7", "10"]
    },
    "9": {
        "id": "9",
        "title": "Blue Moon",
        "year": "2025",
        "trailer": "https://www.youtube.com/watch?v=q407m38w5qw",
        "poster": "https://m.media-amazon.com/images/M/MV5BMGUwNWMyMTAtZDUyZS00NGM0LWJhMzgtMTE4OGI4Y2Q4NWRkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
        "summary": "On the evening of March 31, 1943, legendary lyricist Lorenz Hart confronts his shattered self-confidence in Sardi’s bar as his former collaborator Richard Rodgers celebrates the opening night of his ground-breaking hit musical “Oklahoma!”",
        "director": ["Richard Linklater"],
        "stars": ["Andrew Scott", "Ethan Hawke", "Margaret Qualley", "Bobby Cannavale"],
        "runng_time": "100",
        "metacritic_score": "76",
        "genres": ["Drama", "Biography", "Music"],
        "languages": ["English"],
        "festival_wins": ["Best Supporting Performance (Berlin 2025)"],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["5", "6", "8"]
    },
    "10": {
        "id": "10",
        "title": "Grand Tour",
        "year": "2024",
        "trailer": "https://www.youtube.com/watch?v=oN0wM9QLu3c",
        "poster": "https://upload.wikimedia.org/wikipedia/en/9/95/Grand_Tour_2024_film_poster.jpg",
        "summary": "Rangoon, Burma, 1917. Edward, a civil servant for the British Empire, runs away from his fiancée Molly the day she arrives to get married. During his travels, however, panic gives way to melancholy. Contemplating the emptiness of his existence, the cowardly Edward wonders what has become of Molly. Determined to get married and amused by Edward’s move, Molly follows his trail on this Asian grand tour.",
        "director": ["Miguel Gomes"],
        "stars": ["Crista Alfaiate", "Gonçalo Waddington"],
        "running_time": "129",
        "metacritic_score": "77",
        "genres": ["History", "Drama", "Romance"],
        "languages": ["Portuguese", "Burmese", "Vietnamese", "English"],
        "festival_wins": ["Best Director (Cannes 2024)"],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["3", "6", "9"]
    }
}



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/films')
def get_films():
    return jsonify(films)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("q", "").strip().lower()  # Get search query, remove whitespace, convert to lowercase
    if not query:
        return render_template("search_results.html", search_term="", results=[])

    matching_films = [
        film for film in films.values() if query in film["title"].lower()
    ]

    return render_template("search_results.html", search_term=query, results=matching_films)

@app.route('/view/<id>')
def view_film(id):
    film = films.get(id)
    if not film:
        return render_template("film_not_found.html"), 404
    return render_template("film_detail.html", film=film)

if __name__ == '__main__':
    app.run(debug=True)
