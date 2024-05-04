import dorflex from '../assets/img/remedios/dorflex.jpeg'
import dipirona from '../assets/img/remedios/dipirona.jpg'
import multigripe from '../assets/img/remedios/multigrip.jpeg'
import eno from '../assets/img/remedios/eno.jpeg'
import cefalexina from '../assets/img/remedios/cefalexina.jpg'

import contonete from '../assets/img/higiene/contonete.webp'
import sabonete from '../assets/img/higiene/sabonte-em-pedra.jpeg'
import gilete from '../assets/img/higiene/gilete.webp'
import papelHigienico from '../assets/img/higiene/papel-higienico.jpg'
import absorvente from '../assets/img/higiene/absorvente.webp'

import Alcool from '../assets/img/primeirossocorros/Alcool-tupi-talco.jpg'
import Algodão from '../assets/img/primeirossocorros/algodão.png'
import esparadrapo from '../assets/img/primeirossocorros/esparadrapo.jpeg'
import gaze from '../assets/img/primeirossocorros/gaze.jpg'
import Termometro from '../assets/img/primeirossocorros/termometro.jpg'

import Assadura from '../assets/img/bebe/Assadura.jpg'
import Condicionador from '../assets/img/bebe/Condicionador.jpg'
import Shampoo from '../assets/img/bebe/Shampoo.jpg'
import Frauda from '../assets/img/bebe/Frauda.jpg'
import oleo from '../assets/img/bebe/hidratante.jpeg'

import xampu from '../assets/img/cabelo/xampu.jpg'
import condicionadorcap from '../assets/img/cabelo/condicionador.jpg'
import cremecapilar from '../assets/img/cabelo/cremecapilar.jpg'
import oleocapilar from '../assets/img/cabelo/óleocapilar.jpg'
import mascaracapilar from '../assets/img/cabelo/mascaracapilar.jpg'
const remedios = [
    {
        id: 1,
        nome: "Dorflex",
        categoria: "Antibióticos",
        imagem: dorflex,
        preco: 'R$ 7,00',
        descricao: `
        • Analgésico e relaxante muscular.
        • Composto por dipirona, paracetamol e cafeína\r. 
        • Indicado para dores musculares e de cabeça.`
    },
    {
        id: 2,
        nome: "Dipirona",
        categoria: "Antibióticos",
        imagem: dipirona,
        preco: 'R$ 7,00',
        descricao: `
        • Analgésico e antipirético.
        • Usado para alívio de dor e redução de febre.
        • Cuidado com reações alérgicas.`
    },
    {
        id: 3,
        nome: "Multigripe",
        categoria: "Antibióticos",
        imagem: multigripe,
        preco: 'R$ 17,00',
        descricao: `
        • Possivelmente referindo-se a um medicamento para gripe.
        • Pode conter ingredientes como paracetamol, descongestionantes, e antialérgicos.
        • Usado para alívio dos sintomas da gripe, como febre, dor e congestão nasal.`
    },

    {
        id: 4,
        nome: "Eno",
        categoria: "Antibióticos",
        imagem: eno,
        preco: 'R$ 20,00',
        descricao: `
        • Marca de antiácido efervescente.
        • Contém bicarbonato de sódio, ácido cítrico e carbonato de sódio.
        • Alivia rapidamente a azia e a indigestão.`
    },
    {
        id: 5,
        nome: "Cefalexina",
        categoria: "Antibióticos",
        imagem: cefalexina,
        preco: 'R$ 17,00',
        descricao: `
        • Antibiótico da família das cefalosporinas.
        • Trata infecções bacterianas.
        •Prescrição médica requerida.`

    },
]

const higiene = [
    {
        id: 1,
        nome: "Contonete",
        categoria: "Limpeza",
        imagem: contonete,
        preco: 'R$ 7,00',
        descricao: `
        • Haste de plástico ou madeira com algodão em cada ponta.
        • Usado para limpeza delicada do ouvido externo.`
    },
    {
        id: 2,
        nome: "Sabonete",
        categoria: "Limpeza",
        imagem: sabonete,
        preco: 'R$ 10,00',
        descricao: `
        • Produto de higiene pessoal.
        • Limpa a pele, removendo sujeira e bactérias.`
    },
    {
        id: 3,
        nome: "Gilete",
        categoria: "Limpeza",
        imagem: gilete,
        preco: 'R$ 5,00',
        descricao: `
        • Ferramenta de barbear.
        •  Lâmina afiada para remover pelos indesejados.`
    },
    {
        id: 4,
        nome: "Papel Higienico",
        categoria: "Limpeza",
        imagem: papelHigienico,
        preco: 'R$ 15,00',
        descricao: `
        • Papel macio usado para higiene pessoal após o uso do banheiro.
        • Disponível em rolos ou folhas.`
    },
    {
        id: 5,
        nome: "Absorvente",
        categoria: "Limpeza",
        imagem: absorvente,
        preco: 'R$ 7,00',
        descricao: `
        • Produto usado por mulheres durante o ciclo menstrual.
        • Absorve o fluxo menstrual.`
    },
]

