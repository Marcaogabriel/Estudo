const prompt = require("prompt-sync")({ sigint: true });
let voceganhou = 0
let voceperdeu = 0
let empatou = 0
while(true){
    linha_x()
    console.log(`MENU DO JOGO
[ 1 ] Jogar Pedra, Papel e Tesoura
[ 2 ] Regras do Pedra, Papel e Tesoura
[ 3 ] Placar
[ 4 ] Sair do jogo`)
linha_x()
espaco()
    let numero = prompt('Escolha uma opção: ')
    let resposta = Number(numero)

    if(resposta === 1){
        prompt('Aperte ENTER para começarmos os jogos')
        while(true){
            limpar()
            console.log('Qual você deseja escolher')
            escolha = prompt(`[ 1 ] PEDRA   [ 2 ] PAPEL  [ 3 ] TESOURA   `)
            espaco()
            opcao = Number(escolha)
            // oponente -> 0 Pedra 1 Papel 2 Tesoura
            oponente = Math.round(Math.random() *  2)
            // pedra
            if(opcao === 1 && oponente === 0){
                console.log('Deu empate de Pedra com Pedra')
                empatou += 1
                break;
            }

            if(opcao === 1 && oponente === 1){
                console.log('Você perdeu você escolheu Pedra e ele papel')
                voceperdeu += 1
                break;
            }

            if(opcao === 1 && oponente === 2){
                console.log('Você ganhou você escolheu Pedra e ele tesoura')
                voceganhou += 1
                break;
            }

            // papel

            if(opcao === 2 && oponente === 0){
                console.log('Você ganhou você escolheu Papel e ele pedra')
                voceganhou += 1
                break;
                
            }

            if(opcao === 2 && oponente === 1){
                console.log('Deu empate de Papel com Papel')
                empatou += 1
                break;
                
            }

            if(opcao === 2 && oponente === 2){
                console.log('Você perdeu você escolheu Papel e ele tesoura')
                voceperdeu += 1
                break;
            }

            // tesoura
            if(opcao === 3 && oponente === 0){
                console.log('Você perdeu você escolheu tesoura e ele pedra')
                voceperdeu += 1
                break;
            }

            if(opcao === 3 && oponente === 1){
                console.log('Você ganhou você escolheu tesoura e ele papel')
                voceganhou += 1
                break;
            }

            if(opcao === 3 && oponente === 2){
                
                console.log('Você empatou você escolheu tesoura e ele tesoura')
                empatou += 1
                break;
            }

        }
        prompt('Aperte ENTER para continuar')
        limpar()
    }

    if(resposta === 2){
        limpar()
        linha_x()
        console.log(`A regra é a seguinte
        1° Papel ganha da Pedra
        2° Pedra ganha da Tesoura 
        3° Tesoura ganha do Papel
        `)
        linha_x()
    }

    if(resposta === 3){
        limpar()
        console.log(`Você ganhou ${voceganhou} vezes, você perdeu ${voceperdeu} vezes e empatou ${empatou}`)
    }
    if(resposta === 4){
        console.log('Volte Sempre!!')
        break;
    }
    else{
    console.log('Esocolha uma das opções solicitadas')
    }
}

function linha_x(){
    console.log('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
}

function espaco(){
    console.log('')
}

function limpar(){
    console.clear()
}