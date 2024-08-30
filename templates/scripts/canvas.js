const canvas = document.getElementById("img");
const ctx = canvas.getContext("2d");

function drawRect(x, y, w = 1, clr = "#ffffff") {
  ctx.fillStyle = clr;
  ctx.fillRect(x, y, w, w);
}

var pressed = false;
canvas.addEventListener("mousedown", function () {
  pressed = true;
});
canvas.addEventListener("mouseup", function () {
  pressed = false;
});
canvas.addEventListener("mouseleave", function () {
  pressed = false;
});

canvas.addEventListener("mousemove", function (e) {
  if (pressed) {
    console.log("draw");
  }
});
