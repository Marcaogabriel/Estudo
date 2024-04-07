const container = document.getElementById('container');
// nome do id
const button = document.getElementById('btn');

function clicar() {


const usersArray = [
    {
        id: 1,
        nome: 'marcos',
        idade: 17
    },

    {
        id: 2,
        nome: 'Kamila',
        idade: 18
    },

    {
        id: 3,
        nome: 'Shirley',
        idade: 47
    },

];

const ulist = document.getElementById("list");

usersArray.map((user, index) => {
    const li = document.createElement("li");
    li.textContent = `Nome: ${user.nome}  Idade: ${user.idade}`;
    ulist.appendChild(li);
});
}
