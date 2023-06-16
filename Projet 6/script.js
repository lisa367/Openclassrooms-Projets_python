const arrowsLeft = document.querySelectorAll(".arrow-left");
const arrowsRight = document.querySelectorAll(".arrow-right");


const cadreImg = document.querySelectorAll(".cadre-img");
const vignettes = document.querySelectorAll(".vignette");
const modalWindow = document.getElementById("modal-window");
const closeButton = document.getElementById("close-button");
// const div = document.querySelector(".movies-images");

// Horizontal scrolling
function moveRight(i) {
    const originalX = cadreImg[i].getBoundingClientRect()["x"];
    let newX = originalX;
    // console.log(cadreImg[i].getBoundingClientRect())
    cadreImg[i].style.transition = "1.5s";
    cadreImg[i].style.transform = `translateX(${newX + (5 * 12)}px)`;
    newX += (5 * 16);
    // console.log(originalX);
    //console.log(newX);
    // console.log(cadreImg[i].getBoundingClientRect())
}
function moveLeft(i) {
    // console.log(cadreImg[i].getBoundingClientRect())
    const originalX = cadreImg[i].getBoundingClientRect()["x"];
    let newX = originalX;
    // console.log(cadreImg[i].getBoundingClientRect())
    cadreImg[i].style.transition = "1.5s";
    cadreImg[i].style.transform = `translateX(-${newX + (5 * 12)}px)`;
    newX -= (5 * 16);
    // console.log(cadreImg[i].getBoundingClientRect())
}

for (let i of [0, 1, 2, 3]) {
    arrowsRight[i].onclick = function () {
        moveRight(i)

    };
    arrowsLeft[i].onclick = function () {
        moveLeft(i);
    };
}


// Toggle modal window visibility
function displayModalWindow() {
    modalWindow.setAttribute("class", "modal-visible");
}
function closeModalWindow() {
    modalWindow.setAttribute("class", "modal-hidden");
}

function getVignetteData(vignette){
    title = vignette.getAttribute("alt");
    img = vignette.getAttribute("src");
    titleUrl = title.replace(" ", "+");
    let vignetteData = fetch(`http://localhost:8000/api/v1/titles/?title=${titleUrl}`)
    if (vignetteData) {

    }
}
closeButton.onclick = closeModalWindow;
vignettes.forEach(element => {
    element.onclick = displayModalWindow;
})

/*
// document.getElementById("img1.1").style.backgroundColor = "blue";
// document.querySelector("h1").innerHTML = "Hello";
// document.querySelector("h1").style.color = "blue";

const bdy = document.querySelector("body");
const btn = document.getElementsByTagName("button")[0];
// bdy.style.backgroundColor = "blue";
// btn.style.backgroundColor = "pink";
arrowLeft.style.color = "red";

function changeBackgroundColor() {
    bdy.style.backgroundColor = "pink";
}
function revertBackgroundColor() {
    bdy.style.backgroundColor = "black";
}
function random(number) {
    return Math.floor(Math.random() * (number + 1));
}

btn.addEventListener("click", () => {
    const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
    bdy.style.backgroundColor = rndCol;
});
// arrowsRight[0].onclick = moveRight;
// arrowsLeft[0].onclick = moveLeft;

function left(value, index, array) {
    arrowsLeft[index].onclick = revertBackgroundColor;
}
function right(value, index, array) {
    array[index].onclick = changeBackgroundColor;
}
arrowsLeft.forEach(element => {
    // element.onclick = revertBackgroundColor;
    console.log(element.innerHTML)
});



function scrollLeft(arrow) {
    const i = document.id;
    const index = parseInt(i);

}

*/

