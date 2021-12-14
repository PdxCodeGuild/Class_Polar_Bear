const url = `https://favqs.com/api/qotd`;
const p = document.querySelector('#quote');
const a = document.querySelector('#author')

axios.get(url, {
  params: {}
})
.then((res) => {
  let response = res.data.quote;
  if (p && a) {
    console.log(response)
    p.textContent = response.body;
    a.textContent = `- ${response.author}`;
  }
})
.catch((err) => {
  console.log(err)
})
