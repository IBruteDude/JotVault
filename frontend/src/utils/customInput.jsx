import React from 'react';
import styled from 'styled-components';

const StyledInput = styled.input`
	width: 65%;
	padding: 1rem 1.5rem;
	font-size: 1rem;
	border-radius: 10px;
	box-shadow: 0px 0px 4px 0px rgba(0, 0, 0, 0.25);
	border: none;
	outline: none;
	margin-bottom: 3.5rem;
	&::placeholder {
		color: #a9a9a9;
	}
`;

const CustomInput = ({ name, placeholder }) => {
	return (
		<StyledInput
			type="text"
			name={name}
			placeholder={placeholder}
		/>
	);
};

export default CustomInput;
