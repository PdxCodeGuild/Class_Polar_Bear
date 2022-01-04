const choiceSelect = document.querySelector('#choice-select')
const result = document.querySelector('#result')
import random

choiceSelect.addEventListener('click')

function getRandomInt(min, max){
    min = Math.ceil(min);
    max = Math.floor(max);
}
function getResult (){
    let choiceList = ['rock', 'paper', 'scissors']

    if (choiceSelect.value == '')
}