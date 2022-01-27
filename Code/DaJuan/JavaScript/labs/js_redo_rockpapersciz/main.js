const choiceSelect = document.querySelector('#choice-select')
const result = document.querySelector('#result')
const submitButton = document.querySelector('#submit-button')


submitButton.addEventListener('click', getRandomInt)

function getRandomInt(min, max){
    let compChoices = ['rock', 'paper', 'scissors'];
    
    min = Math.ceil(min);
    max = Math.floor(max);
    for (i in compChoices){
        console.log(compChoices[i])
    }
}
