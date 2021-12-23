const app = new Vue({
  el: '#app',
  data: {
    message: 'Hello from Vue!',
    name: 'Bradly',
    age: 57,
    colors: ['red', 'blue', 'green', 'yellow', 'purple']
  },
  methods: {
    birthday: function() {
      this.age += 1;
    }
  }
})

const colorList = new Vue({
  el: '#app-2',
  data: {
    color: '',
    colors: []
  },
  methods: {
    addColor: function() {
      this.colors.push(this.color);
      this.color = '';
    },
    removeColor: function(color) {
      console.log('hello')
      const index = this.colors.indexOf(color);
      this.colors.splice(index, 1);
    },
  }
})