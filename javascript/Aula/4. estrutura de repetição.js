// Atividade 1
console.log('Atividade 1')
for(p = 1; p <= 10; p++){
    console.log(p)
}

console.log('')

// Atividade 2
console.log('Atividade 2')
for(p = 1;p <= 10; p++){
    console.log(`7 x ${p} = ${7 * p}`)
}

console.log('')

// Atividade 3
console.log('Atividade 3')
soma_numeros_pares = 0

for(n = 2; n <= 10; n++ ){
    if (n % 2 === 0){
        soma_numeros_pares += n
        console.log(soma_numeros_pares)
    }
    
}

console.log('')
console.log('Desafio')

for(p = 1;p <= 10; p++){
    console.log('')
    console.log(`Tabuada ${p}`)
    for(v = 1;v <= 10; v++){
        console.log(`${p} x ${v} = ${p * v}`)
    }
}

console.log(' ')
sada = 0
console.log('Tentar entender qualquer coisa')
for(g = 1; g <= 10 ;g++){
    sada += 1
    console.log(`${g}² = ${g * g}`)
}

for(e = 1;e <= 10; e++){
    console.log('')
    console.log(`Tabuada ${e}²`)
    for(h = 1;h <= 10; h++){
        console.log(`${e}^${h} = ${e ** h}`)
    }
}

console.log(' ')
// Desafio Bonus
numerosimpar = 0
numerospares = 0
l = 12
console.log('Atividade Bônus')
for(let i = 1; i <= l; i++){ 
    if(i % 2 === 0){
        numerospares += 1
    }
    else{
        numerosimpar += 1
    }

    
    
} 
console.log(`Em uma contagem de 1 a ${l} temos ${numerospares} números pares e ${numerosimpar} números impares`)


console.log("")
console.log("coisa minha")

snumero = 1
snumero2 = 1
for(z = 1; z <= 10; z++){
    snumero += snumero2 = snumero
    
    console.log(z,`${snumero}`)
}
