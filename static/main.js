console.log('Hello World from Base dir')

const head=document.getElementById('header')

if (head) {
    const gobackbtn=document.getElementById('go-back-btn')
    gobackbtn.addEventListener('click',()=> history.back())
}