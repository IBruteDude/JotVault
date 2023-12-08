import {
	Route,
	RouterProvider,
	createBrowserRouter,
	createRoutesFromElements,
} from 'react-router-dom';
import './App.css';
import LandingPage from './components/landingPage';
import RootLayout from './pages/rootLayout';
import Login from './components/login';
import Signup from './components/signup';

const router = createBrowserRouter(
	createRoutesFromElements(
		<Route
			path="/"
			element={<RootLayout />}>
			<Route
				index
				element={<LandingPage />}
			/>
			<Route
				path="/login"
				element={<Login />}
			/>
			<Route
				path="/signup"
				element={<Signup />}
			/>
		</Route>
	)
);

function App() {
	return <RouterProvider router={router}></RouterProvider>;
}

export default App;
