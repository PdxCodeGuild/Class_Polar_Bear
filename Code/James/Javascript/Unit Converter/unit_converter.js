let num = prompt('Enter a number: ')
let unit1 = prompt('What unit would you like to convert from (mm, m, cm, or km):  ')
let unit2 = prompt('What unit would you like to convert to (mm, m, cm, or km): ')

if (unit1 === 'm' && unit2 === 'mm') {
    output = parseInt(num)*1000
    console.log(output)
}
if (unit1 === 'm' && unit2 === 'km') {
    output = parseInt(num)/1000
    console.log(output)
}
if (unit1 === 'm' && unit2 === 'cm') {
    output = parseInt(num)*100
    console.log(output)
}
if (unit1 === 'cm' && unit2 === 'm') {
    output = parseInt(num)/100
    console.log(output)
}
if (unit1 === 'cm' && unit2 === 'mm') {
    output = parseInt(num)/10
    console.log(output)
}
if (unit1 === 'cm' && unit2 === 'km') {
    output = parseInt(num)*100000
    console.log(output)
}
if (unit1 === 'km' && unit2 === 'm') {
    output = parseInt(num)*1000
    console.log(output)
}
if (unit1 === 'km' && unit2 === 'mm') {
    output = parseInt(num)*1000000
    console.log(output)
}
if (unit1 === 'km' && unit2 === 'cm') {
    output = parseInt(num)*100000
    console.log(output)
}
if (unit1 === 'mm' && unit2 === 'm') {
    output = parseInt(num)/1000
    console.log(output)
}
if (unit1 === 'mm' && unit2 === 'km') {
    output = parseInt(num)/1000000
    console.log(output)
}
if (unit1 === 'mm' && unit2 === 'cm') {
    output = parseInt(num)/10
    console.log(output)
}
