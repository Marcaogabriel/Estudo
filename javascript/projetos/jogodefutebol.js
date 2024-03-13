console.log('OLA AMIGOS BEM VINDOS AO')
let seusgols = 0
let golsrival = 0
times = ['Grêmio', 'Flamengo', 'Vitória', 'sport', 'Atlético Goianiense', 'Atlético Paranaense']
timesrival = ['Fortaleza', 'Fluminense', 'santa cruz', 'São Paulo', 'Botafogo', 'Bahia']
seutime = Math.random() * 5
timerival = Math.random() * 5
console.log(`Você é o time ${times[Math.round(seutime)]} e vai contra ${timesrival[Math.round(timerival)]}`)
console.log('')
console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
console.log(`COMEÇAAA O JOGO HOJE TEMOS ${times[Math.round(seutime)]} CONTRA ${timesrival[Math.round(timerival)]}`)
console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
console.log('')
chancesdegol(10)
function chancesdegol(tentativas){
     
    for(let numeral = 1; numeral <= tentativas;numeral++){
        console.log('')
        // Chance do rival
        console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        console.log(`time ${timesrival[Math.round(timerival)]}`)
        console.log('')
        let chancesdegoldorival = Math.random() * 100
        if(chancesdegoldorival > 60){
            console.log(`O time ${timesrival[Math.round(timerival)]} perde a posse de bola`)
            linha()
        }

        if(chancesdegoldorival > 40 && chancesdegoldorival <= 60){
            console.log(`O jogador recebeu um passe em profudidade e vai chutar de fora da area`)

            chutedeforarival = Math.random() * 100
            if(chutedeforarival >= 50){
                console.log(`A bola vai para fora e é tiro de meta`)
                linha()
            }

            if(chutedeforarival >= 20 && chutedeforarival < 50){
                console.log(`o goleiro defende e a bola vai para escanteio, será que sai gol?`)
                escanteiorival()
                linha()
            }

            if(chutedeforarival < 20){
                console.log(`GOLAÇOOOO DE FORA DA ÁREA`)
                golsrival += 1
                linha()
                placar()
            }
        }
        if(chancesdegoldorival > 30 && chancesdegoldorival <= 40){
           
            console.log('Vai ter um escanteio séra que sai gol?')
            escanteiorival()
            linha()
        }

        if(chancesdegoldorival > 20 && chancesdegoldorival <= 30){
            chutecaracararival = Math.random() * 100
            console.log('Ele recebe um passe e fica cara a cara com goleiro')
            if(chutecaracararival >= 70){
                console.log(`A bola vai para fora e é tiro de meta`)
                linha()
            }

            if(chutecaracararival >= 40 && chutecaracararival < 70){
                console.log(`Linda defesa do goleiro e a bola vai para escanteio será que sai gol?`)
                escanteiorival()
                linha()
            }

            if(chutecaracararival < 40){
                console.log(`GOLAÇOOOO ELE CHUTA NO CANTO DO GOLEIRO E MARCA UM LINDO GOL`)
                golsrival += 1
                linha()
                placar()
            }

        }

        if(chancesdegoldorival > 10 && chancesdegoldorival <= 20){
            chutedefaltarival = Math.random() * 100
            console.log('Vai ter uma Falta séra que sai gol?')
            if(chutedefaltarival >= 50){
                console.log(`A bola vai para fora e é tiro de meta`)
                linha()
            }

            if(chutedefaltarival >= 20 && chutedefaltarival < 50){
                barreirarival = Math.random() * 100
                if(barreirarival > 50){
                    console.log(`A bola bate na barreira e vai para escanteio será que sai gol?`)
                    escanteiorival()
                    linha()
                }
                else{
                    console.log(`linda defesa do goleiro e a bola vai para escanteio`)
                    escanteiorival()
                    linha()
                }
            }

            if(chutedefaltarival < 20){
                console.log(`GOLAÇOOOO DE FALTAAA`)
                golsrival += 1 
                linha()
                placar()
            }
         
        }

        if(chancesdegoldorival > 5 && chancesdegoldorival <= 10){
            Penaltirival = Math.random() * 100
            console.log('É PENALIDADE MAXIMA')
            if(Penaltirival >= 90){
                console.log(`Ele isola e perde a chance de golll`)
                linha()
            }

            if(Penaltirival >= 75 && Penaltirival < 90){
                console.log(`Linda defesa do goleiro e a bola vai para escanteio será que sai gol?`)
                escanteiorival()
                linha()
            }

            if(Penaltirival < 75){
                console.log(`GOLLLL e ele amplia o placar`)
                golsrival += 1
                linha()
                placar()
            }
        
        }

        if(chancesdegoldorival < 5){
            erradorival = Math.random() * 100
            console.log('O goleiro saiu errado')
            if(erradorival >= 95){
                console.log(`Ele a perde a chance de golll claraaa`)
                linha()
            }

            if(erradorival >= 90 && erradorival < 95){
                console.log(`O GOLEIRO DEPOIS DE FALHAR SALVAAA e a bola vai para escanteio será que sai gol?`)
                escanteiorival()
                linha()
            }

            if(erradorival < 90){
                console.log(`GOLLLL e ele amplia o placar com um erro do goleiro`)
                golsrival += 1
                linha()
                placar()
            }
        }

        // Chance do meu time
        console.log('')
        console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        console.log(`time ${times[Math.round(seutime)]}`)
        console.log('')
        let minhaschancesdegol = Math.random() * 100
        if(minhaschancesdegol > 60){
            console.log(`O time ${times[Math.round(seutime)]} perde a posse de bola`)
            linha()
        }
       
        if(minhaschancesdegol > 40 && minhaschancesdegol <= 60){
            console.log(`O jogador recebeu um passe em profudidade e vai chutar de fora da area`)
            chutedefora = Math.random() * 100
            if(chutedefora >= 50){
                console.log(`A bola vai para fora e é tiro de meta`)
                linha()
            }

            if(chutedefora >= 20 && chutedefora < 50){
                console.log(`o goleiro defende e a bola vai para escanteio, será que sai gol?`)
                escanteio()
                linha()
            }

            if(chutedefora < 20){
                console.log(`GOLAÇOOOO DE FORA DA ÁREA`)
                seusgols += 1
                linha()
                placar()
            }
        }
        if(minhaschancesdegol > 30 && minhaschancesdegol <= 40){
           
            console.log('Vai ter um escanteio séra que sai gol?')
            escanteio()
            linha()
        }

        if(minhaschancesdegol > 20 && minhaschancesdegol <= 30){
            chutecaracara = Math.random() * 100
            console.log('Ele recebe um passe e fica cara a cara com goleiro')
            if(chutecaracara >= 70){
                console.log(`A bola vai para fora e é tiro de meta`)
                linha()
            }

            if(chutecaracara >= 40 && chutecaracara < 70){
                console.log(`Linda defesa do goleiro e a bola vai para escanteio será que sai gol?`)
                escanteio()
                linha()
            }

            if(chutecaracara < 40){
                console.log(`GOLAÇOOOO ELE DRIBLA O GOLEIRO E MARCA UM LINDO GOL`)
                seusgols += 1
                linha()
                placar()
            }

        }

        if(minhaschancesdegol > 10 && minhaschancesdegol <= 20){
            chutedefalta = Math.random() * 100
            console.log('Vai ter uma Falta séra que sai gol?')
            if(chutedefalta >= 50){
                console.log(`A bola vai para fora e é tiro de meta`)
                linha()
            }

            if(chutedefalta >= 20 && chutedefalta < 50){
                barreira = Math.random() * 100
                if(barreira > 50){
                    console.log(`A bola bate na barreira e vai para escanteio será que sai gol?`)
                    escanteio()
                    linha()
                }
                else{
                    console.log(`linda defesa do goleiro e a bola vai para escanteio`)
                    escanteio()
                    linha()
                }
            }

            if(chutedefalta < 20){
                console.log(`GOLAÇOOOO DE FALTAAA`)
                seusgols += 1
                linha()
                placar()
            }
         
        }

        if(minhaschancesdegol > 5 && minhaschancesdegol <= 10){
            Penalti = Math.random() * 100
            console.log('É PENALIDADE MAXIMA')
            if(Penalti >= 90){
                console.log(`Ele isola e perde a chance de golll`)
                linha()
            }

            if(Penalti >= 75 && Penalti < 90){
                console.log(`Linda defesa do goleiro e a bola vai para escanteio será que sai gol?`)
                escanteio()
                linha()
            }

            if(Penalti < 75){
                console.log(`GOLLLL e ele amplia o placar`)
                seusgols += 1
                linha()
                placar()
            }
        
        }

        if(minhaschancesdegol < 5){
            errado = Math.random() * 100
            console.log('O goleiro saiu errado')
            if(errado >= 95){
                console.log(`Ele a perde a chance de golll claraaa`)
                linha()
            }

            if(errado >= 90 && errado < 95){
                console.log(`O GOLEIRO DEPOIS DE FALHAR SALVAAA e a bola vai para escanteio será que sai gol?`)
                escanteio()
                linha()
            }

            if(errado < 90){
                console.log(`GOLLLL e ele amplia o placar com um erro do goleiro`)
                seusgols += 1
                linha()
                placar()
            }
        }
        console.log('')
    }
}
if(seusgols < golsrival){
    console.log('')
        console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        console.log(`O JOGO ACABA COM A VITORIA DO ${timesrival[Math.round(timerival)]} POR ${golsrival} a ${seusgols} em cima do ${times[Math.round(seutime)]}`)
        console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        console.log('')
}

