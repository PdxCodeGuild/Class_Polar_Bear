const btn = document.querySelector("#add-btn")
const item = document.querySelector("#list-item")
const list = document.querySelector("#list")

btn.addEventListener("click", () => {
  let item_c = document.createElement("c")
  let item_i = document.createElement("i")
  let xs = document.createElement("s")
  let ys = document.createElement("s")

  item_i.innerHTML = item.value
  ys.innerHTML = 'accept'
  xs.innerHTML = 'reject'

  xs.addEventListener("click", function () {this.parentNode.remove()})
  ys.addEventListener("click", function () {
    let title = this.parentElement.firstChild
    title.classList.add("complete")
  })

  item_c.appendChild(item)
  item_c.appendChild(xs)
  item_c.appendChild(ys)
  list.append(item_c)
  item.value = null
}

