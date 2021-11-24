// alert('Hello WOrld');
// console.log('Hello World');
// console.warn('Somethin went wrong');
// console.info('Page loaded');
// prompt('How is your day?');

// let userInput = prompt('How is your day?');
// userInput = 'Best day ever';
const favColor = 'red';
// favColor = 'green';

// alert(favColor);

// const sayHello = () => {
//   let favColor = 'blue';
//   console.log(favColor);
// };

// sayHello();

'Hello World'     // string
4                 // number
3.5               // number
true              // boolean
[1, 2, 3]        // array
{ name: 'Brian' } // object
undefined         // undefined
null              // object

// let greeting = 'Hello ' + 'World';
let sum = 4 + 6;

// let idk = 4 + '4';
// let idk = .1 + .2;
// let idk = parseFloat(3.5) + 4
// console.log(idk)

// let number = 10;
// if (number < 10) {
//   console.log('Hooray');
// } else
// if (number > 10) {
//   console.log('That is too large');
// } else {
//   console.log('Perfect fit');
// }

// const person = {
//   firstName: 'Joe',
//   lastName: 'Llama',
//   age: 30,
//   pets: {
//     dog: 'Spot',
//     cat: 'Ginger',
//     rock: 'Rocky'
//   }
// };

// person.age = 31;
// person.age += 1;
// person.age++;
// person.age--;
// console.log(person.pets.dog)

let pies = ['Apple', 'Pumpkin', 'Pecan', 'Sweet Potato'];

// Iterates ofer elements and returns each one
// for (pie of pies) {
//   console.log(pies);
// }

// This is how an array looks as an object
// let otherPies = {
//   '0': 'Apple',
//   '1': 'Pumpkin',
//   '2': 'Pecan',
//   '3': 'Sweet Potato'
// }

// RETURN ALL OF THE INDECES
// for (pie in pies) {
//   console.log(pie);
// }

// pies.push('Cherry');
// pies.push('Mincemeat');

// const bestPie = pies.pop();

// // console.log(pies, bestPie)
// const index = pies.indexOf('Pumpkin');
// pies.splice(index, index)

// if (pies.includes('Pumpkin')) {
//   console.log('Hooray! We have pumpkin pie!')
// } else {
//   console.log('Sad day!')
// }
// let allPies = '';
// for (pie of pies) {
//   allPies += pie + ', ';
// }
// const allPies = pies.join(', ')
// console.log(allPies)

let greeting = document.querySelector('#title');

greeting.textContent = 'Javascript is fun 😁'

greeting.className = "bold-red"