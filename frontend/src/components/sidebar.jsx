import { Box, Button, Stack, Typography } from '@mui/material';
import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import styled from 'styled-components';
import { icons } from '../utils/icons';

const StyledInput = styled.input`
	padding: 0.5rem 1rem;
	border-radius: 20px;
	outline: none;
	border: none;
	color: white;
	font-weight: bold;
	box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.25);
	background-color: transparent;
	font-size: 1rem;
`;

const Sidebar = () => {
	return (
		<Box>
			<Stack
				sx={{
					height: '100vh',
					alignItems: 'center',
					justifyContent: 'space-between',
					gap: '2rem',
					backgroundColor: 'var(--orange)',
					padding: '1rem 1.6rem',
					position: 'sticky',
					left: '0',
					top: '0',
					overflowY: 'auto',
				}}>
				<Box>
					<Link to="/">{icons.sidebarLogo}</Link>
				</Box>
				<Stack
					component="ul"
					alignItems="center"
					gap="2.2rem">
					<li>
						<NavLink to="/dashboard">{icons.home} Home</NavLink>
					</li>
					<li>
						<NavLink to="/dashboard/notes">{icons.note} Notes</NavLink>
					</li>
					<li>
						<NavLink to="/dashboard/tasks">{icons.task} Tasks</NavLink>
					</li>
					<li>
						<NavLink to="/dashboard/archive">{icons.archive} Archive</NavLink>
					</li>
					<li>
						<NavLink to="/dashboard/trash">{icons.trash} Trash</NavLink>
					</li>
				</Stack>
				<Stack
					gap="1rem"
					alignItems="center"
					height="40%">
					<Typography
						variant="h4"
						fontWeight="bold">
						Projects
					</Typography>
					<Stack
						gap="1rem"
						alignItems="center">
						<StyledInput
							type="text"
							name="project name"
							value="Project Name"
							readOnly
						/>
					</Stack>
					<Button
						variant="text"
						sx={{
							textTransform: 'none',
							alignSelf: 'flex-start',
							fontSize: '1rem',
							color: 'var(--light-blue)',
						}}>
						Add project +
					</Button>
				</Stack>
			</Stack>
		</Box>
	);
};

export default Sidebar;
