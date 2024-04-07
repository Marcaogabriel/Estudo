const container = document.getElementById('container');
// nome do id
const button = document.getElementById('btn');

function clicar() {
const numeroaserchamado = Math.round(Math.random() * 100);
const numeroaserchamado1 = Math.round(Math.random() * 100);
const numeroaserchamado2 = Math.round(Math.random() * 100);

const usersArray = [
    {
        id: 1,
        nome: 'marcos',
        idade: 17,
        chamada: numeroaserchamado
    },

    {
        id: 2,
        nome: 'Kamila',
        idade: 18,
        chamada: numeroaserchamado1
    },

    {
        id: 3,
        nome: 'Shirley',
        idade: 47,
        chamada: numeroaserchamado2
    },

];

const ulist = document.getElementById("list");
const ulist20 = document.getElementById("list20");

usersArray.map((user, index) => {
    const li = document.createElement("li");
    li.textContent = `Nome: ${user.nome}  Idade: ${user.idade}  Você é o número${user.chamada}`;
    ulist.appendChild(li);
});
}

function clicar1() {

const ulist20 = document.getElementById("list20");
usersArray.map((user, index) => {
    const li = document.createElement("li");
    li.textContent = `Nome: ${user.nome},  Idade: ${user.idade + 20},  Você é o número  ${user.chamada}`;
    ulist20.appendChild(li);
});
}
