const prompt = require("prompt-sync")({ sigint: true });
item = {
    nome: 'Coxinha',
    preço: 4,
    quantidade: 10
}
console.log('Teve uma crise e a coxinha aumentou ou diminui?')
resposta = prompt('A para aumentou / D para diminuio')
if(resposta === 'A'){
    preco = Math.random * 3
    console.log(`Agora a ${item.nome} aumentou e está com ${item.preço + preco}`)
}
item.recheio = ['frango e catupry', 'frango', 'frango e chedar']
console.log(item)
