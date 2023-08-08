import React from 'react';
import { Link } from 'react-router-dom';
import './WelcomePage.css'

function WelcomePage() {
  return (
    <div className="welcome-container">
      <h1>Welcome to ToDo App</h1>
      <p>This is a simple ToDo application.</p>
      <Link to="/page1">
        <button>Get Started</button>
      </Link>
    </div>
  );
}

export default WelcomePage;
