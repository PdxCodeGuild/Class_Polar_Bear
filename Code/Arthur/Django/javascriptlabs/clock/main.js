function renderTime()
{
    let newDate =new Date()
    let newYear =newDate.getYear()
    if(newYear<1000)
    {
        newYear +=1900
    }

    let newDay = newDate.getDay();
    let newMonth = newDate.getMonth();
    let newDaym = newDate.getDate();
    let newDayArray = new Array("sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    let newMonthArray = new Array("January","February","March","April","May","June","July","August","September","October","November","December")

    let CurrentTime = new Date()
    let hours = CurrentTime.getHours()
    let minutes = CurrentTime.getMinutes()
    let seconds = CurrentTime.getSeconds()

    if(hours == 24)
    {
        hours=0

    }
    else if(hours>12)
    {
        hours=hours-0

    }

    if(hours<10)
    {
        hours="0"+hours
    }

    if(minutes<10)
    {
        minutes="0"+minutes
    }

    if(seconds<10)
    {
        seconds="0"+minutes
    }

    let newClock = document.getElementById("clock")
    newClock.textContent = "" + newDayArray[newDay]+ " " +newDaym+ " " +newMonthArray[newMonth]+ " " +newYear+ " | " +hours+ ":" +minutes+ ":" +seconds
    newClock.innerHTML = "" + newDayArray[newDay]+ " " +newDaym+ " " +newMonthArray[newMonth]+ " " +newYear+ " | " +hours+ ":" +minutes+ ":" +seconds


    setTimeout("renderTime()",1000)
}

renderTime();