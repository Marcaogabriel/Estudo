const prompt = require("prompt-sync")({ sigint: true });
const cartas = ['A', 2, 3, 4, 5, 6, 7 , 8, 9, 'Q', 'J', 'K']
let voceganhou = 0
let voceperdeu = 0
let empate = 0
let terceira = false
let pegouaterceira = false
let pegouaquarta = false
let passoudolimite = false
let passoudolimiterival = false
while(true){
    linha_x()
    console.log(`MENU DO JOGO
[ 1 ] Jogar Blackjack
[ 2 ] Regras do Blackjack
[ 3 ] Placar
[ 4 ] Sair do jogo`)
linha_x()
espaco()
    let numero = prompt('Escolha uma opção: ')
    let resposta = Number(numero)

    if(resposta === 1){
        limpar()
        // Quais são as cartas
        console.log(`Então vamos começar os jogos`)
        primeiracarta = Math.round(Math.random() *  10)
        segundaacarta = Math.round(Math.random() *  10)
        primeiracartarival = Math.round(Math.random() *  10)
        segundaacartarival = Math.round(Math.random() *  10)
        
        // cartas
        prompt("Pressione ENTER para pegar as cartas.");
        espaco()
        limpar()
        linha()
        console.log(`As suas cartas são ${cartas[primeiracarta]} e ${cartas[segundaacarta]}`)
        linha()
        espaco()
        atribuir()

        // Analisar a regra das cartas A com K,J ou Q
        Analisarregrasua()
        Analisarregrarival()

        while(true){
            linha()
            let opcao = prompt('Deseja pegar outra carta? [ 1 ] sim   [ 2 ] não  ')
            linha()
            espaco()
            pergunta = Number(opcao)

            if(pergunta === 1){
                logicadepegarcartas()
                if(passoudolimite){
                    break;
                }
                logicadepegarcartasrival()
                if(passoudolimiterival){
                    break
                }
                // resultados
                decisao()
                break;
    
            }

            else if(pergunta === 2){
                linha_x()
                console.log('Então vamos continuar')
                linha_x()
                suascartas = cartas[primeiracarta] + cartas[segundaacarta]
                cartasdorival = cartas[primeiracartarival] + cartas[segundaacartarival]
                logicadepegarcartasrival()
                if(passoudolimiterival){
                    break
                }
                // resultados
                decisao()
                break;
              
            }

            else{
                console.log('Digite uma das opções')
            }
           
        }
        apagarhistorico()
        reatribuir()
        terceira = false
        passoudolimite = false
        passoudolimiterival = false
    }
    else if(resposta === 2){
        limpar()
        console.log(`Vou falar principios basicos para jogar: 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
1° Você precisa alcançar uma pontuação maior que a do seu rival
2° Você não pode utrapassar 21 pontos
3° Q, J, K valem 10 pontos  
4° Caso tire um Q ou J ou K juntamente com A os seus pontos se tornam 21 automaticamente
5° Caso tire um Q ou J ou K juntamente com A e pegue outra carta o A se torna 1
6° Pode tirar até 3 carta (sem contar as duas primeiras) para poder somar sua pontuação
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=`)
    }
    else if(resposta === 3){
        limpar()
        linha_x()
        console.log(`Você venceu ${voceganhou} vezes, perdeu ${voceperdeu} vezes e empatou ${empate} vezes`)
        linha_x()
       
    }
    else if(resposta === 4){
        console.log(`Volte sempre e até a próxima`)
        break
    }
    else{
        console.log('Digite uma das opções acima')
    }
}



