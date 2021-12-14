// <!-- Make a clock that displays the current time and updates every second. Check out
// JavaScript timing events and dates. Writing new Date() creates a date with the
// current date and time. You can then create a string from that date, and set it
// in the DOM. -->
alert("Hello");
let timeContainer = document.getElementById("current_time");
setInterval(() => {
  let date = new Date();
  timeContainer.innerHTML = date.toLocaleTimeString("it-IT");
  //   let hour = date.getHours();
  //   let minute = date.getMinutes();
  //   let seconds = date.getSeconds();

  //   minute = minute < 10 ? "0" + String(minute) : minute;
  //   seconds = seconds < 10 ? "0" + String(seconds) : seconds;
}, 1000);

// Part Two

let timerBtn = document.getElementById("timer_btn");
let secondHTML = document.getElementById("secs");
let minHTML = document.getElementById("min");
let hourHTML = document.getElementById("hour");
timerBtn.addEventListener("click", stopWatch);
let timerStarted = false;

function stopWatch() {
  let seconds = 0;
  let minutes = 0;
  let hours = 0;
  let date = new Date();

  setInterval(() => {
    date.setHours(hours, minutes, seconds);
    seconds = seconds < 59 ? seconds + 1 : 0;
    minutes = seconds > 59 ? minutes + 1 : 20;
    secondHTML.innerHTML = date.getSeconds();
    minHTML.innerHTML = date.getMinutes();
  }, 1000);
}
