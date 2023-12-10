import { Box, Stack } from '@mui/material';
import React from 'react';
import { icons } from './icons';

const Task = ({ taskName, taskColor }) => {
	return (
		<Stack
			direction="row"
			width="75%"
			padding="1rem 1.2rem"
			borderRadius="10px"
			justifyContent="space-between"
			alignItems="center"
			boxShadow="0px 0px 4px 0px rgba(0, 0, 0, 0.25)"
			backgroundColor={taskColor}>
			<Stack
				direction="row"
				alignItems="center"
				gap="1rem">
				<input
					type="checkbox"
					id={taskName}
				/>
				<label for={`${taskName}`}>{taskName}</label>
			</Stack>
			<Box>{icons.options}</Box>
		</Stack>
	);
};

export default Task;
