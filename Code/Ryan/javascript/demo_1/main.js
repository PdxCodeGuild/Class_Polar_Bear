// prints a message in a pop up infront of the URLSearchParams

alert('Hello World')


// debugging purposes you can put it in the console

console.log('See what a console log looks like')
console.warn('Something went wrong')
console.info('Page loaded')
// prints a dictionary in a readable manner
// console.table

// to request user for input

// assign to a variable:
//     let //normal input can be redefined as the program runs

//     const // will make that variable that forever

let userInput = prompt('How is your day')
alert(userInput)

// old school way and a bit dangerous to use because it can be accessed throughout the program
var someName //not scoped bound // usable outside the function // dangerous way to define variables

// -------------------------------------------------

const favColor = 'red'
function sayHello(){
    let favColor = 'blue'
    console.log(favColor) //goes out if the variable does not exist (does not go into nested )
}

// --------------------------------------------------

if (true){
    let favColor = 'green'
}

// --------------------------------------
// Data Types

'Hello World'       //String
4                   //Number
3.5                 //Number
true                //Boolean
[1, 2, 3]           //Array (behaves much like a list)
{ name: 'Brian' }   //Object (behaves much like a dict)
undefined           //Undefined
null                //Object


let greeting = 'Hello ' + 'World'
let sum = 4 + 6

let idk = 4 + '4'
console.log(idk)

let number = 6
if (number < 10){
    console.log('Hooray!')
} else if (number > 10){
    console.log('That is a large number!')
} else {
    console.log('Hi')
}

// Javascript minifier to make it as unreadable as possible to make it difficult to parse

// == is to see if something is equal

// === makes sure to see if it is the same type and character


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

console.log(person.firstName)
console.log(person['firstName'])

// person.age = 31
person.age += 1
// person.age++ // incrementing by 1 only

// person.age -= 1
// person.age --
console.log(person.age)

// NESTED ITEMS 
console.log(person.pets.dog)
console.log(person['pets']['cat'])

// Objects
let colors = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF'
}
for (key in colors){
    console.log(colors['key'])
}
// in for objects
// of for arrays

// Arrays
let pies = ['Apple', 'Pumpkin', "Pecan", "Sweet Potato"]
for (pie of pies){
    console.log(pie)
}

for (pie in pies){
    console.log(pies['pie'])
}

// How to get the length of the array
console.log(pies.length)

// because it is an object can change attributes 
// pies.length = 20 //redifines the length but does not 

// to add to the array
pies.push('Cherry')
pies.push('Mincemeat')

// removes the last item of the Array
// stores the option to display if needed
pies.pop() //removes the last item
let bestPie = pies.pop() //saves the last item removed

// look up index and remove the item starting at that index
let index = pies.indexOf('Pumpkin')
pies.splice(index, 1)

// when you know the index of the object you want to remove
pies.splice(1, 1) // start at a specific index and remove a specific number of elements

console.log(bestPie)

// to see if there is an object in the array use METHOD
if (pies.includes('Pumpkin')){
    console.log('Hooray!, We have pumpkin pie!')
}


// Take an array and make a string.
let stringPies = pies.join(', ')
console.log(stringPies.toLowerCase()) //this will lower case the string using the METHOD

stringPies = stringPies.toLowerCase()


// LOOPS -------

for (pie of pies){
    console.log(pie)
}

for (pie in pies){
    console.log(pies['pie'])
}

for (let i = 0; i < 100; i++ ){
    console.log(i)
}


for (let i = 0; i < pies.length; i++){
    console.log(i)
    // pies[i] = 
}

let i = 0 
while (i < 100){
    i ++
}

for (let pie of pies){
    console.log(pie)
}

for (let i in pies ){
    console.log(i)
}

// This will allow you to add things to html using this
pies.forEach(function (pie){
    console.log(pie)
})

//creates new array
let mappedPies = pies.map(function (pie){
    console.log(pie)
})

// ----------------------------------------------------------
// FUNCTIONS
// ----------------------------------------------------------

// This gets hoisted to the top so can exist anywher in the program
function addNums(num1, num2){
    return num1 + num2
}

// Matters where in the program this is set
const sayHello = function (name) {
    return 'Hello ' + name
}

const arrFunc = (num1, num2) => {
    return num2 - num1
}

// _________________________________________________
// Document Manipulation DOM Manipulation
// -------------------------------------------------

let title = document.querySelector('#greeting')

title.textContent = 'JavaScript is fun!'