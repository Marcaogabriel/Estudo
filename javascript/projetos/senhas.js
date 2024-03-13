function gerarSenha(comprimento, incluirLetras, incluirNumeros, incluirSimbolos) {
    const letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numeros = '0123456789';
    const simbolos = '!@#$%^&*()-_+=~';
    let senha = '';
    let caracteres = '';
    if (incluirLetras == true) {
        caracteres += letras;
    }
    if (incluirNumeros == true) {
        caracteres += numeros;
    }
    if (incluirSimbolos == true) {
        caracteres += simbolos;
    }
    for (let i = 0; i < comprimento; i++) {
        const aleatorio = Math.floor(Math.random() * caracteres.length);
        senha += caracteres.charAt(aleatorio);
    }
    return senha;
}

const comprimento = 15;
const incluirLetras = true;
const incluirNumeros = true;
const incluirSimbolos = false;

const senhaGerada = gerarSenha(comprimento, incluirLetras, incluirNumeros, incluirSimbolos);
    console.log((incluirLetras == false && incluirNumeros == false && incluirSimbolos == false ) ? "Você precisa escolher uma das opções para gerar a senha": 'Senha Gerada:', senhaGerada);
