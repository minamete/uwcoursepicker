import HomePage from '../views/home';
import InputPage from '../views/in';
import SettingsPage from '../views/settings';
import ErrorPage from '../views/error';
import LookupPage from '../views/error';
import DevPortal from '../views/devportal';

import { BrowserRouter, Routes, Route } from 'react-router-dom';
const WebsiteRouter = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/devportal" element={<DevPortal />} />
                <Route path="/lookup" element={<LookupPage />} />
                <Route path="/settings" element={<SettingsPage />} />
                <Route path="/in" element={<InputPage />} />
                <Route path="/" element={<HomePage />} />
                <Route path="" element={<HomePage />} />
                <Route element={<ErrorPage />} />
            </Routes>
        </BrowserRouter>
    )
}

export default WebsiteRouter;