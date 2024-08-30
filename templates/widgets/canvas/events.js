//EVENTS

//drawing
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


//resize
window.addEventListener("resize", () => {
  canvas.width = window.innerWidth * 0.92;
  canvas.height = canvas.width;

  clearCnv();
});
