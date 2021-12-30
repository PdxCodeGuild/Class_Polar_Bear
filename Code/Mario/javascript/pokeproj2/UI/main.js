const app = new Vue({
  el: "#app",
  data: {
    message: "Hello World",
  },
  method: {},
  created: function () {
    axios({
      method: "GET",
      url: "http://127.0.0.1:8000/pokemon/",
    }).then(function (e) {
      console.log(e);
    });
  },
});
