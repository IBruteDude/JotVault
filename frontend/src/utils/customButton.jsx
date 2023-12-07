import { Button } from '@mui/material';
import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const StyledButton = styled(Button)`
	&& {
		padding: ${(props) => props.padding};
		background-color: ${(props) => props.bgColor};
		color: white;
		border: 1px solid ${(props) => props.borderColor};
		border-radius: 10px;
		font-weight: bold;
		text-transform: unset;
		font-size: ${(props) => props.fs};
	}

	&&:hover {
		background-color: ${(props) => props.bgHover};
	}
`;
const CustomButton = ({
	text,
	bgColor,
	borderColor,
	bgHover,
	fs,
	padding,
	path,
}) => {
	return (
		<Link to={path}>
			<StyledButton
				variant="contained"
				disableElevation
				bgColor={bgColor}
				borderColor={borderColor}
				bgHover={bgHover || bgColor}
				fs={fs || 'auto'}
				padding={padding || '0.5rem 1rem'}>
				{text}
			</StyledButton>
		</Link>
	);
};

export default CustomButton;
