import React from 'react';
import Registration from '../utils/registration';
import SignupForm from './signupForm';
import { icons } from '../utils/icons';

const Signup = () => {
	return (
		<>
			<Registration
				header="Sign up"
				icon={icons.signupIcon}
				text="Elevate your productivity and streamline your life with our intuitive note-taking platform. Effortlessly organize thoughts, boost creativity, and conquer tasks"
				form={<SignupForm />}
				option="Or if you already have an account"
				theForm="login now!"
				path="/login"
			/>
		</>
	);
};

export default Signup;
