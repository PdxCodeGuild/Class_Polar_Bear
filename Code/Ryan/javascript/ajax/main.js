
// Option 1 use then
// axios({
//     method: 'get',
//     // method: 'post', can be used to push to django
//     url: 'https://api.chucknorris.io/jokes/random'
// }).then(function (response) {
//     // console.log(response.data.value)
//     const p = document.querySelector('#joke')
//     p.textContent = response.data.value
// })

// Option 2 create a function that stops and waits
async function searchJoke(search) {
    const response = await axios({
        method: 'get',
        url: 'https://api.chucknorris.io/jokes/search',
        params: {
            query: search
        }
    })
    // const p = document.querySelector('#joke')
    // p.textContent = response.data.result[0].value
    // console.log(response)
    return response.data.result 
}

// searchJoke()

const searchInput = document.querySelector('#search-input')

const searchBtn = document.querySelector('#search-button')

searchBtn.addEventListener('click', async function(){
    const div = document.querySelector('#joke')
    div.innerHTML = 'loading....'
    let searchValue = searchInput.value
    // searchJoke(searchValue)
    console.log(searchValue)


    const jokes = await searchJoke(searchValue)
    div.innerHTML = ''
    for (let i = 0; i < jokes.length; i++){
        let p = document.createElement('p')
        p.textContent = jokes[i].value
        div.append(p)
    }
    searchInput.value = ''
})