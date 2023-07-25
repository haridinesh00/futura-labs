import React, { useEffect, useState } from 'react'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from 'axios'

const baseurl ='http://127.0.0.1:8000'

function AddData() {
    const [first, setfirst] = useState({
        "subject":"",
        "description":""
    })
    console.log(first)
    const handlechange = (event)=>{
        setfirst({
            ...first,
            [event.target.name]:event.target.value
        })
    }
    const submitform = (e)=>{
        e.preventDefault()
        const Districtdata = new FormData();
        Districtdata.append('subject',first.subject)
        Districtdata.append('description',first.description)
        try {
            axios.post(baseurl+'/district_add/',first).then((response)=>console.log(response.data))
        } catch (error) {
            console.log("error")
        }
    }
    useEffect(() => {
      document.title = 'Form Add'
    }, [])
    
  return (
    <div style={{marginTop: "5vh", marginLeft: "1vw", marginRight: "1vw"}}>
    <Form>
      <Form.Group className="mb-3" controlId="formBasic">
        <Form.Label>Subject</Form.Label>
        <Form.Control type="text" placeholder="Enter subject" onChange={handlechange} name="subject" value={first.subject} />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Label>Description</Form.Label>
        <Form.Control type="text" placeholder="Enter description" onChange={handlechange} name="description" value={first.description} />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Check me out" />
      </Form.Group>
      <Button onClick={submitform} variant="primary" type="submit">
        Submit
      </Button>
    </Form>
    </div>
  )
}

export default AddData