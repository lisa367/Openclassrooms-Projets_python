const apiUrl = "http://localhost:8000/api/v1/titles";
const apiTest = "https://jsonplaceholder.typicode.com/users"

console.log("Hello");

async function get_info(parameter, value) {
    const responseRaw = await fetch(`${apiUrl}/?${parameter}=${value}`);
    if (responseRaw.ok === true) {
        return responseRaw.json();
    }
    // else { const response404 = "Oops !"; return response404 }
    throw new Error("Oops !")

}

const test = get_info("sort_by", "imdb_score");
console.log(test);


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
const best_movie = get_info("genre", "Romance");
console.log(best_movie);
*/

// const imageFrame = document.getElementById("img1.1");
// imageFrame.src = '';

