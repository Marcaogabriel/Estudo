let ano = 2200

if(ano / 4 % 1) {
    console.log(`O ano ${ano} não é Bissexto`)
}

else{
    console.log(`O ano ${ano} é Bissexto`)
}

let ano2 = 2200

if(ano2 % 4 === 0 && ano2 % 100 === 0 && ano2 % 400 === 0){
    console.log(`${ano2} é Bissexto`)
}

else{
    console.log(`${ano2} não é bissexto`)
}