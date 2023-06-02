const apiUrl = "http://localhost:8000/api/v1/titles";
let parameters = "";
// console.log("Hello"

async function get_info(parameter, value) {
    const responseRaw = await fetch(`${apiUrl}/${parameter}=${value}`);
    if (responseRaw.ok === true) {
        const responseJSON = responseRaw.json();
        return response
    }
    // else { const response404 = "Oops !"; return response404 }
    throw new Error("Oops !")

}
const best_movie = get_info("genre", "Romance");
console.log(best_movie);

// const imageFrame = document.getElementById("img1.1");
// imageFrame.src = '';

