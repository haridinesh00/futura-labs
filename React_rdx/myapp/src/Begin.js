import React from 'react'

function Begin() {
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
  return (
    <h1>{shuffle[ran]}</h1>
  )
}

export default Begin