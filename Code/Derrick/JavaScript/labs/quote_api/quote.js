const $quoteAuthor = document.querySelector('#quote-author')
const $quoteBody = document.querySelector('#quote-body')
const $newQuoteBtn = document.querySelector('#new-quote-btn')

function newQuote() {
    
}

$newQuoteBtn.addEventListener('click',function(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api/qotd'
    }).then(response => {
        let author = response.data.quote.author
        let body = response.data.quote.body
        $quoteAuthor.textContent = `- ${author}`
        $quoteBody.textContent = body
    })
})