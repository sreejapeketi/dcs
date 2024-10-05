import React from 'react'
import Header from '../header/header.jsx'
import Footer from '../footer/footer.jsx'
import Theme from '../home/theme.jsx'

function Home() {
  return (
    <div className='home'>
        <Header />
        <Footer />
        <button id="theme-toggle">Toggle Dark/Light Mode</button>
        <Theme />  
    </div>
  )
}

export default Home;
