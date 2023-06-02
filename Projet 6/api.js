async function main() {

    const apiUrl = "http://localhost:8000/api/v1/titles";

    console.log("Hello");

    async function get_info(parameter, value) {
        const responseRaw = await fetch(`${apiUrl}/?${parameter}=${value}`);
        if (responseRaw.ok === true) {
            const responseJson = await responseRaw.json();
            return responseJson;
        }
        throw new Error("Oops !")

    }
    const bestMovie = await get_info("sort_by", "-imdb_score")
    console.log(bestMovie.results[0]["image_url"])

    const cat1 = await get_info("genre", "Comedie");
    console.log(cat1);

    const cat2 = await get_info("genre", "Romance");
    console.log(cat2);

    const cat3 = await get_info("genre", "Action");
    console.log(cat3);
}

main()
/*
let bestMovie2 = get_info("sort_by", "-imdb_score")
    .then(r => r.results[0]);
console.log();

const cat1 = get_info("genre", "Comedie");
console.log(cat1);

const cat2 = get_info("genre", "Romance");
console.log(cat2);

const cat3 = get_info("genre", "Action");
console.log(cat3);

const r = fetch(apiUrl)
    .then(r => r.json())
    .then(body => console.log(body.results[0]["image_url"]))
*/
// const data = bestMovie.get("response");
// console.log(data);

// const bestMovieDiv = document.getElementById("best-movie");
// bestMovieDiv.style.backgroundImage = 'url("")';


/*

const r = fetch(apiUrl)
    .then(r => r.json())
    .then(body => console.log(body))

async function get_info(url) {
    const responseRaw = await fetch(url);
    responseRaw.text()
    return responseRaw.body
    /*
    if (responseRaw.ok === true) {
        responseRaw.text();
        return responseRaw.body;
    }
    // else { const response404 = "Oops !"; return response404 }
    throw new Error("Oops !")

}
const test = get_info(apiUrl);
console.log(test);


async function get_info(parameter, value) {
    const responseRaw = await fetch(`${apiUrl}/?${parameter}=${value}`);
    if (responseRaw.ok === true) {
        const responseJSON = responseRaw.json();
        return response
    }
    // else { const response404 = "Oops !"; return response404 }
    throw new Error("Oops !")

}
const romance = get_info("genre", "Romance");
console.log(best_movie);

const best_movie = get_info("sort_by", "-imdb_score");
const data = best_movie[0];
console.log(data);
*/

// const imageFrame = document.getElementById("img1.1");
// imageFrame.src = '';

