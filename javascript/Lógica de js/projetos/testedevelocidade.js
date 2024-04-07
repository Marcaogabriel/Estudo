verificarvelocidade(190)

function verificarvelocidade(velocidade){
    velocidademaxima = 70
    kmporPonto = 5
    if (typeof velocidade !== 'number'){
        console.log('Confira se a velocidade é um número')
    }

    else if (velocidade <= 70){
        console.log('O carro está em uma velocidade ok')
    }

    else{
        const pontos = Math.floor(((velocidade - velocidademaxima) / kmporPonto))
        if (pontos >= 12){
            console.log('A sua carteira está suspensa')}
        else{
            console.log(`Você recebeu ${pontos} na carteira`)
        }
    }
    }
