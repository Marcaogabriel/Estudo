dia = 9
switch(dia){
    case 1:
    console.log(`Domingo é final de semana`);
    break;

    case 2:
    console.log(`Segunda-feira é dia util`);
    break;
    
    case 3:
    console.log(`Terça-feira é dia util`);
    break;

    case 4:
    console.log(`Quarta-feira é dia util`);
    break;
    
    case 5:
    console.log(`Quinta-feira é dia util`);
    break;

    case 6:
    console.log(`Sexta-feira é dia util`);
    break;
    
    case 7:
    console.log(`Sabado-feira é final de semana`);
    break;

    default:
    console.log('Data invalida, escreva um número entre 1 e 7')
}

let permissao;
permissao = 'gerente'
switch (permissao) {
    case 'comum':
    console.log('usuario comum');
    break;

    case 'gerente':
    console.log('usuario gerente ');
    break;

    case 'diretor':
    console.log('usuario diretor ');
    break;

    default:
    console.log('usuario Invalida, tente novamente')
}

let plano;
plano = 'plano vip'
switch (plano) {
    case 'plano gratis':
    console.log('Você escolheu o plano gratis então ficara pro R$0,0');
    break;

    case 'plano premium':
    console.log('Você escolheu o plano premium então ficara pro R$30,00');
    break;

    case 'plano vip':
    console.log('Você escolheu o plano vip então ficara pro R$60,00');
    break;

    default:
    console.log('usuario Invalida, tente novamente')
}


mes = 9
switch(mes){
    case 1:
    console.log(`o mês 1 é de Janeiro`);
    break;

    case 2:
    console.log(`o mês 2 é de Fevereiro`);
    break;
    
    case 3:
    console.log(`o mês 3 é de Março`);
    break;

    case 4:
    console.log(`o mês 4  é de Abril`);
    break;
    
    case 5:
    console.log(`o mês 5 é de maio`);
    break;

    case 6:
    console.log(`o mês 6 é de junho`);
    break;
    
    case 7:
    console.log(`o mês 7 é de julho`);
    break;

    case 8:
    console.log(`o mês 8 é de agosto`);
    break;

    case 9:
    console.log(`o mês 9 é de Setembro`);
    break;
    
    case 10:
    console.log(`o mês 10 é de Outubro`);
    break;

    case 11:
    console.log(`o mês 11 é de Novembro`);
    break;
    
    case 12:
    console.log(`o mês 12 é de Dezembro`);
    break;

    default:
    console.log('Escolha um número de mês entre 1 e 12')
}
 
let nota
nota = 6
switch(nota){
    case 0:
    console.log(`Conceito E`);
    break;

    case 1:
    console.log(`Conceito E`);
    break;

    case 2:
    console.log(`Conceito E`);
    break;

    case 3:
    console.log(`Conceito E`);
    break;

    case 4:
    console.log(`Conceito D`);
    break;
    
    case 5:
    console.log(`Conceito D`);
    break;

    case 6:
    console.log(`Conceito D`);
    break;

    case 7:
    console.log(`Conceito C`);
    break;

    case 8:
    console.log(`Conceito C`);
    break;

    case 9:
    console.log(`Conceito B`);
    break;  
    
    case 10:
    console.log(`Conceito A`);
    break;
    
    default:
    console.log(`a nota é entre 0 e 10`)
}

function classificarNota(nota) {
    let classificacao;
    switch (true) {
        case (nota >= 0 && nota <= 3):
            classificacao = "Rank E";
            break;
        case (nota >= 4 && nota <= 6):
            classificacao = "Rank D";
            break;
        case (nota >= 7 && nota <= 8):
            classificacao = "Rank C";
            break;
        case (nota == 9):
            classificacao = "Rank B";
            break;
        case (nota == 10):
            classificacao = "Rank A";
            break;
        default:
            classificacao = "Nota inválida";
    }   
    return classificacao;
}

console.log(classificarNota(2));  
console.log(classificarNota(5));  
console.log(classificarNota(7));  
console.log(classificarNota(9));  
console.log(classificarNota(10)); 
console.log(classificarNota(-1)); 



