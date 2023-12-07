import { Box, Stack, Typography } from '@mui/material';
import React from 'react';
import { Link } from 'react-router-dom';

const Registration = ({ icon, text, header, form, option, theForm, path }) => {
	return (
		<Stack
			direction="row"
			height="100vh">
			{/* icon and text */}
			<Stack
				justifyContent="center"
				alignItems="center"
				sx={{
					background:
						' linear-gradient(180deg, #FEC097 42.81%, #FF9190 99.06%)',
					width: '50%',
				}}>
				<Stack
					gap="3rem"
					alignItems="center">
					<Box>{icon}</Box>
					<Typography
						variant="body1"
						sx={{
							textShadow: '0px 0px 5px #FFF',
							color: 'white',
							textAlign: 'center',
							width: '60%',
						}}>
						{text}
					</Typography>
				</Stack>
			</Stack>
			{/* Form */}
			<Stack
				justifyContent="center"
				alignItems="center"
				width={'50%'}
				sx={{
					background:
						' radial-gradient(50% 50% at 50% 50%, rgba(255, 255, 255, 0.38) 0%, rgba(254, 192, 151, 0.19) 100%)',
				}}>
				<Stack
					alignItems="center"
					width="100%"
					gap="1.4rem">
					<Typography
						variant="h2"
						fontWeight="700"
						color="var(--blue)">
						{header}
					</Typography>
					{form}
				</Stack>
				<Typography
					marginTop="1rem"
					variant="body1"
					textAlign="center"
					color="var(--dark-gray)">
					{option},{' '}
					<Link
						to={path}
						style={{ color: 'var(--blue)', fontWeight: 'bold' }}>
						{theForm}
					</Link>
				</Typography>
			</Stack>
		</Stack>
	);
};

export default Registration;
