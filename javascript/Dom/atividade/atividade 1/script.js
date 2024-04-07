const usuarioFormulario = document.getElementById('formulario');   //Lista de formularios
const usuariomostrar = document.getElementById('lista');      //Lista de usuarios
let usuarios = [];         // array para armazenar

function renderusuariomostrar() {      // Mostra para o usuario
    usuariomostrar.innerHTML = '';      // Evitar que duplique ou misture usuarios
    usuarios.forEach((usuario, indice) => {      // é usado para percorrer a array usuario
        const li = document.createElement('li');    // Criar o elemento li  
        li.innerHTML = ` 
            <strong>Nome:</strong> ${usuario.name} | <strong>Email:</strong> ${usuario.email} | <strong>Idade: </strong>${usuario.idade} | <strong>Estado: </strong>${usuario.estado}
            <button onclick="Editarusuario(${indice})">Editar</button>
            <button onclick="traçarusuario(${indice})">Traçar</button>
            <button onclick="deletarusuario(${indice})">Excluir</button>
        `;                             //Foi usado para misturar o html e js, além disso para criar o botão de editar e excluir e suas funcionalidades
        usuariomostrar.appendChild(li);                // Adiciona o novo elemento na interface
    });
}

function tracarlinha() {      // traçar a linha
    usuariomostrar.innerHTML = '';      // Evitar que duplique ou misture usuarios
    usuarios.forEach((usuario, indice) => {      // é usado para percorrer a array usuario
        const li = document.createElement('li');    // Criar o elemento li  
        li.innerHTML = ` 
            <del><strong>Nome:</strong> ${usuario.name} | <strong>Email:</strong> ${usuario.email} | <strong>Idade: </strong>${usuario.idade} | <strong>Estado: </strong>${usuario.estado}</del> 
            <button onclick="Editarusuario(${indice})">Editar</button>
            <button onclick="tirartraço(${indice})">Retirar traço</button>
            <button onclick="deletarusuario(${indice})">Excluir</button>
        `;                             //Foi usado para misturar o html e js, além disso para criar o botão de editar e excluir e suas funcionalidades
        usuariomostrar.appendChild(li);                // Adiciona o novo elemento na interface
    });
}

usuarioFormulario.addEventListener('submit', function(event) {      // Adicionar o evento que ira acontecer e o submit server para quando clicar no botão acionar a função 
    event.preventDefault();        // Manter o cadastro e fazer junção com o submit
    const name = usuarioFormulario.name.value;      // Definir o nome com o seu valor
    const email = usuarioFormulario.email.value;       // Definir o email e seu valor
    const idade = usuarioFormulario.idade.value;          // Definira a idade e seu valor
    const estado = usuarioFormulario.estado.value;
    const usuario = {name, email, idade, estado};      // Usuario é o nome + email
    usuarios.push(usuario);      // Adicionar um novo item na array
    renderusuariomostrar();      // Renderizar para mostrar na tela
    usuarioFormulario.reset();      // Ele permite escrever na página sem precisar resetar ela
});



function Editarusuario(indice) { //Editar
    const troca = usuarios[indice]; // Define troca que vai recerber usuarios
    const novonome = prompt('Digite o novo nome:', troca.name); // Define que a troca do nome é uma nova variavel que sera atribuida pela nova array(troca)
    const novoemail = prompt('Digite o novo email:', troca.email); // Define que a troca do email é uma nova variavel que sera atribuida pela nova array(troca)
    const novaidade = prompt('Digite a nova idade', troca.idade);// Define que a troca da idade é uma nova variavel que sera atribuida pela nova array(troca)
    const novoestado = prompt('Digite a nova idade', troca.estado);
    if (novonome &&  novoemail && novaidade && novoestado) { // Caso for verdadeiro a troca
        usuarios[indice] = { name: novonome, email: novoemail, idade: novaidade, estado: novoestado}; // O array principal Usuarios ira receber a troca no lugar do antigo
        renderusuariomostrar(); // Renderizar para mostrar na tela
    }
}

function deletarusuario(indice) { // Apagar
    const confirmDelete = confirm('Tem certeza que deseja excluir este usuário?'); // confirmar se realmente quer apagar
    if (confirmDelete) { // Caso seja verade
        usuarios.splice(indice, 1); // O objeto clicado "o splice funciona(Qual objeto, qntd ex: 1, 2, 3...)"
        renderusuariomostrar(); // renderizar
    }
}

function traçarusuario() {   // deixar traçado
    tracarlinha(); // renderizar a linha traçada
}

function tirartraço(){ // retirar o traço
    renderusuariomostrar() // Renderizar a linha
}