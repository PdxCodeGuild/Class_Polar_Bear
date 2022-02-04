// Use the favqs.com api to show a random quote. To start, use https://favqs.com/api/qotd to GET a quote, then display it on the page.

// {
//   "id": 4,
//   "author": "Albert Einstein",
//   "body": "Make everything as simple as possible, but not simpler.",
//   ...
// }

const quoteText = document.getElementById('quote_text')
const quoteAuthor = document.getElementById('quote_author')
const APIurl = 'https://favqs.com/api/qotd'


axios({
    method: 'get',
    url: APIurl
}).then(response => {
    console.log(response.data.quote)
    let author = response.data.quote.author
    quoteAuthor.textContent = author
    let text = response.data.quote.body
    quoteText.textContent = text
})

