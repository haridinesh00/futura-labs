import React, { useEffect, useState } from "react";
import Button from "react-bootstrap/esm/Button";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
import './DispData.css';

const baseurl = "http://127.0.0.1:8000";

function formatDateAndTime(dateTimeString) {
  const [date, time] = dateTimeString.split("T");
  const formattedDate = date;
  const formattedTime = time;
  return `${formattedDate} : ${formattedTime}`;
}

function DispData() {
  const [first, setfirst] = useState([]);
  
  useEffect(() => {
    fetch(baseurl + "/getdata")
      .then((response) => response.json())
      .then((data) => {
        // Sort the data by pub_date in descending order
        const sortedData = data.sort((a, b) => {
          const dateA = new Date(b.pub_date);
          const dateB = new Date(a.pub_date);
          return dateA - dateB;
        });
        setfirst(sortedData);
      })
      .catch((err) => console.log(err));
  }, []);
  const handleDelete = async (id) => {
    await fetch(`${baseurl}/district_delete/${id}`, {
      method: "DELETE",
      headers: {
        "Content-type": "application/json",
      },
    });
    setfirst(first.filter((_list) => _list.id !== id));
  };
  
  return (
    <div className="container listed">
      <h1>ToDo List</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Subject</th>
            <th>Description</th>
            <th>Date and Time</th>
            <th>Actions</th> {/* Remove colSpan */}
          </tr>
        </thead>
        <tbody>
          {first.map((list, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{list.subject}</td>
              <td>{list.description}</td>
              <td>{formatDateAndTime(list.pub_date)}</td>
              <td className="button-cell">
                <Link to="/page3" state={{ id: list.id }}>
                  <Button variant="danger">Update</Button>
                </Link>
                <Button variant="danger" onClick={() => handleDelete(list.id)}>
                  Delete
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default DispData;
