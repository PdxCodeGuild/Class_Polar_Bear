url = "https://favqs.com/api/qotd";

const response = function () {
  let quotesDiv = document.querySelector("#quotes");
  let res = "";
  axios({
    method: "GET",
    url: url,
  }).then(({ data }) => {
    let author = data.quote.author;
    let quote = data.quote.body;
    let li = document.createElement("li");
    li.textContent = `${author}: ${quote}`;
    li.classList.add("fade-in");
    quotesDiv.append(li);
    console.log(`${author}: ${quote}`);
  });
};
let i = 0;
for (i; i < 4; i++) {
  response();
}
