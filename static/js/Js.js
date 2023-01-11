var btnDisable = document.getElementById('btn')
var displayCard = document.getElementById('cardBtn')

if (btnDisable.click){
    displayCard.removeAttribute('disabled')
}
else {
    displayCard.disabled == true
}