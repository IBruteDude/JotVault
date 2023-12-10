import { Box, Stack } from '@mui/material';
import React from 'react';
import DashboardHeading from '../utils/dashboardHeading';
import CustomInput from '../utils/customInput';
import Task from '../utils/task';
import ContentContainer from '../utils/contentContainer';

const Tasks = () => {
	return (
		<ContentContainer>
			<Box>
				<DashboardHeading title="Tasks" />
				<Stack
					direction="row"
					justifyContent="center">
					<CustomInput
						name="addTask"
						placeholder="Add a task..."
					/>
				</Stack>
				<Stack
					direction="row"
					gap="1rem"
					justifyContent="center">
					<Task taskName="a7a" />
				</Stack>
			</Box>
		</ContentContainer>
	);
};

export default Tasks;
