
import React, { useState } from 'react';
import axios from 'axios';

const ShareStory = ({ storyId }) => {
    const [sharedWith, setSharedWith] = useState('');

    const handleShare = async () => {
        try {
            const response = await axios.post('127.0.0.1/api/share-story/', {
                story: storyId,
                shared_with: sharedWith
            });
            console.log('Story shared successfully:', response.data);
            
        } catch (error) {
            console.error('Error sharing story:', error);
        }
    };

    return (
        <div className="share-story">
            <input
                type="text"
                value={sharedWith}
                onChange={(e) => setSharedWith(e.target.value)}
                placeholder="Share with (username)"
                className="input-field"
            />
            <button onClick={handleShare} className="share-button">
                Share Story
            </button>
        </div>
    );
};

export default ShareStory;
