// frontend/src/components/Listing/WasteListingForm.js
import React, { useState } from 'react';
import axios from 'axios';

export default function WasteListingForm() {
    const [formData, setFormData] = useState({
        material_type: '',
        quantity: 0,
        location: ''
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:5000/listings', formData, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            alert('Listing created!');
        } catch (error) {
            console.error('Error creating listing:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Material Type" required 
                onChange={e => setFormData({...formData, material_type: e.target.value})} />
            <input type="number" placeholder="Quantity" required 
                onChange={e => setFormData({...formData, quantity: e.target.value})} />
            <input type="text" placeholder="Location" required 
                onChange={e => setFormData({...formData, location: e.target.value})} />
            <button type="submit">Create Listing</button>
        </form>
    );
}
