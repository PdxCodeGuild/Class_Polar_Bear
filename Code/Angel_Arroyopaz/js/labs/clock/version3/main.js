// select the necessary elements from our index.html
let timerInput = document.querySelector('#timer-input')
let dropdownMenuSelect = document.querySelector('#dropdown-menu-select');
let hoursOption = document.querySelector('#hours-option');
let minutesOption = document.querySelector('#minutes-option');
let secondsOption = document.querySelector('#seconds-option');
let startButtonVersion3 = document.querySelector('#start-button')
let stopResetButton = document.querySelector('#stop-reset-button')
let clockP = document.querySelector('#clock-p');


// define our variables
let hours = 0;
let minutes = 0;
let seconds = 0;

let myIntervalVar;
let optionValue;

// event listeners
startButtonVersion3.addEventListener('click', function () {
    unitAssigner();
    timerInput.value = ''
    myInterval();
})

timerInput.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        unitAssigner();
        myInterval();
    }
})


stopResetButton.addEventListener('click', function () {
    clearInterval(myIntervalVar)
    hours = 0;
    minutes = 0;
    seconds = 0;
    clockP.innerHTML = hours + ':' + minutes + ':' + seconds;
})


// functions
function unitAssigner () {
    if (parseInt(dropdownMenuSelect.value) === 1) {
        hours = parseInt(timerInput.value);
        minutes = 60;
        seconds = 60;
        optionValue = 'Hours';
        clockP.innerHTML = hours + ':' + minutes + ':' + seconds;
    } else if (parseInt(dropdownMenuSelect.value) === 2) {
        minutes = parseInt(timerInput.value);
        hours = 0;
        seconds = 60;
        optionValue = 'Minutes';
        clockP.innerHTML = hours + ':' + minutes + ':' + seconds;
    } else {
        seconds = parseInt(timerInput.value);
        hours = 0;
        minutes = 0;
        optionValue = 'Seconds';
        clockP.innerHTML = hours + ':' + minutes + ':' + seconds;
    } 
}

function startCountdown () {
    clockP.innerHTML = hours + ':' + minutes + ':' + (seconds > 0 ? seconds : 0)
    if (optionValue === 'Hours') {
        if (hours === 1) {
            hours = 0;
        }

        if (minutes === 60){
            minutes--
        }
        if (seconds === 0) {
            minutes--
            seconds = 59;
        } if (minutes === 0 && hours > 0) {
            hours--
            minutes = 59;
            seconds = 59;
        } if ((hours + minutes + seconds) === 0) {
            alert('Times is up!')
            clearInterval(myIntervalVar)
        }
        seconds--
    

    } else if (optionValue === 'Minutes') {
        if (minutes >= 1) {
            minutes--;
        }
        seconds--
        if (seconds === 0 && minutes > 0) {
            minutes--
            seconds = 59
        } if ((hours + minutes + seconds) === 0) {
            alert('Times is up!')
            clearInterval(myIntervalVar)
        }


    } else if (optionValue === 'Seconds') {
        if (seconds < 0) {
        console.log(seconds)
        alert('Times is up!')
        
        clearInterval(myIntervalVar)
    }   seconds--
    }
}

function myInterval () {
    myIntervalVar = setInterval(startCountdown, 1000)
}