
let addItem = document.querySelector('#add_item')
let itemToDo = []
let displayItem = document.querySelector('#display-item')
let newItemRow
let newStatus
let deleteMe
let newToDoItem
let newItem = document.querySelector('#new_item')

addItem.addEventListener('click', function (){
    let pushNewItem = newItem.value
    itemToDo.push({text: pushNewItem, completed: false})
    displayItems(itemToDo)
})


function displayItems(){
    displayItem.innerHTML = ''
    for (let i = 0; i < itemToDo.length; i++){
        newItemRow = document.createElement('tr')
        let newItemData_1 = document.createElement('td')
        let itemObject = itemToDo[i]
        // console.log(itemObject['text'])
        newItemData_1.innerHTML = itemObject['text']
        newStatus = document.createElement('input')
        newStatus.type = 'checkbox'
        newStatus.name = `name_${i}`
        newStatus.value = 'value'
        newStatus.id = `id_status_${i}`
        if (itemObject['completed'] === true){
            newItemData_1.style.textDecoration = 'line-through'
            newItemData_1.style.color = 'gray'
            newStatus.checked = true
            // console.log(`tried this out`)
        }
        newStatus.addEventListener('click', function (event){
            // console.log(event.target.checked)
            let changeItemStatus = event.target.checked
            const parent = newItemData_1.parentElement
            const td = parent.querySelector('td')
            // console.log(newStatus.parentElement)
            if (changeItemStatus === true){
                itemObject['completed'] = true
                td.style.textDecoration = 'line-through'
                td.style.color = 'gray'
            } else {
                itemObject['completed'] = false
                td.style.textDecoration = 'none'
                td.style.color = 'black'
            }
        })

        // newStatus.addEventListener()
        deleteMe = document.createElement('button')
        deleteMe.textContent = '❌'
        deleteMe.id = `id_delete_${i}`
        deleteMe.addEventListener('click', function () {
            itemToDo.splice(i, 1)
            displayItems(itemToDo)
        })
            // Deletes the item but does not push new list
        newItemRow.appendChild(newItemData_1)
        newItemRow.appendChild(newStatus)
        newItemRow.appendChild(deleteMe)
        displayItem.append(newItemRow)
        newItem.value = ''
    }
}

