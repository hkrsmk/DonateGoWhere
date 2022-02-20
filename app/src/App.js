import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
// import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Header from './Header';
import Footer from './Footer';
import About from './About';
import Evaluate from './Evaluate';
import Contact from './Contact';
import Home from './Home';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

const theme = createTheme();

const sections = [
  { title: 'About', url: '/about' },
  { title: 'Evaluate', url: '/evaluate' },
  { title: 'Contact', url: '/contact' },
];

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg">
        <Header title="DonateGoWhere" sections={sections} />
      </Container>

      <Router>
        <Container maxWidth = "lg">
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/about" element={<About />} />
            <Route exact path="/evaluate" element={<Evaluate />} />
            <Route exact path="/contact" element={<Contact />} />
          </Routes>
        </Container>
      </Router>

      <Footer
        title="DonateGoWhere"
        description="Impact for your Buck"
        repoLink="https://github.com/hkrsmk/DonateGoWhere"
      />
    </ThemeProvider>
  );
}
