/*var nome = prompt('Qual seu nome?')
alert('Taca-le pau ' + nome)
confirm('Ta top?')
var n1 = Number(prompt('A Soma entre '))
var n2 = Number(prompt('e '))
var s= n1+n2
alert('Resulta em ' + s)*/
var a = window.document.getElementById('area')
a.addEventListener ('click', clicar)
a.addEventListener('mouseenter', entrar)
a.addEventListener('mouseout', sair)
var b = window.document.getElementById('letra')
function clicar() {
b.innerText = 'clicou!'
a.style.background = "red"
}
function entrar() {
b.innerText = 'Entrou!'
}
function sair() {
b.innerText = 'Saiu!'
a.style.background = "blue"
}

function somar() {
    var n1 = window.document.getElementById('n01')
    var n2 = window.document.getElementById('n02')
    var n1= Number(n01.value)
    var n2= Number(n02.value)
    var res= window.document.getElementById('res')
    var s= n1+n2
    res.innerHTML = `A Soma entre ${n1} e ${n2} é igual a ${s}`
}