//Escreva uma função chamada identificarNumero que recebe um valor como parâmetro e verifica se é um número positivo, negativo ou zero. Caso seja positivo, retorne "Número positivo". Caso seja negativo, retorne "Número negativo". Caso seja zero, retorne "Zero".

function identificarNumero(numero){
    if (numero > 0){
        console.log('Número positivo')
    }
    
    else if (numero < 0){
        console.log('Número negativo')
    }
    
    else{
        console.log('Neutro')
    }
}

identificarNumero(0)