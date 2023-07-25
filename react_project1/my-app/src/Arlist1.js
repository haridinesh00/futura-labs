import React, { useState } from 'react'
import Arlist2 from './Arlist2'

function Arlist1() {
    const [obj1,obj2] = useState(
        [
            {name:"john",place:"Kozhikode"},
            {name:"Paul",place:"Thrissur"},
            {name:"Milly",place:"Wayanad"},
        ]
    )
    console.log(obj1)
  return (
    <div>
        <Arlist2 sample={obj1}/>
    </div>
  )
}

export default Arlist1