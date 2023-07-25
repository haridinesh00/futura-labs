import React from 'react'

const Arlist2 = (props) => {
    const eg = props.sample;
    console.log(props,eg)
  return (
    <div>
        {
            eg.map((i)=>(
                <>
                <h1>Name: {i.name}</h1>
                <h1>Place: {i.place}</h1>
                </>
            ))
        }
    </div>
  )
}

export default Arlist2