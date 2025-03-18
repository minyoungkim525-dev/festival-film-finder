from flask import Flask, render_template, request, jsonify
import re
from markupsafe import Markup

app = Flask(__name__)

# Full dataset of 10 award-winning films
data = {
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
        "rating": "93",
        "genres": ["Comedy", "Drama", "Romance"],
        "languages": ["English"],
        "festival_wins": [
            "Palme d'Or (Cannes 2024)",
            "Best Picture (Oscars 2025)",
            "Best Director (Oscars 2025)",
            "Best Actress (Oscars 2025)",
            "Best Original Screenplay (Oscars 2025)",
            "Best Film Editing (Oscars 2025)"
        ],
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
        "rating": "89",
        "genres": ["Drama", "Horror", "Sci-Fi"],
        "languages": ["English"],
        "festival_wins": [
            "Best Actress – Motion Picture Drama (Golden Globes 2025)",
            "Best Actress (SAG Awards 2025)",
            "Best Actress (BAFTA 2025)"
        ],
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
        "rating": "72",
        "genres": ["Musical", "Crime", "Drama"],
        "languages": ["Spanish", "English"],
        "festival_wins": [
            "Jury Prize (Cannes 2024)",
            "Best Supporting Actress (Oscars 2025)",
            "Best International Feature Film (Oscars 2025)"
        ],
        "where_to_watch": ["Netflix"],
        "similar_movie_ids": ["2", "4", "8"]
    },
    "4": {
        "id": "4",
        "title": "A Real Pain",
        "year": "2024",
        "trailer": "https://www.youtube.com/watch?v=b2et8Vpu7Ls",
        "poster": "https://m.media-amazon.com/images/S/pv-target-images/052b01cac315f471530d89c791fd641202cbdd75e0f094dcbbcff885a606f291.jpg",
        "summary": "Mismatched cousins David and Benji reunite for a tour through Poland to honor their beloved grandmother. The adventure takes a turn when the pair’s old tensions resurface against the backdrop of their family history.",
        "director": ["Jesse Eisenberg"],
        "stars": ["Kieran Culkin", "Jesse Eisenberg", "Emma Stone"],
        "running_time": "90",
        "rating": "96",
        "genres": ["Comedy", "Drama"],
        "languages": ["English"],
        "festival_wins": [
            "Best Supporting Actor (Oscars 2025)",
            "Special Jury Prize (La Roche-sur-Yon International Film Festival 2024)"
        ],
        "where_to_watch": ["Hulu"],
        "similar_movie_ids": ["1", "3", "7"]
    },
    "5": {
        "id": "5",
        "title": "Dreams (Sex Love)",
        "year": "2024",
        "trailer": "https://www.youtube.com/watch?v=TMspz330NiE",
        "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Dreams_2024_film_poster.jpg/220px-Dreams_2024_film_poster.jpg",
        "summary": "Dreams (Sex Love) (Norwegian: Drømmer) is a 2024 Norwegian drama film written and directed by Dag Johan Haugerud. After Sex and Love, it is the third part of a trilogy by Haugerud that deals with the complexity of human relationships, sexuality, and social norms. The film follows Johanne's (Ella Øverbye) infatuation with her French teacher Johanna (Selome Emnetu), which ignites tensions within her family as her mother and grandmother confront their own unfulfilled dreams and desires.",
        "director": ["Dag Johan Haugerud"],
        "stars": ["Ella Øverbye", "Selome Emnetu", "Ane Dahl Torp"],
        "running_time": "110",
        "rating": "86",
        "genres": ["Drama", "Romance"],
        "languages": ["Norwegian"],
        "festival_wins": [
            "Golden Bear (Berlin 2025)",
            "FIPRESCI Prize (Berlin 2025)",
            "Prize of the Guild of German Art House Cinemas (Berlin 2025)"
        ],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["1", "6", "9"]
    },
    "6": {
        "id": "6",
        "title": "The Blue Trail",
        "year": "2025",
        "trailer": "https://www.youtube.com/watch?v=M2TlfZsN6q4",
        "poster": "https://a.ltrbxd.com/resized/film-poster/1/0/5/9/3/0/9/1059309-the-blue-trail-0-230-0-345-crop.jpg?v=ee29d361f0",
        "summary": "Tereza, 77, has lived her whole life in a small industrialized town in the Amazon until one day she receives an official government order to relocate to a senior housing colony. The colony is an isolated area where the elderly are brought to 'enjoy' their final years, freeing the younger generation to focus fully on productivity and growth. Tereza refuses to accept this imposed fate. Instead, she embarks on a transformative journey through the rivers and tributaries of the Amazon to fulfill one last wish before her freedom is taken away—a decision that will change her destiny forever.",
        "director": ["Gabriel Mascaro"],
        "stars": ["Denise Weinberg", "Rodrigo Santoro", "Miriam Socorrás"],
        "running_time": "85",
        "rating": "82",
        "genres": ["Adventure", "Fantasy", "Sci-Fi"],
        "languages": ["Portuguese"],
        "festival_wins": [
            "Silver Bear Grand Jury Prize (Berlin 2025)",
            "Prize of the Ecumenical Jury (Berlin 2025)"
        ],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["2", "5", "8"]
    },
    "7": {
        "id": "7",
        "title": "Living the Land",
        "year": "2025",
        "trailer": "https://www.youtube.com/watch?v=R2tu42L7khQ",
        "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Living_the_Land_film_poster.jpg/220px-Living_the_Land_film_poster.jpg",
        "summary": "It is 1991, and China’s socio-economic transformation is profoundly affecting the lives of individual families across the vast nation. Peasant farmers face challenges and technological advances that are radically reshaping their rural way of life. In response, ten-year-old Chuang’s parents have opted to move away to seek work in the city, leaving their third child behind to be raised by extended family and neighbors in their countryside village community.",
        "director": ["Huo Meng"],
        "stars": ["Wang Shang", "Zhang Chuwen", "Zhang Yanrong"],
        "running_time": "132",
        "rating": "84",
        "genres": ["Drama"],
        "languages": ["Mandarin"],
        "festival_wins": [
            "Silver Bear for Best Director (Berlin 2025)"
        ],
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
        "rating": "93",
        "genres": ["Drama", "Comedy"],
        "languages": ["English"],
        "festival_wins": [
            "Silver Bear for Best Leading Performance (Berlin 2025)"
        ],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["3", "7", "10"]
    },
    "9": {
        "id": "9",
        "title": "Blue Moon",
        "year": "2025",
        "trailer": "https://www.youtube.com/watch?v=q407m38w5qw",
        "poster": "https://m.media-amazon.com/images/M/MV5BMGUwNWMyMTAtZDUyZS00NGM0LWJhMzgtMTE4OGI4Y2Q4NWRkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
        "summary": "On the evening of March 31, 1943, legendary lyricist Lorenz Hart confronts his shattered self-confidence in Sardi’s bar as his former collaborator Richard Rodgers celebrates the opening night of his ground-breaking hit musical 'Oklahoma!'",
        "director": ["Richard Linklater"],
        "stars": ["Andrew Scott", "Ethan Hawke", "Margaret Qualley", "Bobby Cannavale"],
        "running_time": "100",
        "rating": "95",
        "genres": ["Drama", "Biography", "Music"],
        "languages": ["English"],
        "festival_wins": ["Silver Bear for Best Supporting Performance (Berlin International Film Festival 2025)"],
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
        "rating": "89",
        "genres": ["History", "Drama", "Romance"],
        "languages": ["Portuguese", "Burmese", "Vietnamese", "English"],
        "festival_wins": ["Best Director (Cannes Film Festival 2024)"],
        "where_to_watch": ["TBA"],
        "similar_movie_ids": ["3", "6", "9"]
    }
}

