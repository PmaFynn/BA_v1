import React from 'react'
import { Link, useMatch, useResolvedPath } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav className='nav'>
        <Link to='/' className='site-title'> Testwebsite </Link>
        <ul>
          <CustomLink to='/pricing' id='1234'>Pricing</CustomLink>
          <CustomLink to='/about' id='12345'>About</CustomLink>
        </ul>
    </nav>
  )
}

function CustomLink( {to, children, ...props} ){
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({path: resolvedPath.pathname, end: true})
  return (
    <li className={ isActive ? "active" : "" }>
      <Link to={to} {...props}>
        {children}
        </Link>
    </li>
  )
}