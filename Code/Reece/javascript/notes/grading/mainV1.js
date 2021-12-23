
let gradeButton = document.querySelector('#grade-button')
// console.log(gradeButton)
gradeButton.addEventListener('click', function () {
    let gradeInput = document.querySelector('#grade-input')
    let grade = gradeInput.value

    let letter
    if (grade >= 90){
        letter = 'A'
    } else if (grade >= 80){
        letter = 'B'
    } else if (grade >= 70){
        letter = 'C'
    } else if (grade >= 60){
        letter = 'D'
    } else {
        letter = 'F'
    }

    let gradResult = document.querySelector('#grade-result')
    gradResult.textContent = `You got a(n) ${letter}`
})