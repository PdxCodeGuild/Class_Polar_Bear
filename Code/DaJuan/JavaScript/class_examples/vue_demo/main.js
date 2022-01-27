const app = new Vue({
    el: '#app',
    data: {
        message: 'Hello World',
        name: "",
        age: "22",
        colors: [
            'blue',
            'yellow',
            'red',
            'black',
            'white'
        ]
    },
    methods: {
        birthday: function() {
            this.age++
        }
    
    }
})

const app2 = new Vue({
    el: '#app-2',
    data: {
        color: "",
        colors: [],
    },
    methods: {
        addColor: function () {
            this.colors.push(this.color)
            this.color = ""
        },
        removeColor: function (color) {
            let index = this.colors.indexOf(color)
            this.colors.splice(index, 1),
            app.data.colors.push(this.color)
        }
        }

})