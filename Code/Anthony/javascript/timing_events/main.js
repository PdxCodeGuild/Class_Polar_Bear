let seconds = 60

function changeGreeting(){
    const greeting = document.querySelector('#greeting')
    greeting.textContent = "JavaScript is fun"
}

let change = setTimeout(changeGreeting, 1000)
clearTimeout(change)


let counter

const startBtn = document.querySelector('#start-btn')
startBtn.addEventListener('click', function() {
    counter = setInterval(function() {
        const greeting = document.querySelector('#greeting')
        seconds--
        greeting.textContent = seconds
    }, 1000)
})

const stopBtn = document.querySelector('#stop-btn')
stopBtn.addEventListener('click', function() {
    if (counter) {
        clearInterval(counter)
    }
})