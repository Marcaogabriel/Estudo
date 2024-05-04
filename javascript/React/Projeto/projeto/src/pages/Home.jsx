import React from 'react'
import { Header } from '../components'
import { useNavigate } from 'react-router-dom'
import { fremedio , fhigiene, fprimeirosSocorros, fbebe, fcabelo} from '../assets/img';
import { higiene, remedios, bebe, primeirossocorros, cabelo  } from '../database/database';
export default function Home() {
  const navigate = useNavigate();
  return (
    <div className=''>
     <Header/>
  
      <section className='home'>
        
        <h1 className='h1w100'>Produtos</h1>
          <article>
            <div>
              <img onClick={() => navigate('/opcoes', {state: remedios})} src={fremedio} alt="" /> 
              <h1>Remedios</h1>
            </div>
          </article>
          <article>
          <div>
            <img onClick={() => navigate('/opcoes', {state: higiene})} src={fhigiene} alt="" />
            <h1>Higiene Pessoal</h1>
          </div>              
          </article>
          <article>
            <div>
               <img onClick={() => navigate('/opcoes', {state: primeirossocorros})} src={fprimeirosSocorros} alt="" />
               <h1>Primeiros socorros</h1>
            </div>
          </article>
          <article>
            <div>
                <img onClick={() => navigate('/opcoes', {state: bebe})} src={fbebe} alt="" />
                <h1>Cuidados com Bebê</h1>
            </div>
          </article>
          <article>
            <div>
                <img onClick={() => navigate('/opcoes', {state: cabelo})} src={fcabelo} alt="" />
                <h1>Cuidados Cabelo</h1>
            </div>
          </article>
      </section>

      <footer>

      </footer>
    </div>
  )
}
