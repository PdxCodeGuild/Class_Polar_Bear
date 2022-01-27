// const url = "https://favqs.com/api/qotd";

let quote = document.getElementById("quote");
let author = document.getElementById("author");
let body = document.getElementById("body");
let btn = document.getElementById("btn");



// let getQuote = () => {
//     fetch(url)
//       .then((data) => data.json())
//       .then((item) => {
//         quote.innerText = item.getElementById(quote)
//         author.innerText = item.author
//         body.innerText =item.body
//       });
//   };
function getQuote(){
  fetch("https://favqs.com/api/qotd")
  .then(res => res.json())
  .then(data => {
    quote.innerText = `"$data.content"`
    author.innerText = `"$data.author"`
    body.innerText =   `"$data.content"`


  })



window.addEventListener("load", getQuote);
btn.addEventListener("click", getQuote);

