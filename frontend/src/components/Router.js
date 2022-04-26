import HomePage from '../views/home';
import InputPage from '../views/in';
import SettingsPage from '../views/settings';
import ErrorPage from '../views/error';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

const WebsiteRouter = () => {
    return (
        <Router>
            <div id="fixed-body-content">
                <Routes>
                    <Route path="/settings" element={<SettingsPage />} />
                    <Route path="/in" element={<InputPage />} />
                    <Route path="/" element={<Home />} />
                    <Route path="" element={<Home />} />
                    <Route element={<ErrorPage />}/>
                </Routes>
            </div>

        </Router>
    )
}

export default WebsiteRouter;