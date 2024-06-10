import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Navigation from './components/Navigation';
import PrivateRoute from './components/PrivateRoute';
import UserProfile from './components/UserProfile';
import UserRegister from './components/UserRegister';
import Navbar from './components/Navbar';
import Layout from './components/layout';

const App: React.FC = () => {
    return (
      <div className='min-h-screen bg-black text-white '>
        <nav>
          <ul>
            <Navbar />
            <Layout />
          </ul>
        </nav>
      <Router>
            <div>
                <Navigation />
                <Routes>

                    <Route path="/register" element={<UserRegister />} />
                    <Route path="/login" element={<Login />} />
                    <Route
                        path="/profile"
                        element={
                            <PrivateRoute>
                                <UserProfile key="profile" user={undefined} />
                            </PrivateRoute>
                        }
                    />
                </Routes>
            </div>
        </Router>
</div>
    );
};

export default App;
