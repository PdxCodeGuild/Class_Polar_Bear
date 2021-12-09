// random quote lab
// https://github.com/PdxCodeGuild/Class_Polar_Bear/blob/main/4%20JavaScript/labs/04%20Quote%20API.md

const pTag = document.querySelector('#p-tag');

axios ({
    method: 'get',
    url: 'https://favqs.com/api/qotd'
}).then (function (response) {
    pTag.textContent = response.data.quote.body + ' - ' + response.data.quote.author
})