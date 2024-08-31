//needs images post

async function predict() {
  //get the prediction
  var digit = await postImage("img");
  digit = digit["digit"];

  console.log(digit);

  //update the ui
}
