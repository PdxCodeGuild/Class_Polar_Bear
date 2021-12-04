const clock = document.querySelector('#clock-1')

setInterval(function () {
    let currentDate = new Date();
    clock.innerHTML = currentDate.toLocaleTimeString();
}, 1000)