const primeirossocorros = [
    {
        id: 1,
        nome: "Alcool",
        categoria: "Socorro",
        imagem: Alcool,
        preco: 'R$ 8,00',
        descricao: `
        • Líquido transparente e inflamável.
        • Desinfetante usado para limpeza e desinfecção.`
    },
    {
        id: 2,
        nome: "Algodão",
        categoria: "Socorro",
        imagem: Algodão,
        preco: 'R$ 5,00',
        descricao: `
        • Produto fibroso derivado do algodoeiro.
        • Usado em higiene pessoal e aplicação de medicamentos.
        `
    },
    {
        id: 3,
        nome: "Esparadrapo",
        categoria: "Socorro",
        imagem: esparadrapo,
        preco: 'R$ 15,00',
        descricao: `
        • Fita adesiva usada para fixar curativos e bandagens.
        • Disponível em diversas larguras.`
    },
    {
        id: 4,
        nome: "Gaze",
        categoria: "Socorro",
        imagem: gaze,
        preco: 'R$ 5,00',  
        descricao: `
        • Tecido fino e poroso.
        • Usado para cobrir e proteger feridas.`
    },
    {
        id: 5,
        nome: "Termometro",
        categoria: "Socorro",
        imagem: Termometro,
        preco: 'R$ 25,00',
        descricao: `
        • Dispositivo para medir temperatura corporal.
        • Disponível em modelos digital e de mercúrio.`
    },
]

const bebe = [
    {
        id: 1,
        nome: "Pomada para Assadura",
        categoria: "Socorro",
        imagem: Assadura,
        preco: 'R$ 50,00',
        descricao: `
        • Creme utilizado para prevenir e tratar assaduras na pele do bebê.
        • Contém ingredientes protetores e calmantes.`
    },
    {
        id: 2,
        nome: "Condicionador",
        categoria: "Socorro",
        imagem: Condicionador,
        preco: 'R$ 30,00',
        descricao: `
        • Produto de higiene para bebês.
        • Amacia e desembaraça os cabelos delicados dos bebês.`
    },
    {
        id: 3,
        nome: "Frauda",
        categoria: "Socorro",
        imagem: Frauda,
        preco: 'R$ 90,00',
        descricao: `
        • Item de higiene usado por bebês e pessoas com incontinência.
        • Absorve e retém urina e fezes.`
    },
    {
        id: 4,
        nome: "Shampoo",
        categoria: "Socorro",
        imagem: Shampoo,
        preco: 'R$ 40,00',  
        descricao: `
        • Produto de higiene para bebês.
        • Limpa suavemente os cabelos delicados dos bebês`
    },
    {
        id: 5,
        nome: "Óleo hidratante",
        categoria: "Socorro",
        imagem:  oleo,
        preco: 'R$ 45,00',
        descricao: `
        • Hidratante leve e suave para a pele do bebê.
        • Ajuda a manter a pele macia e hidratada.`
    },
]


const cabelo = [
    {
        id: 1,
        nome: "Shampoo",
        categoria: "Socorro",
        imagem: xampu,
        preco: 'R$ 30,00',
        descricao: `
        • Produto de higiene capilar.
        • Limpa o cabelo removendo sujeira e oleosidade.`
    },
    {
        id: 2,
        nome: "Condicionador",
        categoria: "Socorro",
        imagem: condicionadorcap,
        preco: 'R$ 30,00',
        descricao: `
        • Produto capilar usado após o xampu.
        • Amacia e desembaraça os cabelos.`
    },
    {
        id: 3,
        nome: "Creme",
        categoria: "Socorro",
        imagem: cremecapilar,
        preco: 'R$ 30,00',
        descricao: `
        • Produto para hidratação e cuidados com a pele.
        • Disponível em diversas formulações para diferentes necessidades.`
    },
    {
        id: 4,
        nome: "Óleo capilar",
        categoria: "Socorro",
        imagem: oleocapilar,
        preco: 'R$ 40,00',  
        descricao: `
        • Óleo leve usado para nutrir e dar brilho aos cabelos.
        
        • Ajuda a controlar o frizz e suavizar os fios.`
    },
    {
        id: 5,
        nome: "Mascara capilar",
        categoria: "Socorro",
        imagem:  mascaracapilar,
        preco: 'R$ 35,00',
        descricao: `
        • Tratamento intensivo para os cabelos.
        • Hidrata, nutre e fortalece os fios, podendo ter diversos objetivos específicos.`
    },
]
export {remedios, higiene, primeirossocorros, bebe, cabelo}