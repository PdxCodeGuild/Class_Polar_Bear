/*
Use the favqs.com api to show a random quote. 
To start, use https://favqs.com/api/qotd to GET a quote, 
then display it on the page.

{
  "id": 4,
  "author": "Albert Einstein",
  "body": "Make everything as simple as possible, but not simpler.",
  ...
}
*/

/*
axios({
    method: 'get',
    url: 'https://favqs.com/api/qotd',

}).then((function(simple) {
    console.log(simple)
})) 
*/

/* Solution from https://gist.github.com/prameshbajra/2196fc4071604e37d842148956b18aa9

fetch("https://favqs.com/api/qotd")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        let quote = data.quote.body;
        console.log(data.quote);
        document.write(`${quote} by ${data.quote.author}`);
    })
    .catch((error) => {
        console.log(error);
    });
    
*/

/* Test
axios({
    method: 'get',
    url: 'https://favqs.com/api/qotd'
}).then((response) => {
    console.log(response.data)
})
*/


axios({
    method: 'get',
    url: 'https://favqs.com/api/qotd',
    params: {
        id: 3,
    } 
    }).then((response) => {
        //console.log(response.data)
        /* let quotation = data.quote.body;
        document.write(`${quote} by ${data.quote.author}`); */
        console.log(response.data.quote)
        let quote = response.data.quote.body
        document.write(`"${quote}" <br><br> -${response.data.quote.author}`)
})

/* ask how to pass quote into ID tag */