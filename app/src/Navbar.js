import About from './About';
import Evaluate from './Evaluate';
import Contact from './Contact';
import Home from './Home';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import React from 'react';

function Navbar(props) {
    return (
      <BrowserRouter>
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/about" element={<About />} />
            <Route exact path="/evaluate" element={<Evaluate />} />
            <Route exact path="/contact" element={<Contact />} />
          </Routes>
        </BrowserRouter>
    )
  }
  
export default Navbar;