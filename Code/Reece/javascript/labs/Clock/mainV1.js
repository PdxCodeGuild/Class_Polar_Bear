
function dateTime() {

    // get current date
    const data = new Date();

    // get date
    let day = data.getDate();
    let mnt = data.getMonth() + 1;
    let yrs = data.getFullYear();

    // add date to DOM
    document.getElementById('my_date').innerHTML = 'Current Date: ' + day + '-' + mnt + '-' + yrs ;

    // get time
    let hrs = data.getHours();
    let min = data.getMinutes();
    let scs = data.getSeconds();

    // add time to DOM
    document.getElementById('my_time').innerHTML = 'Current Time: ' + hrs + ':' + min + ':' + scs
}

setInterval(dateTime, 1000)

dateTime()