let elements;
window.onload = function () {
  elements = {
    url: document.getElementById("url"),
    id: document.getElementById("id"),
    pwd: document.getElementById("pwd"),
    res: document.getElementById("res"),
  };
};
function submit() {
  eel.post(elements.url.value, {
    id: elements.id.value,
    pwd: elements.pwd.value,
  });
}
function showRes(text) {
  elements.res.innerHTML = text;
}
eel.expose(showRes);
