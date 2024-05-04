import React from 'react'
import { useNavigate, useLocation } from 'react-router-dom';
import Header from '../components/header';
import { Button } from '../components';
export default function Opcoes() {
  const navigate = useNavigate();
  const {state} = useLocation()
  
  return (
    <div>
     <Header/>
      <h1>Primeiros socorros:</h1>
      <Button className='fl-r' onClick={() => navigate(-1)} texto="Voltar"/>
          <section className='container'>
            {state.map((states) => (
                <article>
                  <div className=''>
                    <img onClick={() => navigate(`/item`, {state: states})} src={states.imagem} alt="" />
                    <h1>{states.nome}</h1>
                    <h3>{states.preco}</h3>
                  </div>    
                </article>
            ))}
          </section>
    </div>
  )
}
