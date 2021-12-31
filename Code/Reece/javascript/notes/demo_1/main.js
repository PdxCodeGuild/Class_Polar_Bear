
// alert('Hello World!')
// console.log('Class Polar Bear')
// console.warn('Something went wrong')
// console.info('Page loaded')

// let userInput = prompt('How is your day?')
// userInput = ' Best day ever'
// const favColor = 'red'


// alert(favColor)

'Hello World'       // String
"Hello world"       // String
4                   // Number
3.5                 // Number
true                // Boolean
[1,2,3]             // Array
{ name: 'Brian'}    // Object
undefined           // undefined
null                // Object ?!?!!

// let greeting = 'Hello ' + 'World'
// let sum = 4 + 6

// let idk = '4' + 4
// console.log(idk)

// let number = 6

// if (number < 10){
//     console.log('Hooray!')
// } else if (number > 10){
//     console.log('That is a large number')
// }

// let number = 5
// console.log(number === '5')

let person = {
    firstName: 'Joe',
    lastName: 'Llama',
    age: 30,
    pets :{
        dog: 'Spot',
        cat: 'Ginger',
        rock: 'rocky',
    }
}

// console.log(person.firstName)

// person.age = 31
// person.age += 1
// person.age ++

// console.log(person.pets.dog)

let colors = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
}

// for (key in colors){
//     console.log(colors[key])
// }

// Python for loop
// for key in colors
//     print(colors[key])

// let pies = ['Apple', 'Pumpkin', 'Pecan', 'Sweet Potato']

// for (pie of pies){
//     console.log(pie)
// }

// pies.push('Cherry')
// pies.push('Mincemeat')

// let stringPies = pies.join(' , ')  //", ".join(pies)
// stringPies = stringPies.toUpperCase()
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

//for z in range(100):
//      print(x)

// for ( let i = 0; i < 100; i++ ){
//     console.log(i)
// }

//for z in range(len(pies):
//      print(x)

// for (let i = 0; i < pies.length; i++){
//     console.log(i)
// }

// let i = 0
// while ( i < 100 ){
//     i ++
// }

// let pies = ['Apple', 'Pumpkin', 'Pecan', 'Sweet Potato']

// pies.forEach(function (pie) {
//     console.log(pie + ' is yummy!')
// })

// def add_nums(num1, num2):
//     return num1 + num2

function addNums(num1, num2){
    return num1 + num2
}

// console.log(addNums(3, 4, 5, 6, 7, 'quiznos' ))




let title = document.querySelector('#title')
title.textContent = 'JavaScript is fun!'
title.style = 'color:Rebeccapurple; font-size: 60px'