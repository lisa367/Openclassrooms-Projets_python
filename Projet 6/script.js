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
// const div = document.querySelector(".movies-images");


function changeBackgroundColor() {
    bdy.style.backgroundColor = "pink";
}
function revertBackgroundColor() {
    bdy.style.backgroundColor = "black";
}
function random(number) {
    return Math.floor(Math.random() * (number + 1));
}
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
    // console.log(ori
    // console.log(cadreImg[i].getBoundingClientRect())
}

// arrowsRight[0].onclick = moveRight;
// arrowsLeft[0].onclick = moveLeft;
for (let i of [0, 1, 2, 3]) {
    arrowsRight[i].onclick = function () {
        moveRight(i)

    };
    arrowsLeft[i].onclick = function () {
        moveLeft(i);
    };
}



function scrollLeft(arrow) {
    const i = document.id;
    const index = parseInt(i);

}

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

arrowsRight[0].onclick = function () {
        //.forEach(element => {
            element.style.transition = "1s";
            element.style.transform = "translateX(-5rem)";})//
            div.style.transition = "1s";
            div.style.transform = "translateX(5rem)";
    
        };
arrowsLeft[0].onclick = function () {
        //vignettes.forEach(element => {
            element.style.transition = "1s";
            element.style.transform = "translateX(-5rem)";
            })//
            div.style.transition = "1s";
            div.style.transform = "translateX(-5rem)";
        };
    }

*/
