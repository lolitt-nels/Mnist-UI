//needs the post.js

async function postImage(canvas_id) {
  const dataURL = document.getElementById(canvas_id).toDataURL("image/png");

  return await post(URL, {
    img: dataURL,
  });
}
