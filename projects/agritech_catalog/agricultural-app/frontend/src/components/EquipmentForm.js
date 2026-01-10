import React, { useState, useEffect } from 'react';

const EquipmentForm = ({ initialData, onSubmit, onCancel }) => {
  const [form, setForm] = useState({
    name: '',
    manufacturer: '',
    model: '',
    price: '',
    power: '',
    description: ''
  });

  useEffect(() => {
    if (initialData) {
      setForm({
        name: initialData.name || '',
        manufacturer: initialData.manufacturer || '',
        model: initialData.model || '',
        price: initialData.price || '',
        power: initialData.power || '',
        description: initialData.description || ''
      });
    }
  }, [initialData]);

  const handleChange = e => {
    const { name, value } = e.target;
    setForm(f => ({ ...f, [name]: value }));
  };

  const handleSubmit = e => {
    e.preventDefault();
    if (!form.name || !form.manufacturer || !form.model || !form.price || !form.power) {
      alert('Пожалуйста, заполните все обязательные поля.');
      return;
    }
    onSubmit({
      name: form.name,
      manufacturer: form.manufacturer,
      model: form.model,
      price: Number(form.price),
      power: Number(form.power),
      description: form.description
    });
    setForm({
      name: '',
      manufacturer: '',
      model: '',
      price: '',
      power: '',
      description: ''
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="name" placeholder="Название" value={form.name} onChange={handleChange} required />
      <input type="text" name="manufacturer" placeholder="Производитель" value={form.manufacturer} onChange={handleChange} required />
      <input type="text" name="model" placeholder="Модель" value={form.model} onChange={handleChange} required />
      <input type="number" name="price" placeholder="Цена" value={form.price} onChange={handleChange} required />
      <input type="number" name="power" placeholder="Мощность" value={form.power} onChange={handleChange} required />
      <textarea name="description" placeholder="Описание" value={form.description} onChange={handleChange} />
      <div>
        <button type="submit">{initialData ? 'Обновить' : 'Добавить'}</button>
        {initialData && <button type="button" onClick={onCancel} style={{ marginLeft: 10 }}>Отмена</button>}
      </div>
    </form>
  );
};

export default EquipmentForm;
