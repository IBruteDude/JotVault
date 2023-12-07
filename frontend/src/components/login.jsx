import React from 'react';
import Registration from '../utils/registration';
import { icons } from '../utils/icons';
import LoginForm from './loginForm';

const Login = () => {
	return (
		<>
			<Registration
				header="Login"
				icon={icons.loginIcon}
				text="Capture inspiration on the go, organize thoughts effortlessly, and unleash your productivity – where every idea finds its perfect place."
				form={<LoginForm />}
				option="Or if you don't have account"
				theForm="Signup now!"
				path="/signup"
			/>
		</>
	);
};

export default Login;
