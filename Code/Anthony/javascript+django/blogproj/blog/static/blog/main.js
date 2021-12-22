const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        message: 'Hello django and vue!',
        newPostTitle: '',
        newPostBody: '',
        posts: []
    },
    methods: {
        submitPost: function () {
            const csrftoken = Cookies.get('csrftoken');
            console.log(csrftoken)
            axios({
                method: 'post',
                url: 'save_post/',
                headers: {'X-CSRFToken': csrftoken},
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
                url: 'posts/'
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