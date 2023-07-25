import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { increment, decrement } from './Slice'

function Counter() {
    const {value} = useSelector((a)=>a.counter)
    const dispatch = useDispatch()
  return (
    <div>
        <h1>{value}</h1>
        <button onClick={()=>dispatch(increment())}>+</button>
        <button onClick={()=>dispatch(decrement())}>-</button>
    </div>
  )
}

export default Counter