function linha_x(){
    console.log('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

}

function linha(){
    console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
}

function espaco(){
    console.log('')
} 

function limpar(){
    console.clear()
}

function atribuir(){
        cartas[0] = 1
        cartas[9] = 10
        cartas[10] = 10
        cartas[11] = 10
}

function reatribuir(){
    cartas[0] = 'A'
    cartas[9] = 'Q'
    cartas[10] = 'J'
    cartas[11] = 'K'
}
function analisedoseulimite(){
    if(suascartas > 21){
        linha()
        console.log(`Você perdeu por passar do limite de quantidade de pontos vc ficou com ${suascartas}`)
        linha()
        espaco()
        passoudolimite = true
        voceperdeu += 1
    }
}

function analisarlimitedorival(){
    if(cartasdorival > 21){
        linha()
        console.log(`Você venceu pois seu oponente passou do limimte de pontos ele ficou com ${cartasdorival}`)
        linha()
        espaco()
        passoudolimiterival = true
        voceganhou += 1
    }
}
function decisao(){
    if(suascartas > 21){
        linha()
        console.log(`Você perdeu por passar do limite de quantidade de pontos vc ficou com ${suascartas}`)
        linha()
        espaco()
        voceperdeu += 1
    }
    if(cartasdorival > 21){
        linha()
        console.log(`Você venceu pois seu oponente passou do limimte de pontos ele ficou com ${cartasdorival}`)
        linha()
        espaco()
        voceganhou += 1
    }
    
    if(suascartas > cartasdorival && suascartas <= 21){
        linha()
        console.log(`Parabens você ganhou com sua pontuação de ${suascartas} a ${cartasdorival}`)
        linha()
        espaco()
        voceganhou += 1
        
    }
    if(suascartas < cartasdorival && cartasdorival <= 21){
        linha()
        console.log(`você perdeu com sua pontuação de ${suascartas} a ${cartasdorival}`)
        linha()
        espaco()
        voceperdeu += 1
        
    }
    if(suascartas === cartasdorival){
        linha()
        console.log(`Empate com sua pontuação de ${suascartas} a ${cartasdorival}`)
        linha()
        empate += 1
        espaco()
    }
}


function apagarhistorico(){
    while(true){
        esco = prompt('Deseja apagar o historico da partida? [ 1 ] Sim   [ 2 ] não   ')
        per = Number(esco)
        if(per === 1){
            limpar()
            break
        }
        else if(per === 2){
            break
        }
        else{
            console.log('Digite uma das opções')
        }
    }
}


function Analisarregrasua(){
    if(cartas[primeiracarta] === cartas[0] && cartas[segundaacarta] === cartas[9] || cartas[primeiracarta] === cartas[0] && cartas[segundaacarta] === cartas[10] || cartas[primeiracarta] === cartas[0] && cartas[segundaacarta] === cartas[11]){
        cartas[primeiracarta] = 11
    }

    if(cartas[segundaacarta] === cartas[0] && cartas[primeiracarta] === cartas[9] || cartas[segundaacarta] === cartas[0] && cartas[primeiracarta] === cartas[10] || cartas[segundaacarta] === cartas[0] && cartas[primeiracarta] === cartas[11]){
        cartas[segundaacarta] = 11
    }

    if(terceira === true && cartas[primeiracarta] ===  cartas[0]){
        cartas[primeiracarta] = 1
    } 

    if(terceira === true && cartas[segundaacarta] === cartas[0]){
        cartas[segundaacarta] = 1
    } 
}

function Analisarregrarival(){
    if(cartas[primeiracartarival] === cartas[0] && cartas[segundaacartarival] === cartas[9] || cartas[primeiracartarival] === cartas[0] && cartas[segundaacartarival] === cartas[10] || cartas[primeiracartarival] === cartas[0] && cartas[segundaacartarival] === cartas[11]){
        cartas[primeiracartarival] = 11
    }

    // K, J, Q com A
    if(cartas[segundaacartarival] === cartas[0] && cartas[primeiracartarival] === cartas[9] || cartas[segundaacartarival] === cartas[0] && cartas[primeiracartarival] === cartas[10] || cartas[segundaacartarival] === cartas[0] && cartas[primeiracartarival] === cartas[11]){
        cartas[segundaacartarival] = 11
    }

}

function logicadepegarcartasrival(){
    if(cartasdorival <= 13){
        terceiracartarival = Math.round(Math.random() *  11)
        cartasdorival += cartas[terceiracartarival]
        analisarlimitedorival()
        if(passoudolimite){
            return;
        }
        if(cartasdorival <= 15){
            quartacartarival = Math.round(Math.random() *  11)
            cartasdorival += cartas[quartacartarival]
            analisarlimitedorival()
            if(passoudolimite){
                return;
            }
            if(cartasdorival < 17){
                quintacartarival = Math.round(Math.random() *  11)
                cartasdorival += cartas[quintacartarival]
                analisarlimitedorival()
                if(passoudolimite){
                    return;
                }
            }
        }
        
    }
}

function logicadepegarcartas(){
    terceiracarta = Math.round(Math.random() *  10)
                terceira = true
                pegouaterceira = true
                Analisarregrasua()
                reatribuir()
                // terceira carta
                if(terceiracarta === 0){
                    linha()
                    console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]} e A`)
                    linha()
                    espaco()
                }
                else if(terceiracarta === 9){
                    linha()
                    console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]} e Q`)
                    linha()
                    espaco()
                }
                else if(terceiracarta === 10){
                    linha()
                    console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]} e J`)
                    linha()
                    espaco()
                }
                else if(terceiracarta === 11){
                    linha()
                    console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]} e K`)
                    linha()
                    espaco()
                }
                else{
                    linha()
                    console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]} e ${cartas[terceiracarta]}`)
                    linha()
                    espaco()
                }
                atribuir()
                suascartas = cartas[primeiracarta] + cartas[segundaacarta] + cartas[terceiracarta]
                analisedoseulimite()
                if(passoudolimite){
                    return;
                }
                cartasdorival = cartas[primeiracartarival] + cartas[segundaacartarival]
                while(true){
                    if(pegouaterceira){
                        linha()
                        let opcao1 = prompt('Deseja pegar outra carta? [ 1 ] sim   [ 2 ] não  ')
                        linha()
                        espaco()
                        pergunta1 = Number(opcao1)
                        // quarta carta
                        if(pergunta1 === 1){
                            reatribuir()
                            quartacarta = Math.round(Math.random() *  10)
                            pegouaquarta = true
                            

                            if(quartacarta === 0){
                                linha()
                                console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]} e A`)
                                linha()
                                espaco() 
                                atribuir()
                                suascartas += cartas[quartacarta]
                                analisedoseulimite()
                                if(passoudolimite){
                                return;
                            }
                                break 
                            }
                            else if(quartacarta === 9){
                                linha()
                                console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]} e Q`)
                                linha()
                                espaco()  
                                atribuir()
                                suascartas += cartas[quartacarta]
                                analisedoseulimite()
                                if(passoudolimite){
                                return;
                            }
                                break 
                            }
                            else if(quartacarta === 10){
                                linha()
                                console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]} e J`)
                                linha()
                                espaco() 
                                atribuir()
                                suascartas += cartas[quartacarta]
                                analisedoseulimite()
                                if(passoudolimite){
                                return;
                            }
                                break 
                            }
                            else if(quartacarta === 11){
                                linha()
                                console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]} e K`)
                                linha()
                                espaco() 
                                atribuir()
                                suascartas += cartas[quartacarta]
                                analisedoseulimite()
                                if(passoudolimite){
                                return;
                            }
                                break 
                            }
                            else{
                                linha()
                                console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]} e ${cartas[terceiracarta]} e ${cartas[quartacarta]}`)
                                linha()
                                espaco()  
                                atribuir()
                                suascartas += cartas[quartacarta]
                                analisedoseulimite()
                                if(passoudolimite){
                                return;
                            }
                                break
                            }
                        }
                        if(pergunta1 === 2){
                            return;
                        }
                        else{
                            console.log('Digite uma opção valida')
                        }
                    }   
                }

                        while(true){
                            if(pegouaquarta){
                                linha()
                                let opcao2 = prompt('Deseja pegar outra carta? [ 1 ] sim   [ 2 ] não  ')
                                linha()
                                espaco()
                                pergunta2 = Number(opcao2)
                                // quinta carta
                                if(pergunta2 === 1){
                                    reatribuir()
                                    carta4 = quartacarta
                                    let quintacarta = Math.round(Math.random() *  10)
                                    if(quintacarta === 0){
                                        linha()
                                        console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]}, ${cartas[carta4]} e A`)
                                        linha()
                                        espaco() 
                                        atribuir()
                                        suascartas += cartas[quintacarta]
                                        analisedoseulimite()
                                        if(passoudolimite){
                                        return;
                                    }
                                        break 
                                    }
                                    else if(quintacarta === 9){
                                        linha()
                                        console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]}, ${cartas[carta4]} e Q`)
                                        linha()
                                        espaco()
                                        atribuir()
                                        suascartas += cartas[quintacarta]
                                        analisedoseulimite()
                                        if(passoudolimite){
                                        return;
                                    } 
                                        break 

                                    }
                                    else if(quintacarta === 10){
                                        linha()
                                        console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]}, ${cartas[carta4]} e J`)
                                        linha()
                                        espaco()
                                        atribuir()
                                        suascartas += cartas[quintacarta]
                                        analisedoseulimite()
                                        if(passoudolimite){
                                        return;
                                    }
                                        break 

                                    }
                                    else if(quintacarta === 11){
                                        linha()
                                        console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]}, ${cartas[carta4]} e K`)
                                        linha()
                                        espaco() 
                                        atribuir()
                                        suascartas += cartas[quintacarta]
                                        analisedoseulimite()
                                        if(passoudolimite){
                                        return;
                                    }
                                        break 

                                    }
                                    else{
                                        linha()
                                        console.log(`Agora suas cartas são ${cartas[primeiracarta]} , ${cartas[segundaacarta]}, ${cartas[terceiracarta]}, ${cartas[carta4]} e ${cartas[quintacarta]}`)
                                        linha()
                                        espaco()
                                        atribuir()
                                        suascartas += cartas[quintacarta]
                                        analisedoseulimite()
                                        if(passoudolimite){
                                        return;
                                    } 
                                        break 

                                    }
                                
                                }
                                if(pergunta2 === 2){
                                    return;
                                }
                                else{
                                    console.log('Digite uma opção valida')
                                }
                            }   
                        }
                     
}
                



