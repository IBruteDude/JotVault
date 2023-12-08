import React from 'react';
import { Outlet } from 'react-router-dom';

const RootLayout = () => {
	return (
		<div className="App">
			<Outlet />
		</div>
	);
};

export default RootLayout;
