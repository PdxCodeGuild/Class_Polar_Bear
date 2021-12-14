

// axios({
//     method: 'get',
//     url: 'https://api.dictionaryapi.dev/api/v2/entries/en/hello'
// }).then(function(llama) {
//     console.log(llama)
// })

const input = document.querySelector('#word')
const pTag = document.querySelector('#definition')

input.addEventListener('keypress', function(event){
    if(event.key === 'Enter'){
        axios({
            method: 'get',
            url: `https://api.dictionaryapi.dev/api/v2/entries/en/${input.value}`
        }).then(function (response) {
            pTag.textContent = response.data[0].meanings[0].definitions[0].definition
        })
    }
})