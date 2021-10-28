import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
// import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Header from './Header'
import Footer from "./Footer";

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
      <Footer
        title="DonateGoWhere"
        description="Impact for your Buck"
      />
    </ThemeProvider>
  );
}
