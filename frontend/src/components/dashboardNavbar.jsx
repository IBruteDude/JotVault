import { Box, Button, Stack, Typography } from '@mui/material';
import React from 'react';
import { icons } from '../utils/icons';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const StyledSearch = styled.input`
	outline: none;
	border: none;
	font-size: 1rem;
	width: 290px;

	&::placeholder {
		color: #aaa;
	}
`;

const DashboardNavbar = () => {
	return (
		<Box>
			<Stack
				direction="row"
				justifyContent="space-between"
				alignItems="center"
				padding="1.4rem 3rem"
				boxShadow=" -1px 3px 9px -3px rgba(0, 0, 0, 0.25)">
				<Link to="/dashboard/profile">
					<Stack
						direction="row"
						alignItems="center"
						gap="1rem">
						<Stack
							sx={{
								justifyContent: 'center',
								alignItems: 'center',
								padding: '0.5rem',
								borderRadius: '50%',
								width: '50px',
								height: '50px',
								background:
									'radial-gradient(50% 50% at 50% 50%, rgba(255, 255, 255, 0.38) 0%, rgba(254, 192, 151, 0.19) 100%)',
							}}>
							{icons.user}
						</Stack>
						<Stack>
							<Typography
								variant="h6"
								color="var(--blue)"
								fontWeight="bold">
								Username
							</Typography>
							<Typography
								variant="body1"
								color="#aaa">
								Email
							</Typography>
						</Stack>
					</Stack>
				</Link>
				<Stack>
					<Stack
						direction="row"
						alignItems="center"
						gap="1rem"
						padding="0.7rem 1.2rem"
						border="1px solid var(--red)"
						borderRadius="50px">
						<Button
							variant="text"
							sx={{
								minWidth: 'unset',
								borderRadius: '50%',
							}}>
							{icons.search}
						</Button>
						<StyledSearch
							type="text"
							placeholder="Write the name of the title or ‘No title’"
						/>
					</Stack>
				</Stack>
			</Stack>
		</Box>
	);
};

export default DashboardNavbar;
