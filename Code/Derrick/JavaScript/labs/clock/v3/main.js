const $startTime = document.querySelector("#start-time");
const $addTime = document.querySelector("#time");
const $milliseconds = document.querySelector("#milli");
const $seconds = document.querySelector("#sec");
const $minutes = document.querySelector("#min");

$startTime.addEventListener("click", (event) => {
  event.preventDefault();

  // convert to milliseconds
  let time = $addTime.value * 60000;
  
  console.log(time);
});
