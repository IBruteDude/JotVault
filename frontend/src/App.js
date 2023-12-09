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
import DashboardLayout from './pages/dashboardLayout';
import Home from './components/home';
import Notes from './components/notes';

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
			<Route
				path="/dashboard"
				element={<DashboardLayout />}>
				<Route
					index
					element={<Home />}
				/>
				<Route
					path="/dashboard/notes"
					element={<Notes />}
				/>
			</Route>
		</Route>
	)
);

function App() {
	return <RouterProvider router={router}></RouterProvider>;
}

export default App;
