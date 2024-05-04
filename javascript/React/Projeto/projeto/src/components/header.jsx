import React from 'react'
import { useNavigate } from 'react-router-dom'
import { Input, Button } from '../components'
export default function Header() {
    const navigate = useNavigate()
  return (
    <div>
      <header className="header">
        <h1 onClick={() => navigate('/')}>Farmacia</h1>
        {/*<nav>*/}
          <Input />
          <Button onClick={() => navigate('/login')} texto="Login" />
        {/*</nav>*/}
      </header>
    </div>
  )
}
