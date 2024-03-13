const prompt = require("prompt-sync")({ sigint: true });
item = {
    nome: 'Coxinha',
    preço: 4,
    quantidade: 10
}
console.log('Teve uma crise e a coxinha aumentou ou diminui?')
resposta = prompt('A para aumentou / D para diminuio'    )
preco = Math.random() * 2
if(resposta === 'A'){
    console.log(`Agora a ${item.nome} aumentou e está por ${Math.round(item.preço + preco)}`)
    item.preço = Math.round(item.preço + preco)
}
else if(resposta === 'D'){
    console.log(`Agora a ${item.nome} diminuiu e está por ${Math.round(item.preço - preco)}`)
    item.preço = Math.round(item.preço - preco)
}
console.log('Veio novos sabores de coxinhas veja abaixo no cardapio')
item.recheio = ['frango e catupry', 'frango', 'frango e chedar']
console.log('')
console.log(item)
