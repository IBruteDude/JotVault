import { Box, Stack, Typography } from '@mui/material';
import React from 'react';

const Heading = ({ text, subText }) => {
	return (
		<Box>
			<Stack
				textAlign="center"
				gap="0.5rem">
				<Typography
					variant="h3"
					fontSize="2.2rem"
					fontWeight="700"
					color="var(--purple)">
					{text}
				</Typography>
				{subText && (
					<Typography
						variant="body1"
						color="var(--gray)">
						{subText}
					</Typography>
				)}
			</Stack>
		</Box>
	);
};

export default Heading;
