  //Javascript to toggle the menu\
  document.getElementById('nav-toggle').onclick = function(){
    document.getElementById("nav-content").classList.toggle("hidden");
  }

  window.addEventListener('DOMContentLoaded', ()=> {
    const menuBtn = document.querySelector('#menu-btn')
    const dropdown = document.querySelector('#dropdown')
    const accBtn = document.querySelector('#acc-btn')
    const accdropdown = document.querySelector('#acc-dropdown')
    
    menuBtn.addEventListener('click', () => {
      dropdown.classList.toggle('hidden')
      dropdown.classList.toggle('flex')
    })

    accBtn.addEventListener('click', () => {
      accdropdown.classList.toggle('hidden')
      accdropdown.classList.toggle('flex')
    })
  });