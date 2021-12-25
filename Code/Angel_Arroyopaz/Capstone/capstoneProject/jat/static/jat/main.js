const app = new Vue ({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        posts: []
    },
    methods: {
        getPosts: function () {
            axios ({
                method: 'get',
                url: '../posts/'
            }).then (function (response) {
                app.posts = response.data.posts
                console.log(app.posts)
            })
        }
    },
    created: function () {
        this.getPosts()
    }
})