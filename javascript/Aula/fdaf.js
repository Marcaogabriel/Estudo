let nota = 4;
let conceito;


switch (nota) {
    case (nota > 0 && nota <= 3):
        conceito = "Conceito E";
        break;

    case (nota >= 4 && nota <=6):
        conceito = "Conceito D";
        break;

    case (nota > 6 && nota <=8):
        conceito = "Conceito C";
        break;

    case (nota = 9):
        conceito = "Conceito B";
        break;

    case (nota = 10):
        conceito = "Conceito  A";
        break;

    default:
        conceito = "Nota Inválida";

}
console.log(conceito);