

const api_key = '425b88e699d1373935dc7514b04c0789'

const ip_url = `https://geo.ipify.org/api/v1?apiKey=at_AbJukDnWyQmU96rap3o5IZS0m1zOl`
axios({
    method: 'get',
    url: ip_url
}).then(function (response) {
    const lat = response.data.location.lat
    const lng = response.data.location.lng

    axios({
        method: 'get',
        url: 'https://api.openweathermap.org/data/2.5/weather',
        // ?lat={lat}&lon={lon}&appid={API key}
        params: {
            lat: lat,
            lon: lng,
            appid: api_key,
            units: 'imperial'
        }
    }).then(function(response){
        console.log(response)
    })
})