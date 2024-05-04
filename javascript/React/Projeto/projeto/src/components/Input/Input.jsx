import React from 'react'
import './input.css'
export default function Input() {
 function evento(e){
  alert('não implementado')
  e.preventDefault()
 }
  
  return (
    <div> 
        <form>
            <input type="text" className='input' />
        <button className='button' type="submit" onClick={evento} >P</button>
        </form>  
    </div>
  )
}
