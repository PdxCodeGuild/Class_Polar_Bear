const clock = document.querySelector('#clock')

setInterval(function () {
    let currentDate = new Date();
    clock.innerHTML = currentDate.toLocaleTimeString();
}, 1000)