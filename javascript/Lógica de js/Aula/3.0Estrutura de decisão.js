let horario = 14.20

if (horario >= 6 && horario <= 11) {
    console.log("Atualmente são " + horario + " da manhã.")
}
else if (horario >= 12 && horario <= 17){
    console.log("Atualmente são " + horario + " da tarde")
}
else if (horario >= 18 && horario <= 23){
    console.log("Atualemente são " + horario + " da noite")
}
else{
    console.log("É madrugada vai dormir")
};

let media1 = 6
let media2 = 10
let media3 = 10
let media4 = 8
let media_geral = (media1 + media2 + media3 + media4) / 4

console.log(media_geral >= 8 ? "Uau "+ media_geral.toFixed(2) +" essa é uma ótima media anual" : 8 > media_geral && media_geral > 6 ? "Parabens! você passou de ano direto com a media " + media_geral.toFixed(2) + " ": "Você ficou de recuperação com a media "+ media_geral.toFixed(2))

console.log(media1 >= 6 ? "Parabens Você ficou acima da media com media "+ media1 + " " : "Estude mais você ficou abaixo da media com "+ media1)

let carro_na_rua = true;
if(carro_na_rua) console.log("Não atravessar")
else console.log("Atravessar")
