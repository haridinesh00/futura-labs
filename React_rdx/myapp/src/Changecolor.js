import React, { useState } from 'react'

function Changecolor() {
    const ran = Math.floor(Math.random() * 10);
    const shuffle = [
        "green",
        "orange",
        "red",
        "yellow",
        "purple",
        "blue",
        "maroon",
        "brown",
        "gray",
        "teal"
    ]
    const [first, second] = useState("white")
    const changecolor=()=>{second(shuffle[ran])}
    
  return (
    <div>
    <h1 style={{backgroundColor: first}}>Changecolor</h1>
    <button className='btn btn-primary' onClick={changecolor}>Change Color</button>
    </div>
  )
}

export default Changecolor