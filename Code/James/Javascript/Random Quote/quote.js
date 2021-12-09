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

const quotation = document.getElementById('quotation');

axios({
    method: 'get',
    url: 'https://favqs.com/api/qotd',
    }).then((response) => {
        console.log(response.data.quote)
        let quote = response.data.quote.body
        //document.write(`"${quote}" <br><br> -${response.data.quote.author}`)
        let htmlCode= `<p>${quote}<br><br> -${response.data.quote.author}</p>`
        quotation.innerHTML = htmlCode
})

/*
let htmlCode= "`<p>${quote}</p>`"
quotation.innerHTML = htmlCode
*/

/* ask how to pass quote into ID tag */

/*
htmlCode += `<div>
<p>${list}</p>
<button onclick='check(${ind})' >Check</button>
<button onclick='edit(${ind})' >Edit</button>
<button onclick='deleteTodo(${ind})' >Delete</button>
</div>`;
});
listBox.innerHTML = htmlCode;
*/