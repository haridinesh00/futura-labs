import React from 'react'

function card_eg() {
  const obj = {
    Name: "hari",
    Age: 23,
    Gender: "Male"
}
  return (
    <div class="card">
  <img src="https://pixabay.com/photos/marguerite-daisy-flower-white-729510/" class="card-img-top" alt="..." />
  <div class="card-body">
    <h5 class="card-title">{obj.Name}</h5>
    <p class="card-text">{obj.Gender}, {obj.Age}</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
  )
}

export default card_eg