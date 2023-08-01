import React, { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useLocation } from 'react-router-dom';
import axios from 'axios';

const baseurl = 'http://127.0.0.1:8000';

function UpdateData() {
  const [first, setFirst] = useState([]);
  const location = useLocation();
  const { id } = location.state;
  console.log(id);

  useEffect(() => {
    fetch(baseurl + '/getdata')
      .then((response) => response.json())
      .then((data) => setFirst(data))
      .catch((err) => console.log(err));
  }, []);

  const filteredData = first.filter((item) => item.id === id);

  const handlechange = (event) => {
    setFirst((prevData) =>
      prevData.map((item) =>
        item.id === id ? { ...item, [event.target.name]: event.target.value } : item
      )
    );
  };

  const handleUpdate = async (id) => {
    const dataToUpdate = filteredData.find((item) => item.id === id);
    try {
      await axios.put(`${baseurl}/district_update/${id}`, dataToUpdate);
      setFirst(first.filter((item) => item.id !== id));
    } catch (error) {
      console.error('Error updating data:', error);
    }
  };

  return (
    <div className="form-container" >
      <h2 className="form-title">Update Item</h2>
      {filteredData.map((list, index) => (
        <Form key={index}>
          <Form.Group className="mb-3" controlId="formBasic">
            <Form.Label>Subject</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter subject"
              onChange={handlechange}
              name="subject"
              value={list.subject}
            />
            
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Description</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter description"
              onChange={handlechange}
              name="description"
              value={list.description}
            />
          </Form.Group>
          <Button onClick={() => handleUpdate(list.id)} variant="primary" type="button">
            Submit
          </Button>
        </Form>
      ))}
    </div>
  );
}

export default UpdateData;
