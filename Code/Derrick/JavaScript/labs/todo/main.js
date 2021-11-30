const $list = document.querySelector('#list')
const $itemInput = document.querySelector('#list-item')
const $btn = document.querySelector('#add-item-btn')

$btn.addEventListener('click', function() {
    // Create div for new item and buttons
    let $itemDiv = document.createElement('div')
    let $item = document.createElement('p')
    let $spanY = document.createElement('span')
    let $spanX = document.createElement('span')

    // Create content for listItem and buttons to remove or complete
    $item.innerHTML = $itemInput.value
    $spanY.innerHTML = '✔️'
    $spanY.setAttribute('title','Mark Complete')
    $spanX.innerHTML = '❌'
    $spanX.setAttribute('title','Remove from list')

    // Add listeners to buttons
    $spanX.addEventListener('click', function() {
        this.parentNode.remove()
    })

    $spanY.addEventListener('click', function() {
        let $listTitle = this.parentElement.firstChild
        $listTitle.classList.add('complete')
    })
    
    // Append elements to div and page
    $itemDiv.appendChild($item)
    $itemDiv.appendChild($spanX)
    $itemDiv.appendChild($spanY)
    $list.append($itemDiv)
    
    // Erase input field
    $itemInput.value = null
})