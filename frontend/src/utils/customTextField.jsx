import React from 'react';
import styled from 'styled-components';

const StyledInput = styled.input`
	padding: 1rem 1.2rem;
	// border: 1px solid var(--blue);
	border: none;
	outline: none;
	box-shadow: 0 0 3px 1px rgba(0, 0, 0, 0.25);
	border-radius: 20px;
	background-color: transparent;
	width: 100%;
	color: var(--blue);
	transition: all 0.1s linear;
	&::placeholder {
		color: #a9a9a9;
	}
	&:focus {
		// transform: scale(1.1);
		box-shadow: 0 0 6px 5px rgba(255, 145, 144, 0.25);
	}
`;
const CustomTextField = ({ type, name, placeholder, restprops }) => {
	return (
		<StyledInput
			type={type}
			name={name}
			placeholder={placeholder}
			{...restprops}
		/>
	);
};

export default CustomTextField;
