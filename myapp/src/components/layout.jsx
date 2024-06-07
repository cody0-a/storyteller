import React from 'react';
import { FaHome, FaUserCircle, FaBookOpen, FaCog } from 'react-icons/fa';

const Layout = () => {
  return (
    <div className="flex">
      <Sidebar />
      <MainContent />
    </div>
  );
};

const Sidebar = () => {
  return (
    <div className="bg-white shadow-lg rounded-lg w-72 p-6 mr-6 h-screen overflow-hidden">
      <nav>
        <ul className="space-y-4">
          <li>
            <a href="#" className="flex items-center text-gray-600 hover:text-gray-800 transition-colors">
              <FaHome className="mr-2" />
              <span>Home</span>
            </a>
          </li>
          <li>
            <a href="#" className="flex items-center text-gray-600 hover:text-gray-800 transition-colors">
              <FaUserCircle className="mr-2" />
              <span>Profile</span>
            </a>
          </li>
          <li>
            <a href="#" className="flex items-center text-gray-600 hover:text-gray-800 transition-colors">
              <FaBookOpen className="mr-2" />
              <span>Documents</span>
            </a>
          </li>
          <li>
            <a href="#" className="flex items-center text-gray-600 hover:text-gray-800 transition-colors">
              <FaCog className="mr-2" />
              <span>Settings</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  );
};

const MainContent = () => {
  return (
    <div className="flex-1 bg-white shadow-lg rounded-lg p-6 overflow-y-auto h-screen">
      <h1 className="text-2xl font-bold mb-4 text-green-900 text-center">Main Content</h1>
      <p className="mb-4 text-gray-800 justify-center align-baseline  text-center border-1 rounded-md shadow-md font-sans font-normal space-x-0">
        This is the main content area. It will scroll independently of the sidebar.
        Lord of The Rings , Harry Potter are really good read ( just trust me , the movies didn’t do they justice ) . 451 Fahrenheit , The adventures of Huckleberry Finn is also really good if you looking for a one book run . Finally , Scaramouche is good from my memory ( I read it in 2016 , when I was 13 ) 
        so if anyone could confirm me about this that would be great
      </p>
      {/* Add more content here */}
      <div style={{ height: '160vh' }}>
        {/* Add more content to make the main content scrollable */}
      </div>
    </div>
  );
};

export default Layout;