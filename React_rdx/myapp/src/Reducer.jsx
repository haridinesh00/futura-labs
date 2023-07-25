import React, { useReducer } from 'react'

const initialstate=20
const reducer = (state,action)=>{
    return newstate
}

function Reducer() {
    const [state, dispatch] = useReducer(reducer,initialstate)
  return (
    <div>
        <h3>{state}</h3>
    </div>
  )
}

export default Reducer