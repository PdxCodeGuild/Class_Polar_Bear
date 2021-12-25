

const url = 'https://goweather.herokuapp.com/weather/Curitiba'

axios({
    method: 'get',
    url: url,

}).then(function (response){
    console.log(response)
})