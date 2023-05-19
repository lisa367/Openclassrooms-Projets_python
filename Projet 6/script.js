var arrowLeft = document.getElementsByClassName("arrow-left");
var arrowRight = document.getElementsByClassName("arrow-right");

var body = document.getElementsByTagName("body")

var cadreImg = document.getElementsByClassName("cadre-img");

function changeBackgroundColor() {
    body.style.backgroundColor = "pink"
};

arrowRight.onclick = changeBackgroundColor();