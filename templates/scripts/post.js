//needs the cookies.js

const CSRF = getCookie("csrftoken");

function post(url, body) {
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify(body),
  }).then((response) => {
    const rslt = response.json()
    console.log(rslt)
    return rslt;
  });
}
