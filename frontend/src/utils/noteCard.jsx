import { Box, Stack, Typography } from '@mui/material';
import React from 'react';
import { icons } from './icons';

const NoteCard = ({ title, content, noteColor }) => {
	return (
		<Box
			width="350px"
			borderRadius="10px"
			boxShadow="0px 0px 11px -2px rgba(0, 0, 0, 0.25)"
			backgroundColor={noteColor || 'white'}
			overflow="hidden">
			<Box padding="1.5rem 2rem">
				<Stack
					direction="row"
					alignItems="center"
					justifyContent="space-between"
					marginBottom="1rem">
					<Typography
						variant="h4"
						fontWeight="bold"
						color="var(--blue)">
						{title}
					</Typography>
					<Box>{icons.pin}</Box>
				</Stack>
				<Box>
					<Typography
						variant="body1"
						height="125px"
						overflow="hidden">
						{content}
					</Typography>
				</Box>
			</Box>
			<Stack
				direction="row"
				borderTop="1px solid rgba(13, 7, 69, 0.44)"
				padding="0.5rem 1.5rem"
				justifyContent="space-between"
				alignItems="center">
				<Stack
					direction="row"
					gap="1rem">
					<Box>{icons.archive}</Box>
					<Box>{icons.colors}</Box>
					<Box>{icons.image}</Box>
					<Box>{icons.trash}</Box>
				</Stack>
				<button
					style={{
						display: 'flex',
						backgroundColor: 'white',
						justifyContent: 'center',
						alignItems: 'center',
						borderRadius: '50%',
						padding: '0.5rem',
						border: '1px solid var(--blue)',
						cursor: 'pointer',
					}}>
					{icons.pen}
				</button>
			</Stack>
		</Box>
	);
};

export default NoteCard;
