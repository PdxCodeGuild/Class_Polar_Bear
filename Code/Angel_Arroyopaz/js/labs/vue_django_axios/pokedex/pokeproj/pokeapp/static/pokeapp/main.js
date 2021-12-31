const app = new Vue ({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        pokemons: [],
        search: "",
    },
    methods: {
        getPokemons: function () {
            axios ({
                method: 'get',
                url: '../pokemons/'
            }).then(function (response) {
                app.pokemons = response.data.pokemons
                console.log(app.pokemons)
            })
        }
    },
    created: function () {
        this.getPokemons()
    },
    computed: {
        filteredPokemons: function () {
            return this.pokemons.filter((pokemon) => {
                this.search = this.search.toLowerCase();
                return pokemon.name.match(this.search);
            })
        }
    }
})