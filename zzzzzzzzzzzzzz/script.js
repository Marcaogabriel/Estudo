function adicionarProduto() {
    const inputProduto = document.getElementById('inputProduto');
    const nomeProduto = inputProduto.value.trim();
    inputProduto.value = '';

    if (nomeProduto !== '') {
        const listaProdutos = document.getElementById('listaProdutos');

        const li = document.createElement('li');
        li.textContent = nomeProduto;

        li.addEventListener('click', function() {
            this.classList.toggle('produto-riscado');
        });

        listaProdutos.appendChild(li);
    }
}
