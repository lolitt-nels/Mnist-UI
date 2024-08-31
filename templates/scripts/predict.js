//needs images post

async function predict(btn) {
  //get the prediction
  var digit = await postImage("img");
  digit = digit["digit"];

  console.log(digit);
  
  btn.innerText = `${digit}`
  //update the ui
}
