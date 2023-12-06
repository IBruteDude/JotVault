import { Box, Stack, Typography } from '@mui/material';
import React from 'react';
import Heading from '../utils/heading';

const About = () => {
	return (
		<Box
			margin="2rem 0"
			sx={{
				backgroundImage: `url(${require('../assets/images/circles.png')})`,
				backgroundSize: '90%',
				backgroundRepeat: 'no-repeat',
				backgroundPosition: 'center',
				// backgroundAttachment: 'fixed',
			}}>
			<Heading text="About Us" />
			<Stack
				justifyContent="center"
				alignItems="center"
				textAlign="center"
				height="70vh">
				<Typography
					variant="body1"
					width="60%">
					As a cohesive team, we bring together a blend of designers, front-end,
					and back-end developers. Collaboratively, we dedicated our efforts to
					construct this web app, aimed at simplifying the note-taking and task
					recording processes for a seamless user experience.
				</Typography>
			</Stack>
		</Box>
	);
};

export default About;
