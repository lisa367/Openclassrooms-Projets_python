// document.getElementById("img1.1").style.backgroundColor = "blue";
// document.querySelector("h1").innerHTML = "Hello";
// document.querySelector("h1").style.color = "blue";
const arrowsLeft = document.querySelectorAll(".arrow-left");
const arrowsRight = document.querySelectorAll(".arrow-right");

const bdy = document.querySelector("body");
const btn = document.getElementsByTagName("button")[0];
// bdy.style.backgroundColor = "blue";
// btn.style.backgroundColor = "pink";


// const cadreImg = document.getElementsByClassName("cadre-img");
const cadreImg = document.querySelectorAll(".cadre-img");
const vignettes = document.querySelectorAll(".vignette");


function changeBackgroundColor() {
    bdy.style.backgroundColor = "pink";
}
function revertBackgroundColor() {
    bdy.style.backgroundColor = "black";
}
function random(number) {
    return Math.floor(Math.random() * (number + 1));
}
function moveRight() {
    cadreImg[0].style.transition = "1s";
    cadreImg[0].style.transform = "translateX(10%)";
}
function moveLeft() {
    cadreImg[0].style.transition = "1s";
    cadreImg[0].style.transform = "translateX(-4%)";
}

// arrowsRight[0].onclick = moveRight;
// arrowsLeft[0].onclick = moveLeft;


arrowsRight[0].onclick = function () {
    let arr = new Array(vignettes.slice(0, 6))
    arr.forEach(element => {
        element.style.transition = "1s";
        element.style.transform = "translateX(20%)";
    })
};
arrowsLeft[0].onclick = function () {
    vignettes.forEach(element => {
        element.style.transition = "1s";
        element.style.transform = "translateX(-5rem)";
    })
};


/*
arrowLeft.style.color = "red";

btn.addEventListener("click", () => {
    const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
    bdy.style.backgroundColor = rndCol;
});
function left(value, index, array) {
    arrowsLeft[index].onclick = revertBackgroundColor;
}
function right(value, index, array) {
    array[index].onclick = changeBackgroundColor;
}
arrowsLeft.forEach(element => {
    // element.onclick = revertBackgroundColor;
    console.log(element.innerHTML)
});*/

// arrowsRight.forEach(right);
//console.log(arrowsLeft)
/*
arrowsLeft.forEach(element => {
    element.onclick = revertBackgroundColor;
});
arrowsRight.forEach(element => {
    element.onclick = changeBackgroundColor;
});

*/
