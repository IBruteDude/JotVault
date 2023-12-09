import { Box, Button, Stack, Typography } from '@mui/material';
import React from 'react';
import { Link, NavLink, Outlet } from 'react-router-dom';
import { icons } from '../utils/icons';
import styled from 'styled-components';

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

const StyledSearch = styled.input`
	outline: none;
	border: none;
	font-size: 1rem;
	width: 290px;

	&::placeholder {
		color: #aaa;
	}
`;

const DashboardLayout = () => {
	return (
		<Stack direction="row">
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
							<NavLink to="/dashboard">Home</NavLink>
						</li>
						<li>
							<NavLink to="/dashboard/notes">Notes</NavLink>
						</li>
						<li>
							<NavLink to="/dashboard/tasks">Tasks</NavLink>
						</li>
						<li>
							<NavLink to="/dashboard/archive">Archive</NavLink>
						</li>
						<li>
							<NavLink to="/dashboard/trash">Trash</NavLink>
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
			<Box width="100%">
				<Stack>
					<Box>
						<Stack
							direction="row"
							justifyContent="space-between"
							alignItems="center"
							padding="1.4rem 3rem"
							boxShadow=" -1px 3px 9px -3px rgba(0, 0, 0, 0.25)">
							<Stack
								direction="row"
								alignItems="center"
								gap="1rem">
								<Stack
									sx={{
										justifyContent: 'center',
										alignItems: 'center',
										padding: '0.8rem 1rem',
										borderRadius: '50%',
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
					<Box padding="1.4rem 3.5rem">
						<Outlet />
					</Box>
				</Stack>
			</Box>
		</Stack>
	);
};

export default DashboardLayout;
