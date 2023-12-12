import React from 'react';
import CustomTextField from '../utils/customTextField';
import styled from 'styled-components';
import SubmitButton from '../utils/submitButton';

const StyledForm = styled.form`
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 1rem;
	width: 47%;

	@media (max-width: 768px) {
		width: 75%;
	}
`;

const LoginForm = () => {
	return (
		<StyledForm>
			<CustomTextField
				name="email"
				type="email"
				placeholder="Email"
			/>
			<CustomTextField
				name="password"
				type="password"
				placeholder="Password"
			/>
			<SubmitButton />
		</StyledForm>
	);
};

export default LoginForm;
