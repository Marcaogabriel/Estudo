function Nome(Nome){
    console.log('prazer '+ Nome )
}

Nome('Marcos')

function soma(numeros){
    console.log(numeros * 5)
}
soma(2)

function tabuada(tabuada){
    for(i = 1;i <= tabuada;i++ ){
        for(o = 1;o <= 10;o++ ){
            console.log(`${i} x ${o} = ${i * o}`)
        }
    }
} 
tabuada(5)

function areadoTriangulo(altura, base){
    area = (altura * base) / 2
    console.log(`Com a base de ${base} mutiplicado pela ${altura} divido por 2 a área é = ${area}`)
}
areadoTriangulo(3, 8)

function numeroPrimo(primo){
    if (numeroPrimo < 2){
        return false
    }
    for(i = 2; i < primo-1;i++)
        if(primo % i === 0){
            console.log('Não é primo')
            break
            
        }
        else{
            console.log('é primo')
        }
}
numeroPrimo(16)