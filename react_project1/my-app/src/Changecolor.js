import React, { useState } from 'react'

function Changecolor() {
    const [first, second] = useState("green")
    const changeblue=()=>{second("blue")}
    const changeyellow=()=>{second("yellow")}
    
  return (
    <div>
    <h1 style={{color: first}}>Changecolor</h1>
    <button className='btn btn-primary' onClick={changeblue}>Change Color</button>
    <button className='btn btn-primary' onClick={changeyellow}>Change Color</button>
    </div>
  )
}

export default Changecolor