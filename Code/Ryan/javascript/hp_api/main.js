const app = new Vue({
    el: '#app',
    data: {

    },
    methods: {

    },
    created: function () {
        axios({
            method: 'get',
            url: 'https://hp-api.herokuapp.com/'
        }).then(function(response){
            console.log(response)
        })
    }
})