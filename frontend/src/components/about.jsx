import { Box, Stack, Typography } from '@mui/material';
import React from 'react';
import Heading from '../utils/heading';
import { icons } from '../utils/icons';
import Hossam from '../assets/images/Frame 1.png';
import Segun from '../assets/images/Frame 2.png';
import Kamar from '../assets/images/Frame 3.png';
import styled from 'styled-components';
const StyledImage = `
	position: absolute;
`;
const StyledHossamImage = styled.img`
	${StyledImage}
	top: 10%;
	left: 30%;
	@media (max-width: 768px) {
		top: unset;
		bottom: 8%;
		left: 59%;
	}
`;
const StyledSegunImage = styled.img`
	${StyledImage}
	bottom: 10%;
	right: 25%;

	@media (max-width: 768px) {
		bottom: unset;
		top: 16%;
		right: 28%;
	}
`;
const StyledKamarImage = styled.img`
	${StyledImage}
	bottom: 12%;
	left: 26%;
	@media (max-width: 768px) {
		bottom: 9%;
		left: 5%;
	}
`;
const About = () => {
	return (
		<Box
			id="about"
			margin="2rem 0"
			sx={{
				position: 'relative',
				// backgroundImage: `url(${require('../assets/icons/circles-background.svg')})`,
				backgroundSize: 'contain',
				backgroundRepeat: 'no-repeat',
				backgroundPosition: 'center',
				// backgroundAttachment: 'fixed',
				overflow: 'hidden',
			}}>
			<Box
				sx={{
					position: 'absolute',
					top: { xs: '5rem', md: '1rem' },
					left: { xs: '1rem', md: '5rem' },
					zIndex: '-1',
					width: '100%',
					height: '100%',
					overflow: 'hidden',
				}}>
				{icons.bg}
			</Box>
			<StyledHossamImage
				src={Hossam}
				alt="Hossam"
			/>
			<StyledSegunImage
				src={Segun}
				alt="Segun"
			/>
			<StyledKamarImage
				src={Kamar}
				alt="Kamar"
			/>
			<Heading text="About Us" />
			<Stack
				justifyContent="center"
				alignItems="center"
				textAlign="center"
				padding={{ xs: '9rem 0', md: '11rem 0' }}>
				<Typography
					variant="body1"
					width={{ xs: '95%', md: '60%' }}>
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
