// document.getElementById("img1.1").style.backgroundColor = "blue";
// document.querySelector("h1").innerHTML = "Hello";
// document.querySelector("h1").style.color = "blue";
const arrowLeft = document.querySelector(".arrow-left");
const arrowRight = document.querySelector(".arrow-right");

const bdy = document.querySelector("body");
const btn = document.getElementsByTagName("button");
// bdy.style.backgroundColor = "blue";


const cadreImg = document.getElementsByClassName("cadre-img");

function changeBackgroundColor() {
    bdy.style.backgroundColor = "pink";
}
function revertBackgroundColor() {
    bdy.style.backgroundColor = "pink";
}
function random(number) {
    return Math.floor(Math.random() * (number + 1));
}

arrowRight.onclick = changeBackgroundColor;
arrowLeft.onclick = revertBackgroundColor;


btn.addEventListener("click", () => {
    const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
    bdy.style.backgroundColor = rndCol;
});

arrowLeft.style.color = "red";