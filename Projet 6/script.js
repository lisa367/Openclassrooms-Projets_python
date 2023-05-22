// document.getElementById("img1.1").style.backgroundColor = "blue";
// document.querySelector("h1").innerHTML = "Hello";
// document.querySelector("h1").style.color = "blue";
const arrowLeft = document.getElementsByClassName("arrow-left")[0];
const arrowRight = document.querySelectorAll(".arrow-right")[0];

const bdy = document.querySelector("body");
const btn = document.getElementsByTagName("button");
// bdy.style.backgroundColor = "blue";
// btn.style.backgroundColor = "pink";


const cadreImg = document.getElementsByClassName("cadre-img");

function changeBackgroundColor() {
    bdy.style.backgroundColor = "pink";
}
function revertBackgroundColor() {
    bdy.style.backgroundColor = "black";
}
function random(number) {
    return Math.floor(Math.random() * (number + 1));
}

arrowRight.onclick = changeBackgroundColor;
arrowLeft.onclick = revertBackgroundColor;
arrowLeft.style.color = "red";


btn.addEventListener("click", () => {
    const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
    bdy.style.backgroundColor = rndCol;
});

