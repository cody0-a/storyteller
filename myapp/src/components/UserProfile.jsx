import React from 'react';
import { FaUserCircle, FaEnvelope, FaMapMarkerAlt, FaPhoneAlt, FaGithub, FaLinkedin } from 'react-icons/fa';

const UserProfile = ({ user }) => {
  return (
    <div className="bg-white shadow-lg rounded-lg p-6 flex flex-col items-center">
      <div className="w-32 h-32 rounded-full overflow-hidden">
        {user.avatar ? (
          <img src={user.avatar} alt={user.name} className="w-full h-full text-gray-600" />
        ) : (
          <FaUserCircle size={128} className="text-gray-400 object-fit" />
        )}
      </div>
      <h2 className="text-2xl font-bold mt-4">{user.name}</h2>
      <p className="text-gray-600 mt-2">{user.role}</p>
      <div className="flex items-center text-gray-600 mt-4">
        <FaEnvelope className="mr-2" />
        <span>{user.email}</span>
      </div>
      <div className="flex items-center text-gray-600 mt-2">
        <FaMapMarkerAlt className="mr-2" />
        <span>{user.location}</span>
      </div>
      <div className="flex items-center text-gray-600 mt-2">
        <FaPhoneAlt className="mr-2" />
        <span>{user.phone}</span>
      </div>
      <div className="flex items-center text-gray-600 mt-4">
        <a href={user.githubUrl} target="_blank" rel="noopener noreferrer" className="mr-4">
          <FaGithub size={24} />
        </a>
        <a href={user.linkedinUrl} target="_blank" rel="noopener noreferrer" className="mr-4">
          <FaLinkedin size={24} />
        </a>
      </div>
    </div>
  );
};

export default UserProfile;