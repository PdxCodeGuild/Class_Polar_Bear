const app = new Vue({
    el: '#app',
    data: {
        characters: []
    },
    methods: {

    },
    created: function () {
        axios({
            method: 'get',
            url: 'http://hp-api.herokuapp.com/api/characters'
        }).then(function (response) {
            app.characters = response.data
        })
    }
})