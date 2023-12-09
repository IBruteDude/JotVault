import React from 'react';
import CustomTextField from '../utils/customTextField';
import styled from 'styled-components';
import SubmitButton from '../utils/submitButton';
import { Stack } from '@mui/material';

const StyledForm = styled.form`
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 1rem;
	width: 47%;

	@media (max-width: 768px) {
		width: 75%;
	}
	@media (min-width: 1024px) and (max-width: 1100px) {
		width: 80%;
	}
`;

const SignupForm = () => {
	return (
		<StyledForm>
			<Stack
				direction="row"
				gap="1rem">
				<CustomTextField
					name="fname"
					type="text"
					placeholder="First Name"
				/>
				<CustomTextField
					name="lname"
					type="text"
					placeholder="Last Name"
				/>
			</Stack>
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
			<CustomTextField
				name="password"
				type="password"
				placeholder="Re-Enter Password"
			/>
			<SubmitButton />
		</StyledForm>
	);
};

export default SignupForm;
