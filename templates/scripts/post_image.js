//needs the post.js

async function postImage(canvas_id) {
  const dataURL = document.getElementById(canvas_id).toDataURL("image/png");

  return await post("http://127.0.0.1:8000", {
    img: dataURL,
  });
}
