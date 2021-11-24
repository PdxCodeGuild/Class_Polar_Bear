
// alert('Hello World')
// console.log('Class Polar Bear')
// console.warn('Something went wrong')
// console.info('Page loaded')

// let userInput = prompt('How is your day?')
// userInput = 'Best day ever'


// alert(typeof favColor)


// const favColor = 'red'
// function sayHello(){
//     var favColor = 'blue'
// }
// sayHello()

// if (true){
//     let favColor = 'green'
// }
// console.log(favColor)


'Hello World'       // String
"Hello world"       // String
4                   // Number
3.5                 // Number
true                // Boolean
[1, 2, 3]           // Array
{ name: 'Brian' }   // Object
undefined           // undefined
null                // Object ?!?!!

// let greeting = 'Hello ' + 'World'
// let sum = 4 + 6

// let idk = '4' - 4
// console.log(idk)


// let number = '20'
// if (parseInt(number) < 10){
//     console.log('Hooray!')
// } else if (number > 10){
//     console.log('That is a large number!')
// } else {
//     console.log('hi')
// }

// let number = 5
// console.log(number === '5')

let person = {
    firstName: 'Joe',
    lastName: 'Llama',
    age: 30,
    pets: {
        dog: 'Spot',
        cat: 'Ginger',
        rock: 'Rocky'
    }
}

// console.log(person.firstName)
// console.log(person['lastName'])

// person.age = 31
// person.age += 1
person.age++
// console.log(person.pets.cat)
// console.log(person['pets']['cat'])


let colors = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF'
}

// for (key in colors){
//     console.log(colors[key])
// }

// Python for loop
// for key in colors:
//     print(colors[key])


// let pies = ['Apple', 'Pumpkin', 'Pecan', 'Sweet Potato']
"apple, pumpkin, pecan, sweet potato, ..."

// for (pie of pies){
//     console.log(pie)
// }

// pies.push('Cherry')
// pies.push('Mincemeat')


// let stringPies = pies.join(', ')  //", ".join(pies)
// stringPies = stringPies.toLowerCase()
// console.log(stringPies)

// let bestPie = pies.pop()

// let index = pies.indexOf('Pumpkin')
// pies.splice(index, 1)

// console.log(pies)

// if (pies.includes('Pumpkin')){
//     console.log('Hooray!, We have pumpkin pie!')
// } else {
//     console.log('Sad day...')
// }



// for x in range(100):
//     print(x)

// for (let i = 0; i < 100; i++){
//     console.log(i)
// }

// for x in range(len(pies)):
//     print(x)

// for (let i = 0; i < pies.length; i++){
//     console.log(i)
//     // pies[i] = 'Some new pie'
// }

// let i = 0
// while (i < 100){
//     i ++
// }

// for (let pie of pies){
//     console.log(pie)
// }

// for (let i in pies){
//     console.log(i)
// }


let pies = ['Apple', 'Pumpkin', 'Pecan', 'Sweet Potato']

// pies.forEach(function (pie) {
//     console.log(pie + ' is yummy!')
// })


// let mappedPies = pies.map(function (pie){
//     return pie + ' this is a map'
// })

// console.log(addNums(3))
// console.log(addNums(3, 4))
// console.log(addNums(3, 4, 5, 6, 'llama'))

// def add_nums(num1, num2):
//     return num1 + num2

// This function type will be hoisted
function addNums(num1, num2){
    return num1 + num2
}


// Will not be hoisted
const sayHello = function (name) {
    return 'Hello ' + name
}

// console.log(sayHello('Tim'))

// Arrow function, will not be hoisted
const arrFunc = (num1, num2) => {
    return num2 - num1
}

// console.log(arrFunc(3, 4))



let title = document.querySelector('#title')
title.textContent = 'JavaScript is fun!'
// title.style = 'color: red; font-size: 60px;'
// title.style.color = 'blue'
// title.style.fontSize = '30px'
title.className = 'bold-red'