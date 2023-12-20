import { Box, Stack, Typography } from '@mui/material';
import React from 'react';
import { icons } from '../utils/icons';
import ContentContainer from '../utils/contentContainer';
import CustomTextField from '../utils/customTextField';

const Profile = () => {
	return (
		<Box>
			<Stack
				direction="row"
				borderBottom="1px solid #aaa">
				<Stack
					direction="row"
					alignItems="center"
					gap="1rem"
					padding="3rem 5rem">
					<Box
						width="200px"
						height="200px"
						padding="2rem"
						borderRadius="50%"
						sx={{
							background:
								'radial-gradient(50% 50% at 50% 50%, rgba(255, 217, 194, 0.38) 0%, rgba(255, 143, 69, 0.19) 100%)',
						}}>
						{icons.user}
					</Box>
					<Stack>
						<Typography
							variant="h3"
							fontWeight="bold"
							color="var(--blue)">
							UserName
						</Typography>
						<Typography
							variant="body1"
							fontSize="1.3rem">
							Email
						</Typography>
					</Stack>
				</Stack>
			</Stack>
			<ContentContainer>
				<Stack gap="1rem">
					<Stack
						direction="row"
						alignItems="center"
						gap="1rem">
						<label style={{ width: '90px' }}>First Name</label>
						<Box width="30%">
							<CustomTextField
								name="fname"
								placeholder="User's first name"
								type="text"
							/>
						</Box>
					</Stack>

					<Stack
						direction="row"
						gap="1rem"
						alignItems="center">
						<label style={{ width: '90px' }}>Last Name</label>
						<Box width="30%">
							<CustomTextField
								name="lname"
								type="text"
								placeholder="User's last name"
							/>
						</Box>
					</Stack>
					<Stack
						direction="row"
						gap="1rem"
						alignItems="center">
						<label style={{ width: '90px' }}>Email</label>
						<Box width="30%">
							<CustomTextField
								name="email"
								type="email"
								placeholder="User's email"
							/>
						</Box>
					</Stack>
					<Stack
						direction="row"
						gap="1rem"
						alignItems="center">
						<label style={{ width: '90px' }}>Password</label>
						<Box width="30%">
							<CustomTextField
								name="password"
								type="password"
								placeholder="Password"
								restprops={{ readOnly: true }}
							/>
						</Box>
					</Stack>
				</Stack>
			</ContentContainer>
		</Box>
	);
};

export default Profile;
