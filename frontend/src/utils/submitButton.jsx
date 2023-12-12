import { Button } from '@mui/material';
import React from 'react';
import styled from 'styled-components';

const StyledButton = styled(Button)`
	&& {
		padding: 0.7rem;
		color: white;
		border-radius: 20px;
		font-weight: bold;
		text-transform: unset;
		background-color: var(--blue);
		width: 100%;
		transition: all 0.2s linear;
	}
	&&:hover {
		background-color: #2c2471;
	}
`;
const SubmitButton = () => {
	return (
		<StyledButton
			type="submit"
			variant="contained">
			Submit
		</StyledButton>
	);
};

export default SubmitButton;
