let gradingButton = document.querySelector('#grade-button')

gradingButton.addEventListener('click', function () {
    let gradeInput = document.querySelector('#grade-input')
    let grade = gradeInput.value

    let letter
    if (grade >= 90){
        letter = 'A'
    }else if (grade > 80){
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
})