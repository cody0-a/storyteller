import React, { useState } from 'react';
function UserRegister() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = {
      name: event.target.name.value,
      email: event.target.email.value,
      password: event.target.password.value,
      phone: event.target.phone.value,
      address: event.target.address.value,
      city: event.target.city.value,
      state: event.target.state.value,
      zipcode: event.target.zipcode.value,
      country: event.target.country.value,
      gender: event.target.gender.value,
      hobbies: event.target.hobbies.value,
      about: event.target.about.value,
      image: event.target.image.files[0],
      role: event.target.role.value
    };

    try {
      const response = await fetch('http://127.0.0.1/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',

          
        },
        body: JSON.stringify(formData)
      });
      if (response.ok) {
        const userData = await response.json();
        setUser(userData);
      } else {
        const errorData = await response.json();
        setError(errorData.errors);
      }
    } catch (err) {
      setError('An error occurred while registering the user.');
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className='formInput rounded-lg shadow-xl ml-2'>
        <input className='py-2 ml-0 rounded-lg focus:*:marker:bg-slate-50' type="text" name="name" placeholder="Name" />
        <input className='py-2 ml-0 rounded-lg' type="email" name="email" placeholder="Email" />
        <input className='py-2 ml-0 rounded-lg' type="password" name="password" placeholder="Password" />
        <input className='py-2 ml-0 rounded-lg' type="text" name="phone" placeholder="Phone" />
        <input className='py-2 ml-0 rounded-lg' type="text" name="address" placeholder="Address" />
        <input className='py-2 ml-0 rounded-lg' type="text" name="city" placeholder="City" />
        <input className='py-2 ml-0 rounded-lg' type="text" name="state" placeholder="State" />
        <input className='py-2 ml-0 rounded-lg' type="text" name="zipcode" placeholder="Zipcode" />
        <input className='py-2 ml-0 rounded-lg' type="text" name="country" placeholder="Country" />
        <input className='py-2 ml-0 rounded-lg' type="text" name="gender" placeholder="Gender" />
        <input className='py-2 ml-0 rounded-lg' type="text" name="hobbies" placeholder="Hobbies" />
        <input className ='border-1 shadow-sm rounded-lg' type="file"  name="image" />
        <input className ="text py-3 my-2 rounded-lg" type="text" name="role" placeholder="Role" />
        <button type="submit" className='submitButton'>Register</button>
      </form>
      {user && (
        <div>
          <h1>{user.name}</h1>
          <p>Email: {user.email}</p>
          <p>Phone: {user.phone}</p>
          <p>Address: {user.address}, {user.city}, {user.state}, {user.zipcode}, {user.country}</p>
          <p>Gender: {user.gender}</p>
          <p>Hobbies: {user.hobbies}</p>
          <p>About: {user.about}</p>
          <img src={user.image} alt="User" />
          <p>Role: {user.role}</p>
          <p>Created at: {user.created_at}</p>
          <p>Updated at: {user.updated_at}</p>
        </div>
      )}
      {error && <div>Error: {error}</div>}
    </div>
  );
}

export default UserRegister;