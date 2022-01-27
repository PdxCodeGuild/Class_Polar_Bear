const searchForm = document.querySelector("form");
const searchResultDiv = document.querySelector(".search-result");
const container = document.querySelector(".container");
let searchQuery = "";
const APP_ID = "f6839f38";
const APP_key = "40dcaf67897ba82589b8f6fd1855d041";
console.log(container)
searchForm.addEventListener("submit", function (eatz) {
  eatz.preventDefault();
  searchQuery = eatz.target.querySelector("input").value;
  fetchAPI();
});

async function fetchAPI() {
  const baseURL = `https://api.edamam.com/search?q=${searchQuery}&app_id=${APP_ID}&app_key=${APP_key}&from=0&to=20`;
  const response = await fetch(baseURL);
  const data = await response.json();
  easyFixHTML(data.hits);
  console.log(data);
}


function easyFixHTML(results) {
  container.classList.remove("initial");
  let generatedHTML = "";
  results.map(function (result) {
    generatedHTML += `
      <div class="item">
        <img src="${result.recipe.image}" alt="img">
        <div class="flex-container">
          <h1 class="title">${result.recipe.label}</h1>
          <a class="view-btn" target="_blank" href="${
            result.recipe.url
          }">View Recipe</a>
          <br>
          <a class="view-btn" target="_blank" href="https://www.youtube.com/results?search_query=How+to+make+${result.recipe.label}">See How it's Made</a>
        </div>
        <p class="item-data">Calories: ${result.recipe.calories.toFixed(2)}</p>
        <p class="item-data">Diet label: ${
          result.recipe.dietLabels.length > 0
            ? result.recipe.dietLabels
            : "No Data Found"
        }</p>
        <p class="item-data">Health labels: ${result.recipe.healthLabels}</p>
      </div>
    `;
  });
  searchResultDiv.innerHTML = generatedHTML;
