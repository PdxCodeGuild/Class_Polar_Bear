const changeColorBtn = document.querySelector('#change-color-button')

changeColorBtn.addEventListener('click', function () {
    const changeColorInput = document.querySelector('#change-color-input')
    let color = changeColorInput.value
    const root = document.querySelector(':root')
    root.style.setProperty('--bg-color', color)
})