import React from "react";
import { Table } from "react-bootstrap";

function Tableboot() {
  const obj = [
    {
      id: "1",
      firstname: "John",
      lastname: "Smith",
      username: "@johnsmith32",
    },
    {
      id: "2",
      firstname: "Hellen",
      lastname: "Smith",
      username: "@hellensmith22",
    },
    {
        id: "3",
        firstname: "Mary",
        lastname: "John",
        username: "@maryjohn",
      },
      {
        id: "4",
        firstname: "Jacob",
        lastname: "Miller",
        username: "@jacob",
      },
      {
        id: "5",
        firstname: "Tom",
        lastname: "Holland",
        username: "@tomholland",
      },
  ];
  return (
    <div className="container" style={{ marginTop: "5vh" }}>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Username</th>
          </tr>
        </thead>
        <tbody>
          {obj.map((i) => {
            return (
              <tr>
                <td>{i.id}</td>
                <td>{i.firstname}</td>
                <td>{i.lastname}</td>
                <td>{i.username}</td>
              </tr>
            );
          })}
        </tbody>
      </Table>
    </div>
  );
}

export default Tableboot;
