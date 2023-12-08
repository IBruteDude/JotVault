import { Box, Stack } from '@mui/material';
import React, { useState } from 'react';
import { icons } from '../utils/icons';
import CustomButton from '../utils/customButton';
import styled from 'styled-components';

const StyledLi = styled.li`
	font-weight: 500;
`;

const StyledMenu = styled(Stack)`
	@media (max-width: 900px) {
		position: absolute;
		left: 0;
		top: 0;
		width: 100%;
		height: 50vh;
		background-color: #5e72eb;
		z-index: 1;
		gap: 5rem;
		border-bottom-right-radius: 100%;
		border-bottom-left-radius: 100%;
		transform: translate(-100%, -100%);
		transition: all 0.5s cubic-bezier(0.5, 0.5, 1, 0.5);

		&.active {
			height: 100vh;
			border-bottom-right-radius: 0;
			border-bottom-left-radius: 0;
			transform: translate(0, 0);
		}
	}
`;

const Navbar = () => {
	const [active, setActive] = useState(false);
	const handleMenu = () => {
		setActive(!active);
	};
	return (
		<Box
			component="nav"
			padding={{ xs: '1.5rem', md: '1.5rem 3.5rem' }}
			position="absolute"
			width="100%">
			<Stack
				direction="row"
				width="100%"
				alignItems="center"
				justifyContent={{ xs: 'space-between', md: 'unset' }}
				gap="2.3rem">
				<Box
					component={'a'}
					href="/"
					sx={{ cursor: 'pointer' }}>
					{icons.logo}
				</Box>
				<StyledMenu
					className={active ? 'active' : ''}
					direction={{ xs: 'column', md: 'row' }}
					width="100%"
					justifyContent={{ xs: 'center', md: 'space-between' }}
					alignItems="center">
					<Stack
						direction={{ xs: 'column', md: 'row' }}
						justifyContent={{ xs: 'space-between', md: 'unset' }}
						alignItems={{ xs: 'center', md: 'unset' }}
						component={'ul'}
						gap="2.3rem"
						color="white">
						<StyledLi>
							<a href="#hero">Home</a>
						</StyledLi>
						<StyledLi>
							<a href="#features">Features</a>
						</StyledLi>
						<StyledLi>
							<a href="#about">About</a>
						</StyledLi>
					</Stack>
					<Stack
						direction="row"
						justifyContent="center"
						gap="0.5rem">
						<CustomButton
							text="Sign up"
							bgColor="transparent"
							borderColor="var(--red)"
							bgHover="var(--red)"
							path="/signup"
						/>
						<CustomButton
							text="Log in"
							bgColor="var(--red)"
							borderColor="var(--red)"
							bgHover="transparent"
							path="/login"
						/>
					</Stack>
					<Box
						onClick={handleMenu}
						sx={{
							display: { xs: 'block', md: 'none' },
							position: 'absolute',
							top: '20px',
							right: '20px',
							cursor: 'pointer',
						}}>
						{icons.close}
					</Box>
				</StyledMenu>
				<Box
					sx={{ display: { xs: 'flex', md: 'none' }, cursor: 'pointer' }}
					onClick={handleMenu}>
					{icons.menu}
				</Box>
			</Stack>
		</Box>
	);
};

export default Navbar;
