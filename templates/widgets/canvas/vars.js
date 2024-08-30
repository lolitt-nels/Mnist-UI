const canvas = document.getElementById("img");

//canvas size
canvas.width = window.innerWidth * 0.92;
canvas.height = canvas.width;

const ctx = canvas.getContext("2d");

//line style
ctx.strokeStyle = "#ffffff";
ctx.lineWidth = canvas.width / 10;

let isDrawing = false;
let lastX = 0;
let lastY = 0;
