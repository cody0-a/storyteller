import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-gray-900 py-4">
      <div className="container mx-auto flex justify-between items-center">
      <div className="flex items-center">
          <a href="/" className="text-white font-bold text-xl logo-animation">
            <span className="text-red-400 letter-animation">U</span>
            <span className="text-cyan-900 letter-animation">R</span>
            <span className="letter-animation">StorI</span>
          </a>
        </div>
        <ul className="flex space-x-6 text-gray-400">
          <li>
            <a href="#" className="hover:text-white text-bold text-xl">
              story
            </a>
          </li>
          <li>
            <a href="#" className="hover:text-white text-bold text-xl">
              trending
            </a>
          </li>
          <li>
            <a href="#" className="hover:text-white text-bold text-xl">
              shared
            </a>
          </li>
          <li>
            <a href="#" className="hover:text-white text-bold text-xl">
              recent
            </a>
          </li>
          <li>
            <a href="#" className="hover:text-white text-bold text-xl">
              notifications
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;