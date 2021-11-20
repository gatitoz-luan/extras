function calculatetip(event) {
    alert('fui submetido')
}
document.getElementById('totaltip').style.display="none";
document.getElementById('tipsForm').addEventListener('submit',calculatetip)