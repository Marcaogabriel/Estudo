import React from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { Button, Header } from '../components'
export default function Item() {
  const {state} = useLocation()
  const navegate = useNavigate()
  return (
    <div>
      <Header/>
      <div className='caixa'>
          <div>
            <img className="h100w50" src={state.imagem} alt="" />
            <p><h2>{state.nome}</h2></p>
            <p><h2>{state.preco}</h2></p>
            <h5>{state.descricao}</h5>
            <Button onClick={() => navegate('/carrinho', {state: state})} texto="Comprar" />
            <br />
            <Button onClick={() => navegate(-1)} texto="Voltar" />
          </div> 
      </div>
    </div>
    
  )
}
