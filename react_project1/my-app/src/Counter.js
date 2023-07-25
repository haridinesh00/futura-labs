import React, { useState } from 'react'

function Counter() {
  const [count,setcount] = useState(0)
  console.log(count)
  const incrementcounter=()=>{setcount(count+1)}
  const decrementcounter=()=>{setcount(count-1)}
  return (
    <div>
      <h1>{count}</h1>
      <button onClick={incrementcounter}>increase</button>
      <button onClick={decrementcounter}>decrease</button>
    </div>
  )
}

export default Counter