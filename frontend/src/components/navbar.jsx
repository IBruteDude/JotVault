import { Box, Stack } from '@mui/material';
import React from 'react';
import { icons } from '../utils/icons';
import { NavLink } from 'react-router-dom';
import CustomButton from '../utils/customButton';
import styled from 'styled-components';

const StyledLi = styled.li`
	font-weight: 500;
`;

const Navbar = () => {
	return (
		<Box
			component="nav"
			padding="1.5rem 3.5rem"
			position="absolute"
			width="100%">
			<Stack
				direction="row"
				width="100%"
				alignItems="center"
				gap="2.3rem">
				<Box
					component={'a'}
					href="/"
					sx={{ cursor: 'pointer' }}>
					{icons.logo}
				</Box>
				<Stack
					direction="row"
					width="100%"
					justifyContent="space-between"
					alignItems="center">
					<Stack
						direction="row"
						component={'ul'}
						gap="2.3rem"
						color="white">
						<StyledLi>
							<a href="#">Home</a>
						</StyledLi>
						<StyledLi>
							<a href="#">Features</a>
						</StyledLi>
						<StyledLi>
							<a href="#">About</a>
						</StyledLi>
					</Stack>
					<Stack
						direction="row"
						gap="0.5rem">
						<CustomButton
							text="Sign up"
							bgColor="transparent"
							borderColor="var(--red)"
							bgHover="var(--red)"
						/>
						<CustomButton
							text="Log in"
							bgColor="var(--red)"
							borderColor="var(--red)"
							bgHover="transparent"
						/>
					</Stack>
				</Stack>
			</Stack>
		</Box>
	);
};

export default Navbar;
