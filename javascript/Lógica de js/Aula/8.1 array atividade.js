console.log('Primeira atividade (Facil)')
let somar = [1, 2, 3, 4, 5]
soma = 0
for(let i = 0; i < somar.length; i++){
    soma += somar[i]
}
console.log(soma)

console.log('')
console.log('Segunda atividade (Facil)')

let nota = [8, 7, 9, 8]
somadamedia = 0
for(let a = 0; a < nota.length; a++){
    somadamedia += nota[a]
}
console.log(`A media de suas notas é ${somadamedia / nota.length}`)

console.log('')
console.log('Primeira atividade (Medio)')

function NumerosPares(resto) {
    let numerosPares = [];
    for (let v = 0; v < resto.length; v++) {
        if (resto[v] % 2 === 0) {
            numerosPares.push(resto[v]);
        }
    }
    return numerosPares;
}

let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 123, 123, 7654, 214];
let numerosPares = NumerosPares(numeros);
console.log(numerosPares); 



console.log('')
console.log('Segunda atividade (Medio)')

function ordenar(array) {
    for (let i = 0; i < array.length - 1; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] > array[j]) {
                let temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
    return array;
}

let minhaArray = [5, 2, 7, 1, 9, 3];
console.log(ordenar(minhaArray));


console.log('')
console.log('Primeira atividade (Dificil)')

abc = [1, 2, 3]
def = [4, 5, 6]
somado1 = 0
for(h = 0; h < abc.length;h++){
    somado1 += abc[h] * def[h]
}
console.log(somado1)