// src/components/ShareComment.js
import React, { useState } from 'react';
import axios from 'axios';

const ShareComment = ({ commentId }) => {
    const [sharedWith, setSharedWith] = useState('');

    const handleShare = async () => {
        try {
            const response = await axios.post('/api/share-comment/', {
                comment: commentId,
                shared_with: sharedWith
            });
            console.log('Comment shared successfully:', response.data);
        } catch (error) {
            console.error('Error sharing comment:', error);
        }
    };

    return (
        <div className="share-comment">
            <input
                type="text"
                value={sharedWith}
                onChange={(e) => setSharedWith(e.target.value)}
                placeholder="Share with (username)"
                className="input-field"
            />
            <button onClick={handleShare} className="share-button">
                Share Comment
            </button>
        </div>
    );
};

export default ShareComment;
