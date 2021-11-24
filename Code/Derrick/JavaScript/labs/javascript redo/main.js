// Vars

const lower = 'abcdefghijklmnopqrstuvwxyz'
const upper = lower.toUpperCase()
const num   = '0123456789'
const sym   = '!@#$%^&*()_-+=`~:;,<.>/?\\|'
const all = lower + upper + num + sym 

// Elements

const $result = document.querySelector('#result')
const $btn = document.querySelector('#generate-btn')
const $input = document.querySelector('#user-input')

// Functions

function generatePassword() {
    let num = parseInt($input.value)
    for (i = 0; i < num; i++){
        let indx = Math.floor(Math.random() * all.length)
        $result.textContent += all[indx] 
    }
    $input.value = null
}

$btn.addEventListener('click', generatePassword)

