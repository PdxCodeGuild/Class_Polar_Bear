// const url = ' https://cat-fact.herokuapp.com/facts'

const url = 'https://www.metaweather.com/api/location/search/'

axios({
    method: 'get',
    url: url,
    params: {
        query: 'Portland'
    }
}).then(function (response){
    console.log(response)
})