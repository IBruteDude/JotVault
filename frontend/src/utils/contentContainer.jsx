import { Box } from '@mui/material';
import React from 'react';

const ContentContainer = (props) => {
	return <Box padding="1.4rem 3.5rem">{props.children}</Box>;
};

export default ContentContainer;
