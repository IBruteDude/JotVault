import { Box, Stack, Typography } from '@mui/material';
import React from 'react';
import { icons } from '../utils/icons';
import HFooter from '../assets/images/h-footer.png';
import KFooter from '../assets/images/k-footer.png';
import SFooter from '../assets/images/s-footer.png';
const Footer = () => {
	return (
		<footer style={{ background: 'var(--red)' }}>
			<Box sx={{ padding: '4rem 5rem' }}>
				<Stack
					direction={{ xs: 'column', md: 'row' }}
					justifyContent="space-between"
					gap={{ xs: '2rem', md: 'unset' }}
					alignItems="center">
					<Box>{icons.footerLogo}</Box>
					<Stack
						gap="1.5rem"
						alignItems="center">
						<Typography
							variant="h5"
							fontSize="2rem"
							fontWeight="bold"
							color="white">
							Meet the team
						</Typography>
						<Stack
							direction={{ xs: 'column', md: 'row' }}
							gap={{ xs: '1.5rem', md: 'unset' }}>
							<Box>
								<img
									src={HFooter}
									alt="Hossam"
								/>
							</Box>
							<Box>
								<img
									src={KFooter}
									alt="Kamar"
								/>
							</Box>
							<Box>
								<img
									src={SFooter}
									alt="Segun"
								/>
							</Box>
						</Stack>
					</Stack>
				</Stack>
			</Box>
			<Stack>
				<Typography
					variant="caption"
					textAlign="center"
					color="white"
					fontSize="1rem">
					© All the rights reserved 2023
				</Typography>
			</Stack>
		</footer>
	);
};

export default Footer;
