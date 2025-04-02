// Initialize the canvas and context
function initializeCanvas(canvasId, sz) {
  const canvas = document.getElementById(canvasId);
  canvas.width = sz;
  canvas.height = sz;
  const ctx = canvas.getContext("2d");
  return { canvas, ctx };
}

const { canvas, ctx } = initializeCanvas(
  "img",
  window.innerWidth * 0.92 > 560 ? 560 : window.innerWidth * 0.92
);

// CLEAR
function clearCnv() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

//
const unit = canvas.width / 28;

// DRAWING
function draw_square(i, j, around = 0.5) {
  i = parseInt(i);
  j = parseInt(j);

  ctx.fillStyle = "#ffffff";
  around = parseInt(around * unit);

  // Calculate the position based on the brush thickness
  let x = parseInt(i * unit) - around;
  let y = parseInt(j * unit) - around;

  // Draw a square with the specified brush thickness
  ctx.fillRect(x, y, unit + around * 2, unit + around * 2);
}

// EVENTS
var pressed = false;

canvas.addEventListener("mousedown", function (e) {
  pressed = true;
});

canvas.addEventListener("mouseup", function (e) {
  pressed = false;
});

//DRAW
canvas.addEventListener("mousemove", function (e) {
  if (pressed) {
    const rect = canvas.getBoundingClientRect(); // Get canvas position relative to the viewport

    var x = event.clientX - rect.left; // Calculate X relative to the canvas
    var y = event.clientY - rect.top; // Calculate Y relative to the canvas

    x /= unit;
    y /= unit;

    draw_square(x, y);
  }
});

// TOUCH
canvas.addEventListener("touchstart", function (e) {
  pressed = true;
});

canvas.addEventListener("touchend", function (e) {
  pressed = false;
});

// DRAW
canvas.addEventListener("touchmove", function (e) {
  if (pressed) {
    const rect = canvas.getBoundingClientRect(); // Get canvas position relative to the viewport

    const touch = e.touches[0]; // Get the first touch point
    let x = touch.clientX - rect.left; // Calculate X relative to the canvas
    let y = touch.clientY - rect.top; // Calculate Y relative to the canvas

    x /= unit;
    y /= unit;

    draw_square(x, y);
  }
});
