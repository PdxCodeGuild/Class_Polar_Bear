const url = `https://goweather.herokuapp.com/weather/Portland`

axios({
    method: 'get',
    url : url,
   
}).then(function (response) {
    console.log(response)
})