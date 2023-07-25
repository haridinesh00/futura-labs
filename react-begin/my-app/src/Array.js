import React from 'react'

function Array() {
    const obj = {
        Name: "hari",
        Age: 23,
        Gender: "Male"
    }
  return (
    <div>
        <h1>{obj.Name}</h1>
        <p>{obj.Age}</p>
    </div>
  )
}

export default Array