//needs the cookies.js

const CSRF = getCookie("csrftoken");

async function post(url, body) {
  return fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify(body),
  }).then((response) => {
    return response.json();
  });
}
