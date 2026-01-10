import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000/api' });

export const getEquipment = (category, search) => API.get('/equipment', { params: { category, search } });
export const getEquipmentById = (id) => API.get(`/equipment/${id}`);
export const createEquipment = (data) => API.post('/equipment', data);
export const updateEquipment = (id, data) => API.put(`/equipment/${id}`, data);
export const deleteEquipment = (id) => API.delete(`/equipment/${id}`);
