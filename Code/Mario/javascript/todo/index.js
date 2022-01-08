var addBtn = document.getElementById("add_item_btn");
addBtn.addEventListener("click", (e) => updateList(e));

function updateList(e) {
  e.preventDefault();

  const textContent = document.getElementById("new_item").value;
  const item = document.createElement("li");
  const itemContainer = document.getElementById("todo_items");
  itemContainer.appendChild(item);
}
// $0.style
