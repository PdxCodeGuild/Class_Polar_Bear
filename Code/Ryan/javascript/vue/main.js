const app = new Vue({
    el: '#app',
    data: {
        message: 'Hello World',
        name: 'Bradly',
        age: 57,
        colors: [
            'red',
            'blue',
            'gree',
            'purple'
        ]
    },
    methods: {
        birthday: function () {
            this.age +=1
        }
    }
})

const colorList = new Vue ({
    el: '#app-2',
    data: {
        color: "",
        colors: []
    },
    methods: {
        addColor: function () {
            this.colors.push(this.color)
            this.color = ''
        },
        removeColor: function(color) {
            let index = this.colors.indexOf(color)
            // console.log(color)
            this.colors.splice(index, 1)
        }
    }
})