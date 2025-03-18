document.addEventListener("DOMContentLoaded", function () {
    fetch("/data")
        .then(response => response.json())
        .then(dataset => {
            console.log("Fetched data:", dataset);

            let container = document.getElementById("popular-data");
            if (!container) {
                console.error("Error: #popular-data container not found!");
                return;
            }

            let featured = ["1", "2", "3"];
            featured.forEach(id => {
                let entry = dataset[id];
                let entryCard = `
                    <div class="col-md-4">
                        <div class="card">
                            <img src="${entry.poster}" class="card-img-top" alt="${entry.title}">
                            <div class="card-body">
                                <h5 class="card-title">${entry.title}</h5>
                                <p class="card-text">${entry.summary.substring(0, 100)}...</p>
                                <a href="/view/${entry.id}" class="btn btn-primary">View Details</a>
                            </div>
                        </div>
                    </div>
                `;
                container.innerHTML += entryCard;
            });
        });

    // Search functionality
    document.getElementById("search-form").addEventListener("submit", function (event) {
        let query = document.getElementById("search-input").value.trim();
        if (!query) {
            event.preventDefault();
            document.getElementById("search-input").focus();
        }
    });
});
