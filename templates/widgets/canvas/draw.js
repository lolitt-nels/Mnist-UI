// Function to start drawing
function down(e) {
  isDrawing = true;
  if (e.type.includes("touch")) {
    lastX = e.touches[0].pageX - canvas.getBoundingClientRect().left;
    lastY = e.touches[0].pageY - canvas.getBoundingClientRect().top;
  } else {
    [lastX, lastY] = [e.offsetX, e.offsetY];
  }
}

// Function to draw on the canvas
function move(e) {
  if (!isDrawing) return;

  ctx.beginPath();
  ctx.moveTo(lastX, lastY);

  var toX = e.offsetX;
  var toY = e.offsetY;

  if (e.type.includes("touch")) {
    toX = e.touches[0].pageX - canvas.getBoundingClientRect().left;
    toY = e.touches[0].pageY - canvas.getBoundingClientRect().top;
  }

  ctx.lineTo(toX, toY);

  ctx.stroke();

  [lastX, lastY] = [toX, toY];
}

// Function to stop drawing
function up() {
  isDrawing = false;
}

// Function to clear the canvas

function clearCnv() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}
