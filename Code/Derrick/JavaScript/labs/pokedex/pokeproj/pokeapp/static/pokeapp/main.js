const app = new Vue({
  el: "#app",
  delimiters: ["[[", "]]"],
  data: {
    message: "Yellope",
    pokedex: {},
    search: "",
  },
  methods: {
    findPokemon() {},
  },
  created() {
    axios({
      method: "get",
      url: "pokemon/",
    }).then(function (res) {
      app.pokedex = res.data.pokemon;
    });
  },
});
