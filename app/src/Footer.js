import * as React from 'react';
import PropTypes from 'prop-types';
import { Box, Container, Typography, Link } from '@mui/material/';

function Copyright() {
  return (
  <Typography variant="body2" colour="text.secondary" align="center">
  {'Copyright © '}
  <Link color="inherit" href="github.com/hkrsmk/charitysg">
  DonateGoWhere
  </Link>{' '}
  {new Date().getFullYear()}
  {'.'}
  </Typography>
  );
}

function Footer(props) {
  const { description, title } = props;

  return (
  <Box component="footer" sx={{ bgcolor: 'background.paper', py:6 }}>
  <Container maxWidth="lg">
  <Typography variant="h6" align="center" gutterBottom>
  {title}
  </Typography>
  <Typography
  variant ="subtitle1"
  align="center"
  color="text.secondary"
  component="p"
  >
  {description}
  </Typography>
  <Copyright />
  </Container>
  </Box>
  );
}

Footer.propTypes = {
  description: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
};

export default Footer;
