const category1 = "Comedy";
const category2 = "Romance";
const category3 = "Action";
const vignettes_num = [0, 1, 2, 3, 4, 5, 6];

document.getElementById("title-cat1").innerHTML = category1
document.getElementById("title-cat2").innerHTML = category2
document.getElementById("title-cat3").innerHTML = category3

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
    const bestMovie = await get_info("sort_by", "-imdb_score");
    const img = bestMovie.results[0]["image_url"];
    const title = bestMovie.results[0]["title"];
    const description = bestMovie.results[0]["genres"] + ", " + bestMovie.results[0]["year"];
    //console.log(img)


    const bestMovieDiv = document.getElementById("best-movie");
    const bestMovieTitle = document.getElementById("best-title");
    const bestMovieDescription = document.getElementById("best-description");

    bestMovieDiv.style.background = `url(${img}) no-repeat`;
    bestMovieDiv.style.backgroundSize = `cover`;
    bestMovieTitle.innerHTML = title
    bestMovieDescription.innerHTML = description
    //bestMovieDiv.style.backgroundSize = `${bestMovieDiv.getBoundingClientRect()['width']}px ${bestMovieDiv.getBoundingClientRect()['height']}px `;
    //console.log(bestMovieDiv.getBoundingClientRect())
    //console.log(bestMovieDiv.getBoundingClientRect()['width'])
    //console.log(bestMovieDiv.getBoundingClientRect()['height'])


    const cat1 = await get_info("genre", `${category1}`);
    console.log(cat1.results);

    const cat2 = await get_info("genre", `${category2}`);
    console.log(cat2.results);

    const cat3 = await get_info("genre", `${category3}`);
    console.log(cat3.results);
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

