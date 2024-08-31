const canvas = document.getElementById("img");

//canvas size
canvas.width = window.innerWidth * 0.92;
if (canvas.width > 560) canvas.width = 560;

canvas.height = canvas.width;

const ctx = canvas.getContext("2d");



let isDrawing = false;
let lastX = 0;
let lastY = 0;
