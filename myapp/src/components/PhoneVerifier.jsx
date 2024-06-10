import React, { useState } from 'react';
import axios from 'axios';

function PhoneVerifier() {
    const [phoneNumber, setPhoneNumber] = useState('');
    const [countryCode, setCountryCode] = useState('');
    const [isValid, setIsValid] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/validate/', {
                phone_number: phoneNumber,
                country_code: countryCode,
            });
            setIsValid(response.data.is_valid);
            setError(null);
        } catch (err) {
            setIsValid(null);
            setError(err.response.data.error);
        }
    };

    return (
        <div>
            <h1>Phone Number Verifier</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="phoneNumber">Phone Number:</label>
                    <input
                        id="phoneNumber"    
                        type="text"
                        value={phoneNumber}
                        onChange={(e) => setPhoneNumber(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="countryCode">Country Code:</label>
                    <input
                        id="countryCode"
                        type="text"
                        value={countryCode}
                        onChange={(e) => setCountryCode(e.target.value)}
                    />
                </div>
                <button type="submit">Verify</button>
            </form>
            {isValid !== null && (
                <div>
                    {isValid ? <p>Phone number is valid!</p> : <p>Phone number is invalid!</p>}
                </div>
            )}
            {error && <p>{error}</p>}
        </div>
    );
}

export default PhoneVerifier;
