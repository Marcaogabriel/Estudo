// saber se o número é primo
numero = 43
divisor = 0
for(i = 2; i <= numero-1; i++){
    if(numero === 1){
        console.log('Coloque um número acima de 1')
    }
    else if(numero % i === 0) {
        console.log(`O número ${numero} é divisivel por ${i}`)
        divisor += 1
    }  
}
if(divisor === 0){
    console.log(`O número ${numero} é primo`)
}
else{
    console.log(`O número ${numero} não é primo`)
}