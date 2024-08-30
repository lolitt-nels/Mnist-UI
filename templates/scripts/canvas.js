// script.js
const canvas = document.getElementById("img");

canvas.width = window.innerWidth * 0.92;
canvas.height = canvas.width;

const ctx = canvas.getContext("2d");

//line style
ctx.strokeStyle = "#ffffff";
ctx.lineWidth = 40;

let isDrawing = false;
let lastX = 0;
let lastY = 0;

// Function to start drawing
function down(e) {
  isDrawing = true;
  [lastX, lastY] = [e.offsetX, e.offsetY];
}

// Function to draw on the canvas
function move(e) {
  if (!isDrawing) return;

  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(e.offsetX, e.offsetY);
  ctx.stroke();

  [lastX, lastY] = [e.offsetX, e.offsetY];
}

// Function to stop drawing
function up() {
  isDrawing = false;
}

canvas.addEventListener("mousedown", (e) => {
  down(e);
});
canvas.addEventListener("touchstart", (e) => {
  down(e);
});

canvas.addEventListener("mousemove", (e) => {
  move(e);
});
canvas.addEventListener("touchmove", (e) => {
  move(e);
});

canvas.addEventListener("mouseup", () => {
  up();
});
canvas.addEventListener("touchend", () => {
  up();
});
// Function to clear the canvas
document.getElementById("clear").addEventListener("click", () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
});
