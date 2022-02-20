import * as React from 'react';
import PropTypes from 'prop-types';
import { Box, Container, IconButton, Stack, Typography } from '@mui/material/';
import GitHubIcon from '@mui/icons-material/GitHub';

function Copyright() {
  return (
  <Typography variant="body2" colour="text.secondary" align="center">
  {'Copyright © DonateGoWhere '}
  {new Date().getFullYear()}
  {'.'}
  </Typography>
  );
}

function Footer(props) {
  const { description, title, repoLink } = props;

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

      <Stack
        direction="row"
        justifyContent="center"
        alignItems="center"
        spacing={1}
      >     
        <Copyright />

        <IconButton 
          aria-label="Link to github repository"
          href={repoLink}
          target="_blank"
        >
            <GitHubIcon />
        </IconButton>
      
      </Stack>

    </Container>
  </Box>
  );
}

Footer.propTypes = {
  description: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  repoLink: PropTypes.string.isRequired
};

export default Footer;