else if(seusgols > golsrival){
    console.log('')
        console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        console.log(`O JOGO ACABA COM A VITORIA DO ${times[Math.round(seutime)]} POR ${seusgols} a ${golsrival} em cima do ${timesrival[Math.round(timerival)]}`)
        console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        console.log('')
}

else{
    console.log('')
        console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        console.log(`O JOGO ACABA EMPATADO ${times[Math.round(seutime)]} ${seusgols}  ${timesrival[Math.round(timerival)]} ${golsrival}`) 
        console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        console.log('')
}

function escanteio(){
    goldeescanteio = Math.random() * 100
            if(goldeescanteio <= 25){
                console.log(`GOLLLLL de cabeça`)
                seusgols += 1
                placar()
            }
            else{
                console.log(`A bola vai para fora e é tiro de meta`)
            }
}

function escanteiorival(){
    goldeescanteiorival = Math.random() * 100
            if(goldeescanteiorival <= 25){
                console.log(`GOLLLLL de cabeça`)
                golsrival += 1
                placar()
            }
            else{
                console.log(`A bola vai para fora e é tiro de meta`)
            }
}

function placar(){
    console.log('')
    console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    console.log(`APÓS ESSE GOL O JOGO ESTÁ ${times[Math.round(seutime)]} ${seusgols} a ${timesrival[Math.round(timerival)]} ${golsrival}`)
    console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    console.log('')
}

function linha(){
    console.log('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
}