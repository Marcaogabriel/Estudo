let produto = "Bolsa";
let quantidade = 1;;
let preçoUnitario = 100;
let incrementado = quantidade + 5;
let subirPreço = preçoUnitario * 1.1;

console.log("tinhamos "+ quantidade + ' ' + produto +" no estoque e recebemos uma remessa de 5 ficando com " + incrementado + " bolsas, por isso seu preço subiu em 10% ficando " + subirPreço.toFixed(2));