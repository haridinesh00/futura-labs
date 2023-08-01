import React, { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from 'axios';
import './AddData.css'; // Import custom CSS file for styling

const baseurl = 'http://127.0.0.1:8000';

function AddData() {
  const [first, setfirst] = useState({
    subject: '',
    description: '',
  });

  const handlechange = (event) => {
    setfirst({
      ...first,
      [event.target.name]: event.target.value,
    });
  };

  const submitform = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(baseurl + '/district_add/', first);
      console.log(response.data);
    } catch (error) {
      console.log("error");
    }
  };

  useEffect(() => {
    document.title = 'Form Add';
  }, []);

  return (
    <div className="form-container"> {/* Add a custom class for container */}
      <h1 className="form-title">Add Item to List</h1>
      <Form className="my-form">
        <Form.Group controlId="formBasic">
          <Form.Label>Add Subject</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter subject"
            onChange={handlechange}
            name="subject"
            value={first.subject}
          />
          
        </Form.Group>

        <Form.Group style={{marginTop: "1rem"}}>
          <Form.Label>Add Description</Form.Label>
          <Form.Control
            as="textarea"
            placeholder="Enter description"
            onChange={handlechange}
            name="description"
            value={first.description}
            style={{ height: '100px' }}
          />
        </Form.Group>
        {/* <Form.Group controlId="formBasicCheckbox">
          <Form.Check type="checkbox" label="Check me out" />
        </Form.Group> */}
        <Button onClick={submitform} variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </div>
  );
}

export default AddData;
