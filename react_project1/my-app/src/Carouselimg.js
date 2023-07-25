import React from 'react'
import Carousel from 'react-bootstrap/Carousel';

function Carouselimg() {
    const teams = [{name: "nature1", image: "https://www.industrialempathy.com/img/remote/ZiClJf-640w.avif"},
  {name: "nature2", image: "https://www.rd.com/wp-content/uploads/2020/04/GettyImages-1093840488-5-scaled.jpg"},
{name: "nature3", image: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Altja_j%C3%B5gi_Lahemaal.jpg/800px-Altja_j%C3%B5gi_Lahemaal.jpg"}]
return(
    <div>
        <Carousel>
          {
            teams.map((i)=>
            {
              return(
                <Carousel.Item>
                  <img
                    className="d-block w-100"
                    src={i.image}
                    alt="First slide"
                  />
                  <Carousel.Caption>
                    <h3>{i.name}</h3>
                  </Carousel.Caption>
                </Carousel.Item>
              )
            }
            )
          }
    </Carousel>
    </div>
  )
}

export default Carouselimg