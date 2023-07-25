import React from 'react'
import { Card } from 'react-bootstrap'
import { Button } from 'react-bootstrap'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function bootcard() {
  const obj = {
    Name: "Hari",
    Age: 23,
    Gender: "Male",
    Place: "Kozhikode",
    Dob: "12-12-12"
}
    return (
      <div>
      <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#link">Link</Nav.Link>
            <NavDropdown title="Dropdown" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">
                Another action
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Separated link
              </NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
      <div style={{marginLeft: '5rem', marginTop: '5rem'}}>
      <Card style={{ width: '25rem', display: 'flex', flexDirection: 'row', borderRadius: '5px' }}>
        <Card.Img variant="top" src="https://www.industrialempathy.com/img/remote/ZiClJf-640w.avif" style={{width: '10rem', height: '8rem', marginTop: '1rem', marginLeft: '1rem', borderRadius: '5px'}} />
        <Card.Body style={{flex: 1}}>
          <Card.Title>{obj.Name}</Card.Title>
          <Card.Text>
            Gender: {obj.Gender}<br />
            Age: {obj.Age}<br />
            Place : {obj.Place}<br />
            Dob : {obj.Dob}
          </Card.Text>
        </Card.Body>
      </Card>
      </div>
      </div>
    );
  }

export default bootcard
