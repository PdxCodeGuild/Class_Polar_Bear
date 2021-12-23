const app = new Vue({
    el: '#app',
    data: {
        message: 'Hello django and vue!',
        newPostTitle: '',
        newPostBody: '',
        posts: []
    },
    methods: {
        submitPost: function () {
            axios({
                method: 'post',
                url: 'save_post/',
                data: {
                    title: app.newPostTitle,
                    body: app.newPostBody
                }
            }).then(response => {
                app.getPosts()
                app.newPostTitle = ''
                app.newPostBody = ''
            })
        },
        getPosts: function () {
            axios({
                method: 'get',
                url: 'http://localhost:8000/api/posts'
            }).then(function (response) {
                app.posts = response.data.posts
                console.log(app.posts)
            })
        }
    },
    created: function () {
        this.getPosts()
    }
})