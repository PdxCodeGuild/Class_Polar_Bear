let seconds = 0

// setTimeout(function(){
//     const greeting = document.querySelector('#greeting')
//     greeting.textContent = "JavaScript is difficult"
// }, 5000)

let counter 



const startBtn = document.querySelector("#start-btn")
startBtn.addEventListener('click', function(){
    counter = setInterval(function(){
        const greeting = document.querySelector('#greeting')
        seconds++
        greeting.textContent = seconds
    }, 1000)
})

const stopBtn = document.querySelector("#stop-btn")
stopBtn.addEventListener('click', function(){
    clearInterval(counter)
})