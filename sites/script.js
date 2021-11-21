function calculatetip(event) {
    event.preventDefault();
    let ex = document.getElementById('exer').value;
    let pe = document.getElementById('peso').value;
    let rep = document.getElementById('falha').value;
    let c=(1-(0.02*int(rep)));
    let rm=(rm = int(pe)/c);
    document.getElementById('tot').innerHTML = rm;
}

document.getElementById('totaltip').style.display="block";
document.getElementById('tipsForm').addEventListener('submit',calculatetip);



//// indicar: https://www.basefitness.com.br/?s=supino  ////