function appendToDisplay(value) {
    document.getElementById('display').value += value; // números
}

function clearDisplay() {
    document.getElementById('display').value = ''; // apagar
}

function calculate() {
    const displayValue = document.getElementById('display').value;
    try {
        const result = eval(displayValue); // quando o calculate for clicado o eval é acionado e faz a conta
        document.getElementById('display').value = result; // valor
    }
    
    catch (error) { // caso esteja algo errado
        document.getElementById('display').value = 'Error'; // oque sera transmitido
    }
}
