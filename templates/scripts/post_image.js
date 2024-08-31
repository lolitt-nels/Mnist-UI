//needs the post.js

async function postImage(id) {
  var digit = await post("http://127.0.0.1:8000", {})
  console.log(digit)
}
