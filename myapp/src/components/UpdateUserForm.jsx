import React, { useState } from 'react';

function UpdateUserForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [bio, setBio] = useState('');
  const [profilePicture, setProfilePicture] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const userData = { name, email, bio, profile_picture: profilePicture };
    const response = await fetch(`/api/users/123`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });
    const updatedData = await response.json();
    // Update the user interface with the new data
    console.log(updatedData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type="text"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
      </label>
      <label>
        Email:
        <input
          type="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
        />
      </label>
      <label>
        Bio:
        <textarea
          value={bio}
          onChange={(event) => setBio(event.target.value)}
        ></textarea>
      </label>
      <label>
        Profile Picture:
        <input
          type="text"
          value={profilePicture}
          onChange={(event) => setProfilePicture(event.target.value)}
        />
      </label>
      <button type="submit">Update User</button>
    </form>
  );
}

export default UpdateUserForm;