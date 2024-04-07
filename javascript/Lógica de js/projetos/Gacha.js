const prompt = require("prompt-sync")({ sigint: true });
let comum = 0
let incomum = 0
let raro = 0
let epico = 0
let lendario = 0
let mitico = 0
let especial = 0
raridade = ['Comum', 'Incomum','Raro', 'Épico', 'Lendário', 'Mítico', 'Especial']
raridades = ['Comuns', 'Incomuns','Raros', 'Épicos', 'Lendários', 'Míticos', 'Especiais']
quantidades = prompt('Quanto giros no gacha você quer dar?  ')
giros = Number(quantidades)
gacha(giros)
function gacha(giros){
    console.log('x-x-x-x-x')
    for(let comeco = 1;comeco <= giros;comeco++){
        let chances = Math.random() * 100
        if(chances > 75){
            comum += 1
        }
        if(chances > 50 && chances <= 75){
            console.log('Incomum')
            incomum += 1
        }

        if(chances > 30 && chances <= 50){
            console.log('Raro')
            raro += 1
        }

        if(chances > 15 && chances <= 30){
            console.log('Épico')
            epico += 1
        }

        if(chances > 5 && chances <= 15){
            console.log('Lendário')
            lendario += 1
        }

        if(chances > 1 && chances <= 5){
            console.log('Mítico')
            mitico += 1
        }
        if(chances <= 1){
            console.log('Especial')
            especial += 1
        }
        
    
    }
    console.log('x-x-x-x-x')
    mochila = [comum, incomum, raro, epico, lendario, mitico, especial]
    quantidadenamochila = (mochila.length - 1)
    console.log('')
    console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    for(i = 0; i <= quantidadenamochila; i++){
        switch(mochila[i]){
            case 1:
            console.log(`Você recebeu ${mochila[i]} item ${raridade[i]}`)
            break

            case 0:
            console.log(`Você recebeu Nenhum item ${raridade[i]}`)
            break

            default:
            console.log(`Você recebeu ${mochila[i]} itens ${raridades[i]}`)
            break
        }
    }
    console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

}                                          