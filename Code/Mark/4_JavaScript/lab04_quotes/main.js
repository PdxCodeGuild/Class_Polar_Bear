const $quote = document.querySelector('#quote-body')
const $quote_author = document.querySelector('#quote-author')
const $quote_button = document.querySelector('#new-quote-btn')

$quote_button.addEventListener('click', function(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api/qotd'
    }).then(response => {
        const author = response.data.quote.author
        const text = response.data.quote.body
	$quote.textContent = text
        $quote_author.textContent = `${author}`
    })
})

