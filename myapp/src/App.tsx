import React from 'react';
import './input.css'
import './index.css'
import Navbar from './components/Navbar';
import Layout from './components/layout';
import PhoneVerifier from './components/PhoneVerifier';
import  Notifications from './components/Notifications';
const user = {
  name: 'John Doe',
  role: 'Software Engineer',
  avatar: 'https://example.com/avatar.jpg',
  email: 'john.doe@example.com',
  location: 'New York, USA',
  phone: '+1 (123) 456-7890',
  githubUrl: 'https://github.com/johndoe',
  linkedinUrl: 'https://www.linkedin.com/in/johndoe'
};

function App() {
  return (
    <div className="w-full bg-gray-700 text-white font-sans my-[.5px] h overflow-hidden overflow-y-autoh-screen">
      <Navbar />
      <div className="h-[calc(100vh)] overflow-auto">
        <Layout />
      </div>  
      <PhoneVerifier />
      <Notifications />
    </div>
  );
}

export default App;
