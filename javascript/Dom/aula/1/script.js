const container = document.getElementById('container');
// nome do id
const button = document.getElementById('btn');

function clicar() {
    // Oque ele vai aprender 
    const newParagraph = document.createElement("p");
    // Oque vai escrever
    newParagraph.textContent = "asaasasasasasasasasasasas"; 
    // Adicionar o novo paragrafo
    container.appendChild(newParagraph)
}
