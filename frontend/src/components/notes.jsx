import React from 'react';
import DashboardHeading from '../utils/dashboardHeading';
import { Box, Stack } from '@mui/material';
import CustomInput from '../utils/customInput';
import NoteCard from '../utils/noteCard';
import ContentContainer from '../utils/contentContainer';

const Notes = () => {
	return (
		<ContentContainer>
			<Box>
				<DashboardHeading title="Notes" />
				<Stack
					direction="row"
					justifyContent="center">
					<CustomInput
						name="addNote"
						placeholder="Add a note..."
					/>
				</Stack>
				<Stack
					direction="row"
					flexWrap="wrap"
					gap="2rem">
					<NoteCard
						title={'Note title'}
						content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
						noteColor="var(--red)"
					/>
					<NoteCard
						title={'Note title'}
						content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
						noteColor="yellow"
					/>
					<NoteCard
						title={'Note title'}
						content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
						noteColor="var(--red)"
					/>
				</Stack>
			</Box>
		</ContentContainer>
	);
};

export default Notes;
