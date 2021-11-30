let root = document.documentElement
let flexDirection = 'row'
let flexWrap = 'nowrap'
let justifyContent = 'flex-start'
let alignItems = 'flex-start'



const changeColor = () => {
  let colorPicker = document.getElementById('colorPicker')
  let color = colorPicker.value
  root.style.setProperty('--square-color', color)
}

const changeSize = () => {
  let size = document.getElementById('box-size').value
  size = `${size*10}vw`
  root.style.setProperty('--square-size', size)
}

const changeDirection = () => {
  let directions = document.getElementsByClassName('radio-dir')
  for (dir of directions){
    if (dir.checked){
      root.style.setProperty('--flex-direction', dir.value)
      flexDirection = dir.value
    }
  }
  updateCode()
}

const changeWrap = () => {
  btns = document.getElementsByClassName('flex-wrap')
  for (btn of btns){
    if (btn.checked) {
      root.style.setProperty('--flex-wrap', btn.value)
      flexWrap = btn.value
    }
  }
  updateCode()
}

const changeJustify = () => {
  btns = document.getElementsByClassName('justify-content')
  for (btn of btns){
    if (btn.checked) {
      root.style.setProperty('--justify-content', btn.value)
      justifyContent = btn.value
    }
  }
  updateCode()
}

const changeAlign = () => {
  btns = document.getElementsByClassName('align-items')
  for (btn of btns){
    if (btn.checked) {
      root.style.setProperty('--align-items', btn.value)
      alignItems = btn.value
    }
  } 
  updateCode()
}

const updateCode = () => {
  css = `
  .container {
    display: flex;
    flex-direction: ${flexDirection};
    flex-wrap: ${flexWrap};
    justify-content: ${justifyContent};
    align-items: ${alignItems};
  }
  `
  codeBox = document.getElementsByClassName('code')[0]
  console.log(codeBox)
  code = document.createElement("pre")
  code.innerText = css
  codeBox.removeChild(codeBox.firstChild)
  codeBox.appendChild(code)
}

updateCode()