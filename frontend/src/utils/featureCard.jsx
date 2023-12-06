import { Box, Stack, Typography } from '@mui/material';
import React from 'react';

const FeatureCard = ({ icon, title, text }) => {
	return (
		<Box
			padding="2.5rem 1.6rem"
			borderRadius="20px"
			boxShadow="0px 0px 5px 1px rgba(0, 0, 0, 0.25)">
			<Stack
				gap={'1.3rem'}
				textAlign="center">
				<Box>
					<img
						src={icon}
						alt=""
					/>
				</Box>
				<Typography
					variant="h5"
					fontWeight="bold"
					color="var(--purple)">
					{title}
				</Typography>
				<Typography
					variant="body1"
					color="var(--dark-gray)">
					{text}
				</Typography>
			</Stack>
		</Box>
	);
};

export default FeatureCard;
