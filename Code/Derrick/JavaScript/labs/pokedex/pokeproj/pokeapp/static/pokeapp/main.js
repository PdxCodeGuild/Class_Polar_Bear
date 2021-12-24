const app = new Vue({
  el: "#app",
  delimiters: ["[[", "]]"],
  data: {
    message: "Yellope",
    pokedex: {},
    search: "",
    found: null,
  },
  methods: {
    findPokemon: function () {
      axios({
        method: "get",
        url: "pokemon/",
        data: {
          name: app.search,
        },
      }).then(function (res) {
        res.data.pokemon.forEach((pokemon) => {
          if (pokemon.name === app.search.toLowerCase()) {
            app.found = null;
            app.found = pokemon;
          }
        });
      });
    },
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
