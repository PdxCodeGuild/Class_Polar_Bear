const input = document.querySelector("#word");
const pTag = document.querySelector("#definition");

input.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    axios({
      method: "get",
      url: `https://api.dictionaryapi.dev/api/v2/entries/en/${input.value}`,
    }).then(({ data }) => {
      pTag.textContent = data[0].meanings[0].definitions[0].definition;
    });
  }
});
