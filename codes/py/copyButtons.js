document.addEventListener("DOMContentLoaded", () => {
    const contents = []
    const buttons = []

    const contents2 = []
    const buttons2 = []

    const areas = document.getElementsByClassName('textelement')
    for (let i = 0; i<areas.length; i++){
      contents.push(areas[i].innerHTML)
      buttons.push(document.createElement('button'))
      buttons[i].className = 'copybutton'
      buttons[i].innerHTML = '<img src="../../img/clipboard.png">'
      buttons[i].addEventListener('click', () => {
        navigator.clipboard.writeText(contents[i]);
        buttons[i].innerHTML = '<img src="../../img/check.png">'
        buttons[i].style.backgroundColor = '#61b600'
      })
      areas[i].appendChild(buttons[i])
    }

    const copy = document.getElementsByClassName('copy')
    for (let i = 0; i<copy.length; i++){
      contents2.push(copy[i].innerHTML)
      buttons2.push(document.createElement('button'))
      buttons2[i].className = 'copybutton'
      buttons2[i].innerHTML = '<img src="../../img/clipboard.png">'
      buttons2[i].addEventListener('click', () => {
        navigator.clipboard.writeText(contents2[i]);
        buttons2[i].innerHTML = '<img src="../../img/check.png">'
        buttons2[i].style.backgroundColor = '#61b600'
      })
      copy[i].appendChild(buttons2[i])
    }
  } );