@app.route('/')
def home():
    featured = ["1", "2", "3"]  # Choose 3 featured entries
    featured_data = [data[fid] for fid in featured]

    return render_template('index.html', featured_data=featured_data)

@app.route('/data')
def get_data():
    return jsonify(data)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("q", "").strip().lower()  
    if not query:
        return render_template("search_results.html", search_term="", results=[])

    query_words = query.split()  # Split multi-word queries
    matching_entries = []

    def highlight_text(text):
        """Highlight all query words in the given text."""
        for word in query_words:
            text = re.sub(f"({re.escape(word)})", r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)
        return Markup(text)

    for entry in data.values():
        # Convert fields into lowercase for comparison
        title = entry["title"].lower()
        genres = " ".join(entry["genres"]).lower()  
        directors = " ".join(entry["director"]).lower()
        stars = " ".join(entry["stars"]).lower()

        # Check if ALL words appear in at least one of the fields
        if all(
            word in title or 
            word in genres or 
            word in directors or 
            word in stars 
            for word in query_words
        ):
            # Copy the entry and highlight matches **only in text fields**
            highlighted_entry = entry.copy()
            highlighted_entry["title"] = highlight_text(entry["title"])
            highlighted_entry["director"] = [highlight_text(d) for d in entry["director"]]
            highlighted_entry["genres"] = [highlight_text(g) for g in entry["genres"]]
            highlighted_entry["stars"] = [highlight_text(s) for s in entry["stars"]]

            matching_entries.append(highlighted_entry)

    return render_template("search_results.html", search_term=query, results=matching_entries)


