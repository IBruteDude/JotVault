import React from 'react';

import { Box } from '@mui/material';
import Hero from './hero';
import Features from './features';
import About from './about';
import Footer from './footer';

const LandingPage = () => {
	return (
		<Box>
			<Hero />
			<Features />
			<About />
			<Footer />
		</Box>
	);
};

export default LandingPage;
