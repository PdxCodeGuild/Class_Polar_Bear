// Vars

const lower = 'abcdefghijklmnopqrstuvwxyz'
const upper = lower.toUpperCase()
const num   = '0123456789'
const sym   = '!@#$%^&*()_-+=`~:;,<.>/?\|'
const all = lower + upper + num + sym 

// Elements

const $result = document.querySelector('#result')
const $btn = document.querySelector('#generate-btn')
const $length = document.querySelector('#length')
const $nums = document.querySelector('#nums')
const $syms = document.querySelector('#syms')
const $upper = document.querySelector('#upper')
const $lower = document.querySelector('#lower')
const $errorText = document.querySelector('#error-text')
const $resetBtn = document.querySelector('#reset-btn')


// Functions

function reset() {
    $result.textContent = null
    $errorText.textContent = null    
}

function randomize(r) { 
    for (let i = r.length - 1; i > 0; i--) {
        let randI = Math.floor(Math.random() * (i + 1));

        // swaps 2 letters, random letter from array (randI) and letter at current index (i) to shuffle password 
        [r[i], r[randI]] = [r[randI], r[i]];
    }
    return r.join('')
}

function generatePassword() {
    // Clear h4 and error of previous password
    $result.textContent = null
    $errorText.textContent = null

    // get values from input fields
    let pwLength = parseInt($length.value)
    let numOfLower = parseInt($lower.value)
    let numOfUpper = parseInt($upper.value)
    let nums = parseInt($nums.value)
    let syms = parseInt($syms.value)

    // Array to push characters to final result list
    let result = []

    // Establish indx var
    let indx

    // pick randomly from lower array however many user wants
    for (l = 0;l < numOfLower; l++) {
        indx = Math.floor(Math.random() * lower.length)
        result.push(lower[indx])
    }

    // pick randomly fromupper array however many user wants
    for (u = 0;u < numOfUpper; u++) {
        indx = Math.floor(Math.random() * upper.length)
        result.push(upper[indx])
    }

    // pick randomly from num array however many user wants
    for (n = 0;n < nums; n++) {
        indx = Math.floor(Math.random() * num.length)
        result.push(num[indx])
    }

    // pick randomly from symbols array however many user wants
    for (s = 0;s < syms; s++) {
        indx = Math.floor(Math.random() * sym.length)
        result.push(sym[indx])
    }

    // fill in remaining characters to fulfill length user chooses
    let remainder = pwLength - result.length  
    if (remainder > 0) {
        for (le = 0; le < remainder; le++){
            indx = Math.floor(Math.random() * all.length)
            result.push(all[indx]) 
        }
    }
    
    // Once pw is calculated, reset input fields to null
    [$length.value,
    $lower.value,
    $upper.value,
    $nums.value,
    $syms.value] = [null]

    // display error to user if pw length is longer than total num of chars chosen
    const errorText = `Your password will be longer than ${pwLength} because you chose more characters than the specified length of your password!`

    // randomize pw
    result = randomize(result)

    // Check if pw length is shorter than num of characters chosen and display error text if true
    if (pwLength < numOfUpper + numOfLower + nums + syms) {
        $errorText.textContent = errorText    
    }

    $result.textContent = result
       
}

// Run password generator when btn is clicked
$btn.addEventListener('click', generatePassword)

// Reset error text and result
$resetBtn.addEventListener('click', reset)