@app.route('/view/<id>')
def view_data(id):
    film_data = data.get(id)  # Fetch selected film
    if not film_data:
        return render_template("data_not_found.html"), 404

    return render_template("view_data.html", data=film_data, all_movies=data)

@app.route('/add', methods=['GET'])
def add_page():
    """Render the add new film page."""
    return render_template("add_data.html", errors={})

@app.route('/add', methods=['POST'])
def add_data():
    """Handles form submission and adds a new film entry."""
    new_id = str(len(data) + 1)  # Generate new ID

    # Get form data from request
    film_title = request.form.get("title", "").strip()
    year = request.form.get("year", "").strip()
    trailer = request.form.get("trailer", "").strip()
    poster = request.form.get("poster", "").strip()
    summary = request.form.get("summary", "").strip()
    director = request.form.get("director", "").strip()
    stars = request.form.get("stars", "").strip()
    running_time = request.form.get("running_time", "").strip()
    rating = request.form.get("rating", "").strip()
    genres = request.form.get("genres", "").strip()
    languages = request.form.get("languages", "").strip()
    festival_wins = request.form.get("festival_wins", "").strip()
    where_to_watch = request.form.get("where_to_watch", "").strip()

    # Validate required fields
    errors = {}
    if not film_title:
        errors["title"] = "Title is required."
    if not year.isdigit():
        errors["year"] = "Year must be a number."
    if not running_time.isdigit():
        errors["running_time"] = "Running time must be a number."
    if not rating.isdigit() or not (0 <= int(rating) <= 100):
        errors["rating"] = "Rating must be a number between 0 and 100."
    if not director:
        errors["director"] = "At least one director is required."
    if not genres:
        errors["genres"] = "At least one genre is required."
    if not poster:
        errors["poster"] = "A poster URL is required."

    # If errors exist, return JSON response
    if errors:
        return jsonify({"success": False, "errors": errors})

    # Save new entry to the dataset
    data[new_id] = {
        "id": new_id,
        "title": film_title,
        "year": year,
        "trailer": trailer,
        "poster": poster,
        "summary": summary,
        "director": director.split(","),  # Convert to list
        "stars": stars.split(","),  # Convert to list
        "running_time": running_time,
        "rating": rating,
        "genres": genres.split(","),  # Convert to list
        "languages": languages.split(","),
        "festival_wins": festival_wins.split(","),
        "where_to_watch": where_to_watch.split(","),
        "similar_movie_ids": []  # Empty for now
    }

    return jsonify({"success": True, "id": new_id})

@app.route('/edit/<id>', methods=['GET'])
def edit_data(id):
    """Render the edit form with pre-filled data."""
    film_data = data.get(id)
    if not film_data:
        return render_template("data_not_found.html"), 404  # If the film is not found

    return render_template("edit_data.html", data=film_data)

@app.route('/edit/<id>', methods=['POST'])
def update_data(id):
    """Handles form submission and updates film data."""
    if id not in data:
        return jsonify({"success": False, "error": "Film not found"}), 404

    # Get form data
    title = request.form.get("title", "").strip()
    year = request.form.get("year", "").strip()
    director = request.form.get("director", "").strip().split(", ")
    stars = request.form.get("stars", "").strip().split(", ")
    genres = request.form.get("genres", "").strip().split(", ")
    rating = request.form.get("rating", "").strip()
    summary = request.form.get("summary", "").strip()

    # Validation
    errors = {}
    if not title:
        errors["title"] = "Title is required."
    if not year.isdigit():
        errors["year"] = "Year must be a number."
    if not rating.isdigit():
        errors["rating"] = "Rating must be a number."

    if errors:
        return jsonify({"success": False, "errors": errors})

    # Update data
    data[id].update({
        "title": title,
        "year": year,
        "director": director,
        "stars": stars,
        "genres": genres,
        "rating": rating,
        "summary": summary
    })

    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
