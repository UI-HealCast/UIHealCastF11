const toggle = document.querySelector('.toggle input')

$(document).on('click', '.slider.round', function(){
    console.log(123)
    const onOff = toggle.parentNode.querySelector('.onoff')
    onOff.textContent = toggle.checked ? 'Tersedia' : 'Tidak Tersedia'
})