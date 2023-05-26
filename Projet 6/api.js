const apiUrl = "http://localhost:8000/api/v1/titles";
let parameters = "";

const response = await fetch(`${apiUrl}/${parameters}`);

const imageFrame = document.getElementById("img1.1");
imageFrame.src = '';