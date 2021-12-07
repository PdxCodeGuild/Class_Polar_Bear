

// axios({
//   method: 'get',
//   url: 'https://api.chucknorris.io/jokes/random',
// })
//   .then(response => {
//     const p = document.querySelector('#joke');
//     p.textContent = response.data.value;
//   })

// jokes/search
async function searchJoke(search) {
  const response = await axios({
    method: 'get',
    url: `https://api.chucknorris.io/jokes/search`,
    params: {
      query: search
    },
  })
  return response.data.result;
}

const searchInput = document.querySelector('#search-input');
const searchBtn = document.querySelector('#search-button');

searchBtn.addEventListener('click', async function() {
  const ol = document.querySelector('#joke');
  ol.innerHTML = 'loading...';
  let searchValue = searchInput.value;

  const jokes = await searchJoke(searchValue);
  ol.innerHTML = '';
  for(let i = 0; i < jokes.length; i++) {
    let p = document.createElement('li');
    p.textContent = jokes[i].value;
    ol.append(p);
  }
  searchInput.value = '';
})