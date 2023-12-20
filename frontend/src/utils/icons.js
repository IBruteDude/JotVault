import { ReactComponent as Logo } from '../assets/icons/JotVault.svg';
import { ReactComponent as NWC } from '../assets/icons/note-with-cover.svg';
import { ReactComponent as TWC } from '../assets/icons/task-with-cover.svg';
import { ReactComponent as PWC } from '../assets/icons/project-with-cover.svg';
import { ReactComponent as FooterLogo } from '../assets/icons/JotVault-footer.svg';
import { ReactComponent as Menu } from '../assets/icons/bars-solid.svg';
import { ReactComponent as Close } from '../assets/icons/xmark-solid.svg';
import { ReactComponent as BG } from '../assets/icons/circles-background.svg';
import { ReactComponent as LoginIcon } from '../assets/icons/undraw_taking_notes_re_bnaf 1.svg';
import { ReactComponent as SignupIcon } from '../assets/icons/undraw_design_notes_re_eklr 1.svg';
import { ReactComponent as SidebarLogo } from '../assets/icons/JotVault-sidebar.svg';
import { ReactComponent as User } from '../assets/icons/user-solid 1.svg';
import { ReactComponent as Search } from '../assets/icons/magnifying-glass-solid.svg';
import { ReactComponent as Pin } from '../assets/icons/thumbtack-solid.svg';
import { ReactComponent as Archive } from '../assets/icons/box-archive-solid.svg';
import { ReactComponent as Colors } from '../assets/icons/palette-solid.svg';
import { ReactComponent as Image } from '../assets/icons/image-solid.svg';
import { ReactComponent as Trash } from '../assets/icons/trash-solid.svg';
import { ReactComponent as Pen } from '../assets/icons/pen-solid.svg';
import { ReactComponent as Options } from '../assets/icons/ellipsis-vertical-solid.svg';
import { ReactComponent as Home } from '../assets/icons/house-solid.svg';
import { ReactComponent as Note } from '../assets/icons/note-sticky-solid.svg';
import { ReactComponent as Task } from '../assets/icons/tasks-vector.svg';

export const icons = {
	logo: <Logo />,
	menu: <Menu />,
	close: <Close />,
	nwc: <NWC />,
	twc: <TWC />,
	pwc: <PWC />,
	footerLogo: <FooterLogo />,
	bg: <BG />,
	loginIcon: <LoginIcon />,
	signupIcon: <SignupIcon />,
	sidebarLogo: <SidebarLogo />,
	user: (
		<User
			width="inherit"
			height="inherit"
		/>
	),
	search: <Search />,
	pin: <Pin />,
	archive: <Archive />,
	colors: <Colors />,
	image: <Image />,
	trash: <Trash />,
	pen: <Pen />,
	options: <Options />,
	home: <Home />,
	note: <Note />,
	task: <Task />,
};
