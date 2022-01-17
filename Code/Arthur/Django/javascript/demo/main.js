// // alert is like a print statement
// // alert("hello world!")


// // this you run in the source
// // console.log("Hello world!")
// // console.warn('something went wrong')
// // console.info('page loaded')



// // get information from the user
// // let userInput =prompt("how is your day?")
// // // if you use let you can change the variable, if you use const you cannot change the variable
// // userInput ='best day ever'
// // // const favColor='red'
// // // alert(userInput + 'and so is mine!')
// // alert(favColor)


// // const favColor='red'
// // function sayHello(){
// //     let favColor='blue'
// //     console.log(favColor)
// // }

// // sayHello()

// 'hello world'//string
// "hello world"//string
// 4 //number
// 3.5//number
// true//boolean
// [1,2,3]//array
// {name:'brian'}//object
// undefined //undefined
// null//object???

// // let greeting ='hello'+ 'world'
// // let sum =4+6

// // let idk =4 + '4'
// // console.log(idk)


// // let idl =parseInt('4') + 4
// // console.log(idl)

// // let idl ='4' + 4
// // console.log(idl)

// let number = 6
// if (number<10)
// {
//     console.log('Hooray!')
// }
// else if (number>10)
// {
//     console.log('that is a large number!')
// }

// // f12 and then console
// // javascript minify to hide your code
// //single is for assignment the double is for compare but use ===

// let person = {
//     firstName:'joe',
//     lastName:'Llama',
//     age:30,
//     pets:{
//         dog:'spot',
//         cat:'Ginger',
//         rock:'Rocky'
//     }
// }

// console.log(person.firstName)
// console.log(person['firstName'])

// // person.age =31
// person.age++
// console.log(person.age)
// console.log(person.pets.cat)
// console.log(perosn['pets']['cat'])

// let colors = {
//     'red': 'blue',
//     'green': 'brown',
//     'blue':'gold'
// }

// // // for key in colors
// // for (key of colors){
// //     console.log(colors(key))
// // }

// // let pies =['apple','pumpkin','peacan','sweet']
// // let otherpies ={
// //     '0':'apple',
// //     '1':'pumpkin',
// //     '2':'peacan',
// //     '3': 'sweet'
// // }

// // for (pie of pies){
// //     console.log(pies(pie))
// // }

// let pies =['apple','pumpkin','peacan','sweet']
// pies.length =20

// pies.push('banana')
// let bestpie =pies.pop(1)
// console.log(pies)

// if(pies.includes('pumkin'))
// {
//     console.log('Hooray!')
// }


// //start at index 1 and remove the 1 element 
// // pies.splice(1,1)

// // for(let i =0;i<100;i)
// // {
// // console.log(i)
// // }

// // for(let i =0;i<pies.length;i)
// // {
// // console.log(i)
// // }

// // let i=0
// // while(i<100)
// // {
// //     i++
// // }

// // for(let pie of pies)
// // {
// //     console.log(pie)
// // }

// // for(let i in pies)
// // {
// //     console.log(i)
// // }

// // function add_nums(num1,num2)
// // {
// //   return num1 + num2
// // }

// //const sayHello = function(name)
// // {
// //     return 'Hello' + name
// // }

// // console.log(sayHello('Tim'))


//this works on id's store #title into title
// let title =document.querySelector('#title')
// title.textContent = 'javascript is fun'
// title.style.color ='blue'
// title.style.fontSize ='30px'

// let userName = prompt("what is your name")

// greeting ='Hello ${userName}'
// console.log(greeting)

// let pets =['dogs','cats','snakes','birds']


//in is for indexes of is for pets 
// for (let pet of pets){
//console.log(pet)
// }


// let coffee= {
//     roast:'light',
//     size:'12pz',
//     flavouring:'vanilla'

// }
// console.log(coffee)

// coffee.roast='dark'

// function chargelevel(percentage)
// {    percent =parseInt(percentage)
//     if(percentage===100){
//         return 'phone fully charged'
//     }
//     else {
//         return 'low power'
//     }
// }

// let percentage =prompt("enter phone percentage")
// console.log(chargelevel(percentage))
// id
// let phonetitle =document.quuerySelector('#phone')
//phoneTitle.textContent = chargelevel('percentage)
let gradebutton =document.querySelector('#grade-button')
let gradeInput = document.querySelector('#grade-input')
gradebutton.addEventListener('click',getResults)
gradebutton.addEventListener('keypress',getResults)


// //when the user clicks what do we do
// gradebutton.addEventListener('keypress', function(){
//     let gradeInput =document.querySelector('#grade-input')
//     let grade = gradeInput.value
//   //   console.log(gradeInput.value)
//     let letter 
//     if (grade>90)
//     {
//         letter='A'
//     }
//     else if(grade>80)
//     {
//         letter ='B'
//     }
//     else if (grade>=70)
//     {
//         letter ='C'
//     }
//     else {
//         letter ='F'
//     }
  
//     let gradeResult = document.querySelector('#grade-result')
//     //the letter is not displaying
//     gradeResult.textContent='You got a(n) ${letter} ' 
//   })


function getResults()
{
  let gradeInput =document.querySelector('#grade-input')
  let grade = gradeInput.value
//   console.log(gradeInput.value)
  let letter 
  if (grade>90)
  {
      letter='A'
  }
  else if(grade>80)
  {
      letter ='B'
  }
  else if (grade>=70)
  {
      letter ='C'
  }
  else {
      letter ='F'
  }

  gradeInput.value=""
  let gradeResult = document.querySelector('#grade-result')
  //the letter is not displaying
  gradeResult.textContent='You got a(n) ${letter} ' 
}