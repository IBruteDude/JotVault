import { Box, Stack, Typography } from '@mui/material';
import React from 'react';
import Navbar from './navbar';
import CustomButton from '../utils/customButton';

const Hero = () => {
	return (
		<Box
			sx={{
				height: '100vh',
				background: 'linear-gradient(180deg, #FEC097 0%, #FF9190 100%)',
			}}>
			<Navbar />
			<Stack
				justifyContent="center"
				alignItems="center"
				height="100%"
				textAlign="center"
				gap="3rem">
				<Typography
					variant="h1"
					color="white"
					fontSize={{ xs: '2.4rem', md: '4rem' }}
					fontWeight="700"
					width={{ xs: '100%', md: '65%' }}>
					Unleash Your Ideas, Capture Your Thoughts
				</Typography>
				<CustomButton
					fs="1.25rem"
					text="Get started now!"
					bgColor="var(--purple)"
					borderColor="var(--purple)"
					padding="0.7rem 3rem"
				/>
			</Stack>
		</Box>
	);
};

export default Hero;
