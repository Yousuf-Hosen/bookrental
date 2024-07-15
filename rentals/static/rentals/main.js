const form=document.getElementById('search-form')
const input = document.getElementById("id_search") // id_field name here seaech is a fields name
const BOOK_ID_LENGTH=24

input.focus()

input.addEventListener("keyup", () => {
    if (input.value.length === BOOK_ID_LENGTH) {
        form.submit()
    }
})