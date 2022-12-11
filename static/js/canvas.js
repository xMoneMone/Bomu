/**
 * @type HTMLCanvasElement
 */
const canvas = document.getElementById("canvas");
const guide = document.getElementById("guide");
const toggleGuide = document.getElementById("toggleGuide");

const drawingContext = canvas.getContext("2d");

const color1 = document.getElementById("color1");
const color2 = document.getElementById("color2");
const color3 = document.getElementById("color3");
const color4 = document.getElementById("color4");
const color5 = document.getElementById("color5");
const color6 = document.getElementById("color6");
const color7 = document.getElementById("color7");
const color8 = document.getElementById("color8");
const color9 = document.getElementById("color9");
const color10 = document.getElementById("color10");
const color11 = document.getElementById("color11");
const color12 = document.getElementById("color12");

const colours = ["#ffffff", "#a0e0d2", "#99ccd1", "#9aacc4", "#8e94b4", "#878bbb",
                 "#71639c", "#e382af", "#fb9faa", "#ffc2ad", "#e4adbe", "#673e4a"]

const colourElemets = [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12]

const PIXEL_CANVAS_SIZE = 32;
const pixelLength = canvas.width / PIXEL_CANVAS_SIZE;

let color = '#8e94b4';
let mouseFlag = false;

// canvas initial settings
drawingContext.fillStyle = "#ffffff";
drawingContext.fillRect(0, 0, canvas.width, canvas.height);

{
    guide.style.width = `${canvas.width}px`;
    guide.style.height = `${canvas.height}px`;
    guide.style.gridTemplateColumns = `repeat(${PIXEL_CANVAS_SIZE}, 1fr)`;
    guide.style.gridTemplateRows = `repear(${PIXEL_CANVAS_SIZE}, 1fr)`;

    [...Array(PIXEL_CANVAS_SIZE ** 2)].forEach(() => guide.insertAdjacentHTML("beforeend", "<div></div>"));
}

function handleCanvasMousemove(e) {
    if (mouseFlag == false){
        return;
    }

    const canvasBoundingRect = canvas.getBoundingClientRect();
    const x = e.clientX - canvasBoundingRect.left;
    const y = e.clientY - canvasBoundingRect.top;
    const cellX = Math.floor(x / pixelLength);
    const cellY =  Math.floor(y / pixelLength);

    fillCell(cellX, cellY);
}

function handleToggleGuideChange() {
    guide.style.display = toggleGuide.checked ? null : "none";
}

function fillCell(cellX, cellY) {
    const startX = cellX * pixelLength;
    const startY = cellY * pixelLength;

    drawingContext.fillStyle = color;
    drawingContext.fillRect(startX, startY, pixelLength, pixelLength);
}

function changeMousedownFlag(e) {
    if (e.button !== 0) {
        mouseFlag = false;
        return;
    }

    const canvasBoundingRect = canvas.getBoundingClientRect();
    const x = e.clientX - canvasBoundingRect.left;
    const y = e.clientY - canvasBoundingRect.top;
    const cellX = Math.floor(x / pixelLength);
    const cellY =  Math.floor(y / pixelLength);

    fillCell(cellX, cellY);

    mouseFlag = true;
}

color1.style.backgroundColor = colours[0]
color2.style.backgroundColor = colours[1]
color3.style.backgroundColor = colours[2]
color4.style.backgroundColor = colours[3]
color5.style.backgroundColor = colours[4]
color6.style.backgroundColor = colours[5]
color7.style.backgroundColor = colours[6]
color8.style.backgroundColor = colours[7]
color9.style.backgroundColor = colours[8]
color10.style.backgroundColor = colours[9]
color11.style.backgroundColor = colours[10]
color12.style.backgroundColor = colours[11]

function changeMouseupFlag(e) {
    mouseFlag = false;
}

function changeColor1() {
    color = colours[0]
}

function changeColor2() {
    color = colours[1]
}

function changeColor3() {
    color = colours[2]
}

function changeColor4() {
    color = colours[3]
}

function changeColor5() {
    color = colours[4]
}

function changeColor6() {
    color = colours[5]
}

function changeColor7() {
    color = colours[6]
}

function changeColor8() {
    color = colours[7]
}

function changeColor9() {
    color = colours[8]
}

function changeColor10() {
    color = colours[9]
}

function changeColor11() {
    color = colours[10]
}

function changeColor12() {
    color = colours[11]
}

canvas.addEventListener("pointermove", handleCanvasMousemove);
canvas.addEventListener("pointerdown", changeMousedownFlag);
document.body.addEventListener("pointereup", changeMouseupFlag);

canvas.addEventListener("mousemove", handleCanvasMousemove);
canvas.addEventListener("mousedown", changeMousedownFlag);
document.body.addEventListener("mouseup", changeMouseupFlag);

toggleGuide.addEventListener("change", handleToggleGuideChange);

color1.addEventListener("click", changeColor1);
color2.addEventListener("click", changeColor2);
color3.addEventListener("click", changeColor3);
color4.addEventListener("click", changeColor4);
color5.addEventListener("click", changeColor5);
color6.addEventListener("click", changeColor6);
color7.addEventListener("click", changeColor7);
color8.addEventListener("click", changeColor8);
color9.addEventListener("click", changeColor9);
color10.addEventListener("click", changeColor10);
color11.addEventListener("click", changeColor11);
color12.addEventListener("click", changeColor12);


let post_button = document.getElementById('post-canvas')
post_button.addEventListener('click', function(){
    window.sessionStorage.setItem('drawing', canvas.toDataURL())
    console.log('worketh')
});
