import { Typography } from '@mui/material';
import React from 'react';

const DashboardHeading = ({ title }) => {
	return (
		<Typography
			variant="h3"
			fontSize="32px"
			fontWeight="bold"
			color="var(--blue)">
			{title}
		</Typography>
	);
};

export default DashboardHeading;
