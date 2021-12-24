const app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    message: 'hello',
    newPostTitle: '',
    newPostBody: '',
    posts: [],
  },
  methods: {
    // submitPost: function() {
    //   axios.post('', {
    //     title: app.newPostTitle,
    //     body: app.newPostBody
    //   })
    // },
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
  created: function() {
    this.getPosts();
  },
})