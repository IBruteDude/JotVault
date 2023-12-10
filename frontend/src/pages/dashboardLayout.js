import { Box, Stack } from '@mui/material';
import React from 'react';
import { Outlet } from 'react-router-dom';

import Sidebar from '../components/sidebar';
import DashboardNavbar from '../components/dashboardNavbar';

const DashboardLayout = () => {
	return (
		<Stack direction="row">
			<Sidebar />
			<Box width="100%">
				<Stack>
					<DashboardNavbar />

					<Outlet />
				</Stack>
			</Box>
		</Stack>
	);
};

export default DashboardLayout;
