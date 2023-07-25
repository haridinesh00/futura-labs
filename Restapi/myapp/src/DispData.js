import React, { useEffect, useState } from 'react'
import Button from 'react-bootstrap/esm/Button';
import Table from 'react-bootstrap/Table';

const baseurl ='http://127.0.0.1:8000'

function DispData() {
  const [first, setfirst] = useState([])
  useEffect(() => {
    fetch(baseurl+'/getdata').then(response=>response.json())
    .then(data=>setfirst(data))
    .catch(err=>console.log(err))
  }, [])
  console.log(first)
  const handleDelete = async (id) => {
    await fetch(`${baseurl}/district_delete/$(id)`, {
      method: "DELETE",
      headers: {
        ""
      }
    })
  }
  return (
    <div style={{marginLeft: "1vw", marginTop: "5vh", marginRight: "1vw"}}>
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>#</th>
          <th>Subject</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        {first.map((list,index)=>(
          <tr>
          <td key={index}>{index}</td>
          <td>{list.subject}</td>
          <td>{list.description}</td>
          <td><Button variant='danger' onClick={()=>handleDelete(list.id)}>Delete</Button></td>
        </tr>
        ))}
      </tbody>
    </Table>
    </div>
  )
}

export default DispData