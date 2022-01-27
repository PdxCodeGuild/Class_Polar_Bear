function renderQuote(quoteObj) {
    console.log(quoteObj);
    document.querySelector('.quote-title').innerHTML = `<a href="${quoteObj.url}" target="_blank">
        “${ quoteObj.body }”
    </a>`;
    document.querySelector('.quote-author').innerHTML = quoteObj.author
}

function loadQuote() {
    fetch('https://favqs.com/api/qotd').then(data => data.json())
        .then(data => renderQuote(data && data.quote ? data.quote : {}))
        .catch(() => alert('Sorry, please try later.'));
}

window.onload = loadQuote;