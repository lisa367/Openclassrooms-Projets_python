const category1 = "Comedy";
const category2 = "Romance";
const category3 = "Action";
const vignettes_num = [0, 1, 2, 3, 4, 5, 6];

document.getElementById("title-cat1").innerHTML = category1;
document.getElementById("title-cat2").innerHTML = category2;
document.getElementById("title-cat3").innerHTML = category3;

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
    const bestImdb = await get_info("sort_by", "-imdb_score");
    const bestMovies = bestImdb.results
    const imgBest = bestMovies.results[0]["image_url"];
    const titleBest = bestMovies.results[0]["title"];
    const descriptionBest = bestMovies.results[0]["genres"] + ", " + bestMovies.results[0]["year"];
    //console.log(img)


    const bestMovieDiv = document.getElementById("best-movie");
    const bestMovieTitle = document.getElementById("best-title");
    const bestMovieDescription = document.getElementById("best-description");

    bestMovieDiv.style.background = `url(${imgBest}) no-repeat`;
    bestMovieDiv.style.backgroundSize = `cover`;
    bestMovieTitle.innerHTML = titleBest;
    bestMovieDescription.innerHTML = descriptionBest;
    //bestMovieDiv.style.backgroundSize = `${bestMovieDiv.getBoundingClientRect()['width']}px ${bestMovieDiv.getBoundingClientRect()['height']}px `;
    //console.log(bestMovieDiv.getBoundingClientRect())
    //console.log(bestMovieDiv.getBoundingClientRect()['width'])
    //console.log(bestMovieDiv.getBoundingClientRect()['height'])


    const cat1 = await get_info("genre", `${category1}`);
    const cat1Movies = cat1.results.slice(0, 7);
    // console.log(cat1.results);

    const cat2 = await get_info("genre", `${category2}`);
    const cat2Movies = cat2.results.slice(0, 7);
    // console.log(cat2.results);

    const cat3 = await get_info("genre", `${category3}`);
    const cat3Movies = cat3.results.slice(0, 7);
    // console.log(cat3.results);

    return [bestMovies, cat1Movies, cat2Movies, cat3Movies];
}

const apiCall = main();



const bestMovies = apiCall[0];
const cat1Movies = apiCall[1];
const cat2Movies = apiCall[2];
const cat3Movies = apiCall[3];

for (let i of vignettes_num) {
    const vignette = document.getElementById(`img1.${i}`);
    const imgUrl = bestMovies[i]["image_url"];
    const title = bestMovies[i]["title"];
    vignette.setAttribute("src", imgUrl);
    vignette.setAttribute("alt", title);
}