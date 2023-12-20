import React from 'react';
import DashboardHeading from '../utils/dashboardHeading';
import { Box } from '@mui/material';
import ContentContainer from '../utils/contentContainer';

const Trash = () => {
	return (
		<ContentContainer>
			<Box>
				<DashboardHeading title="Trash" />
			</Box>
		</ContentContainer>
	);
};

export default Trash;
