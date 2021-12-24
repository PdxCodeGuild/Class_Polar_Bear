
const ChangeColorBtn = document.querySelector('#change-color-button')

ChangeColorBtn.addEventListener('click', function (){
    // alert('Hi there!')
    const ChangeColorInput = document.querySelector('#change-color-input')
    let color = ChangeColorInput.value
    const body = document.querySelector('#body')
    body.style.backgroundColor = color
})