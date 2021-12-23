const url = `https://stats.nba.com/stats/leagueleaders`;

axios({
  method: 'get',
  url: url
})
.then(function (response) {
  console.log(response)
})