const $quoteAuthor = document.querySelector('#quote-author')
const $quoteBody = document.querySelector('#quote-body')
const $newQuoteBtn = document.querySelector('#new-quote-btn')

$newQuoteBtn.addEventListener('click',function(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api/qotd'
    }).then(response => {
        const author = response.data.quote.author
        const body = response.data.quote.body
        $quoteAuthor.textContent = `- ${author}`
        $quoteBody.textContent = body
    })
})