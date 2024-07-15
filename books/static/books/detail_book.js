// console.log("Hello world from detail book")

const copy_btn=document.getElementById('copy-btn-box')
const bookIDCopy=document.getElementById('book-id-box')

copy_btn.addEventListener('click',()=>{
    const bookId=bookIDCopy.textContent;
    navigator.clipboard.writeText(bookId).then(()=> {
        copy_btn.innerHTML=" <p> Copied!</p> "
    })
})