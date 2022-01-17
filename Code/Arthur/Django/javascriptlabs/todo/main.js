document.querySelector('#add').onclick = function()
{
    if(document.querySelector('#newtodos input').value.length == 0)
    {
        alert("Enter a todo")
    }

    else
    {
        document.querySelector('#todos').innerHTML += `
            <div class="todo">
                <span id="todoname">
                    ${document.querySelector('#newtodos input').value}
                </span>
                <button class="delete">
                    <i class="trash"></i>
                </button>
            </div>`

        let current_todos = document.querySelectorAll(".delete");
        for(let i=0; i<current_todos.length; i++)
        {
            current_todos[i].onclick = function()
            {
                this.parentNode.remove();
            }
        }
    }
}