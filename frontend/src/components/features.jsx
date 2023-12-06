import { Box, Grid, Stack } from '@mui/material';
import React from 'react';
import Heading from '../utils/heading';
import FeatureCard from '../utils/featureCard';
import { icons } from '../utils/icons';
import { features } from '../data/featuresData';

const Features = () => {
	return (
		<Box className="add-margin">
			<Heading
				text="Features"
				subText="Experience the power of note-taking with our innovative features"
			/>
			<Grid
				justifyContent="center"
				container
				gap="1.7rem"
				padding="3rem 0rem">
				{features.map((feature) => {
					return (
						<Grid
							item
							height="100%"
							xs={12}
							md={6}
							lg={3}
							key={feature.id}>
							<FeatureCard
								icon={require(`../assets/images/${feature.path}`)}
								title={feature.title}
								text={feature.text}
							/>
						</Grid>
					);
				})}
			</Grid>
		</Box>
	);
};

export default Features;
