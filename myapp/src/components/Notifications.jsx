import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Notifications = () => {
    const [notifications, setNotifications] = useState([]);

    useEffect(() => {
        const fetchNotifications = async () => {
            const response = await axios.get('http://localhost:8000/api/notifications/', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            });
            setNotifications(response.data);
        };

        fetchNotifications();
    }, []);

    const markAsRead = async (id) => {
        await axios.patch(`http://localhost:8000/api/notifications/${id}/`, { is_read: true }, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`
            }
        });
        setNotifications(notifications.map(n => n.id === id ? { ...n, is_read: true } : n));
    };

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Notifications</h2>
            <ul>
                {notifications.map(notification => (
                    <li key={notification.id} className={`p-2 mb-2 ${notification.is_read ? 'bg-gray-200' : 'bg-blue-100'} rounded`}>
                        <p>{notification.message}</p>
                        {!notification.is_read && (
                            <button
                                className="mt-2 p-2 bg-green-500 text-white rounded"
                                onClick={() => markAsRead(notification.id)}
                            >
                                Mark as Read
                            </button>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Notifications;
