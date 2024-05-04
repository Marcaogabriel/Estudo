import React from 'react'
import './button.css'
export default function Button({texto, onClick}) {
  return (
    <div>
      <button className='buttono' onClick={onClick}>{texto}</button>
    </div>
  )
}
