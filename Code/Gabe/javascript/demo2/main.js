// Datatypes
"How are you today?"    // String
'Excited doggo'         // String
45                      // Number
3.14                    // Number
true                    // Boolean
false                   // Boolean
['apple', 'banana']     // Array
{ name: 'Cloud' }       // Object
undefined               // undefined
null                    // Object

4 + '4' // '44'
'8' - 4 // 4

'8' == 8 // true
'8' === 8 // false

let pets = ['dogs', 'cats', 'snakes', 'birds', 'fish']
// Add element
pets.push('teenager')

// Remove last element
pets.pop()

// Remove by index
pets.splice(1, 1)

// Find index in array
let i = pets.indexOf('snakes')

// Types of variables
// let      -> Scope based variable, value can change
// const    -> Can not change value, once set
// var      -> Not scope based, value can change


// Strings
let greeting = 'Hello World'
// change to lowercase
greeting = greeting.toLowerCase()
// change to uppercase
greeting = greeting.toUpperCase()
// console.log(greeting)

// let userName = prompt('Enter your name:')
// Formatted strings
// greeting = `Hello ${userName}`
// console.log(greeting)

// For loops
pets = ['dogs', 'cats', 'snakes', 'birds', 'fish']
// for (let pet of pets){
//     console.log(pet)
// }

// for (let i = 0; i < pets.length; i++){
//     console.log(pets[i])
// }

// pets.forEach(function(pet){
//     console.log(pet)
// })

// While loop
// let i = 0
// while (i < pets.length){
//     i += 1
// }


// Objects
let coffee = {
    roast: 'light',
    size: '12oz',
    flavoring: 'vanilla'
}

coffee.roast = 'dark'
coffee.flavoring = 'Pumpkin Spice'

// console.table(coffee)

// Functions
function chargeLevel(percent){
    // document.querySelector to target element from html
    let phoneTitle = document.querySelector('#phone')
    percent = parseInt(percent)
    if (percent === 100){
        // .textContent to change text between element tags
        phoneTitle.textContent = `Battery state: Phone fully charged`
        // .className to set the class attribute
        phoneTitle.className = 'full'
    } else if (percent > 20 && percent < 100){
        phoneTitle.textContent = `Battery state: Phone is discharging`
        phoneTitle.className = 'discharge'
    } else {
        phoneTitle.textContent = `Battery state: Low power.`
        phoneTitle.className = 'empty'
    }
}

let percent = prompt('Enter phone percent:')
chargeLevel(percent)