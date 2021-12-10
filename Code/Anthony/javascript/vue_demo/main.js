const app = new Vue({
    el: '#app',
    data: {
        message: "Let's checkout Vue",
        name: "Bradly",
        age: 57,
        colors: [
            'red',
            'blue',
            'green',
            'yellow',
            'purple'
        ]
    },
    methods: {
        birthday: function () {
            this.age += 1
        }
    }
})

const colorList = new Vue({
    el: "#app-2",
    data: {
        color: "",
        colors: [],
        numbers: []
    },
    methods: {
        addColor: function () {
            this.colors.push(this.color)
            this.color = ""
        },
        removeColor: function(color) {
            let index = this.colors.indexOf(color)
            this.colors.splice(index, 1)
        },
        addThousand: function () {
            for(let i =0; i<1000; i++){
                this.numbers.push(i)
            }
        }
    }
})