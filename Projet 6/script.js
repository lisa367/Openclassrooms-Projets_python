// document.getElementById("img1.1").style.backgroundColor = "blue";
// document.querySelector("h1").innerHTML = "Hello";
// document.querySelector("h1").style.color = "blue";
const arrowLeft = document.getElementsByClassName("arrow-left");
const arrowRight = document.getElementsByClassName("arrow-right");

const body = document.getElementsByTagName("body");

const cadreImg = document.getElementsByClassName("cadre-img");

function changeBackgroundColor() {
    body.style.backgroundColor = "pink";
}

arrowRight.onclick = changeBackgroundColor();
const btn = document.getElementsByTagName("button");

function random(number) {
    return Math.floor(Math.random() * (number + 1));
}

btn.addEventListener("click", () => {
    const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
    body.style.backgroundColor = rndCol;
});

arrowLeft.style.color = "red";