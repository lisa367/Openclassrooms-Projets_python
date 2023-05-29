const apiUrl = "http://localhost:8000/api/v1/titles";
let parameters = "";

async function get_info(parameter, value) {
    const response = await fetch(`${apiUrl}/${parameter}=${value}`);
    return response
}

const imageFrame = document.getElementById("img1.1");
imageFrame.src = '';