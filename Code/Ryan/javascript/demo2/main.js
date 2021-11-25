
const gradeButton = document.querySelector('#grade-button')

const gradeInput = document.querySelector('#grade-input')

gradeInput.addEventListener('keypress', function (event) {
    // console.log(event)
    if (event.key === 'Enter'){
        getResults()
    }
})

gradeButton.addEventListener('click', getResults)

function getResults() {
    let gradeInput = document.querySelector('#grade-input')
    let grade = gradeInput.value
    // console.log(gradeInput.value)

    let letter 
    if (grade > 90) {
        letter = 'A'
    } else if (grade > 80){
        letter = 'B'
    } else if (grade > 70){
        letter = 'C'
    } else if (grade > 60){
        letter = 'D'
    } else {
        letter = 'F'
    }

    gradeInput.value = ''
    let gradeResult = document.querySelector('#grade-result')
    gradeResult.textContent = `You got a(n) ${letter}`
}