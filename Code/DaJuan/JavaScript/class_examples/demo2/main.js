// let userName = prompt("Your name?")
// greeting = `Hello ${userName}`
// console.log(greeting)

function chargeLevel(percent){
    percent = parseInt(percent)
    if (percent === 100){
        return 'Phone fully charged.'
    }
    else if (percent > 20 && percent < 100){
        return 'Phone could use some charging.'
    }
    else {
        return 'Phone battery low.'
    }
}

let percent = prompt('Enter battery percentage')
phoneTitle = document.querySelector('#phone')
phoneTitle.textContent = chargeLevel(percent)