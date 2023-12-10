import { Box, Stack } from '@mui/material';
import React from 'react';
import DashboardHeading from '../utils/dashboardHeading';
import CustomButton from '../utils/customButton';
import NoteCard from '../utils/noteCard';
import ContentContainer from '../utils/contentContainer';

const Home = () => {
	return (
		<ContentContainer>
			<Box>
				<DashboardHeading title="Home" />
				<Stack
					direction="row"
					alignItems="center"
					justifyContent="center"
					gap="1rem">
					<CustomButton
						bgColor="var(--orange)"
						borderColor="var(--orange)"
						padding="1.1rem 4rem"
						text="Add Note"
						fs="1rem"
						txtColor="var(--blue)"
					/>
					<CustomButton
						bgColor="var(--orange)"
						borderColor="var(--orange)"
						padding="1.1rem 4rem"
						text="Add Task"
						fs="1rem"
						txtColor="var(--blue)"
					/>
				</Stack>

				<Box marginTop="3rem">
					{/* <Stack
				justifyContent="center"
				alignItems="center">
				{' '}
				<Typography
					variant="body1"
					fontSize="3rem"
					color="#aaa"
					>
					There are no notes.
				</Typography>
			</Stack> */}
					<Stack
						direction="row"
						flexWrap="wrap"
						justifyContent="center"
						gap="2rem">
						<NoteCard
							title={'Note title'}
							content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
							noteColor="var(--red)"
						/>
						<NoteCard
							title={'Note title'}
							content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
							noteColor="var(--red)"
						/>
						<NoteCard
							title={'Note title'}
							content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
							noteColor="var(--red)"
						/>
						<NoteCard
							title={'Note title'}
							content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
							noteColor="var(--red)"
						/>
						<NoteCard
							title={'Note title'}
							content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
							noteColor="var(--red)"
						/>
						<NoteCard
							title={'Note title'}
							content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
							noteColor="var(--red)"
						/>
						<NoteCard
							title={'Note title'}
							content="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
							noteColor="var(--red)"
						/>
					</Stack>
				</Box>
			</Box>
		</ContentContainer>
	);
};

export default Home;
