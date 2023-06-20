const category1 = "Comedy";
const category2 = "Romance";
const category3 = "Action";
const vignettes_num = [1, 2, 3, 4,];


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
    async function get_info_page2(parameter, value) {
        const responseRaw = await fetch(`${apiUrl}/?${parameter}=${value}&page=2`);
        if (responseRaw.ok === true) {
            const responseJson = await responseRaw.json();
            return responseJson;
        }
        throw new Error("Oops !")

    }
    async function get_details(id) {
        const responseRaw = await fetch(`${apiUrl}/${id}`);
        if (responseRaw.ok === true) {
            const responseJson = await responseRaw.json();
            return responseJson;
        }
        throw new Error("Oops !")

    }

    const bestImdb = await get_info("sort_by", "-imdb_score");
    const bestMovies = bestImdb.results
    const imgBest = bestMovies[0]["image_url"];
    const titleBest = bestMovies[0]["title"];
    const genreBest = bestMovies[0]["genres"] + ", " + bestMovies[0]["year"];
    const bestDetails = await get_details(bestMovies[0]["id"]);
    const descriptionBest = bestDetails["description"];
    //console.log(img)

    const bestImdb2 = await get_info_page2("sort_by", "-imdb_score");
    const bestMovies2 = bestImdb2.results


    const bestMovieDiv = document.getElementById("best-movie");
    const bestMovieTitle = document.getElementById("best-title");
    const bestMovieGenre = document.getElementById("best-genre");
    const bestMovieDescription = document.getElementById("best-description");

    bestMovieDiv.style.background = `url(${imgBest}) no-repeat`;
    bestMovieDiv.style.backgroundSize = `cover`;
    bestMovieTitle.innerHTML = titleBest;
    bestMovieGenre.innerHTML = genreBest;
    bestMovieDescription.innerHTML = descriptionBest;
    //bestMovieDiv.style.backgroundSize = `${bestMovieDiv.getBoundingClientRect()['width']}px ${bestMovieDiv.getBoundingClientRect()['height']}px `;
    //console.log(bestMovieDiv.getBoundingClientRect())
    //console.log(bestMovieDiv.getBoundingClientRect()['width'])
    //console.log(bestMovieDiv.getBoundingClientRect()['height'])


    const cat1 = await get_info("genre", `${category1}`);
    const cat1Movies = cat1.results;
    // console.log(cat1Movies);

    const cat2 = await get_info("genre", `${category2}`);
    const cat2Movies = cat2.results;
    // console.log(cat2Movies);

    const cat3 = await get_info("genre", `${category3}`);
    const cat3Movies = cat3.results;
    // console.log(cat3Movies);

    const cat1_p2 = await get_info_page2("genre", `${category1}`);
    const cat1Movies_p2 = cat1_p2.results;
    // console.log(cat1Movies_p2);

    const cat2_p2 = await get_info_page2("genre", `${category2}`);
    const cat2Movies_p2 = cat2_p2.results;
    // console.log(cat2Movies_p2);

    const cat3_p2 = await get_info_page2("genre", `${category3}`);
    const cat3Movies_p2 = cat3_p2.results;
    // console.log(cat3Movies_p2);


    for (let i of [1, 2, 3, 4]) {
        const labels = [bestMovies, cat1Movies, cat2Movies, cat3Movies]
        for (let j of vignettes_num) {
            const vignette = document.getElementById(`img${i}.${j}`);
            const imgUrl = labels[i - 1][j]["image_url"];
            const id = labels[i - 1][j]["id"];
            vignette.setAttribute("src", imgUrl);
            vignette.setAttribute("alt", id);
        }
    }
    for (let i of [1, 2, 3, 4]) {
        const labels = [bestMovies2, cat1Movies_p2, cat2Movies_p2, cat3Movies_p2]
        for (let j of [5, 6, 7]) {
            const vignette = document.getElementById(`img${i}.${j}`);
            const imgUrl = labels[i - 1][j - 4]["image_url"];
            const id = labels[i - 1][j - 4]["id"];
            vignette.setAttribute("src", imgUrl);
            vignette.setAttribute("alt", id);
        }
    }

    // Fenêtre modale - contenu

}

main();
//const modalWindow = document.querySelector("#modal-window");
console.log("Goodbye");


