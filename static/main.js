document.addEventListener("DOMContentLoaded", function () {
    fetch("/films")
        .then(response => response.json())
        .then(filmData => {
            console.log("Fetched film data:", filmData);

            const topAwardedFilmIds2024 = ["1", "2", "3"];
            const container = document.getElementById("popular-films");

            topAwardedFilmIds2024.forEach(filmId => {
                const film = filmData[filmId];

                if (!film) {
                    console.error(`Error: Film ID ${filmId} not found in data.`);
                    return;
                }

                const filmCard = document.createElement("div");
                filmCard.classList.add("col-md-4", "d-flex");

                filmCard.innerHTML = `
                    <div class="card w-100">
                        <a href="/view/${film.id}">
                            <img src="${film.poster}" class="card-img-top" alt="${film.title}" 
                                onerror="this.onerror=null; this.src='https://via.placeholder.com/300x450';">
                        </a>
                        <div class="card-body">
                            <h5 class="card-title">${film.title} (${film.year})</h5>
                            <p class="card-text">${film.summary.substring(0, 100)}...</p>
                            <a href="/view/${film.id}" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                `;
                container.appendChild(filmCard);
            });
        })
        .catch(error => console.error("Error fetching films:", error));
});
