import React, { useState } from 'react'

function Changestr() {
  const [first,second] = useState("hello")
  const changename=()=>{second(first+"World")}
  return (
    <div>
      <h1>{first}</h1>
      <button onClick={changename}>Change</button>
    </div>
  )
}

export default Changestr