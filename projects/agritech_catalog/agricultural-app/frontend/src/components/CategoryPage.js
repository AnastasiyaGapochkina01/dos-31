import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getEquipment, createEquipment, updateEquipment, deleteEquipment } from '../api';
import EquipmentList from './EquipmentList';
import EquipmentForm from './EquipmentForm';

const CategoryPage = () => {
  const { category } = useParams();
  const [equipment, setEquipment] = useState([]);
  const [search, setSearch] = useState('');
  const [editing, setEditing] = useState(null);

  const loadData = async () => {
    try {
      const { data } = await getEquipment(category, search);
      setEquipment(data);
    } catch (e) {
      alert('Ошибка загрузки оборудования');
    }
  };

  useEffect(() => {
    loadData();
  }, [category, search]);

  const handleCreate = async (newItem) => {
    await createEquipment({ ...newItem, category });
    loadData();
  };

  const handleUpdate = async (id, updatedData) => {
    await updateEquipment(id, updatedData);
    setEditing(null);
    loadData();
  };

  const handleDelete = async (id) => {
    if (window.confirm('Удалить эту запись?')) {
      await deleteEquipment(id);
      loadData();
    }
  };

  return (
    <div>
      <h1>{category}</h1>
      <input
        type="text"
        placeholder="Поиск..."
        value={search}
        onChange={e => setSearch(e.target.value)}
        style={{ marginBottom: 10 }}
      />
      <EquipmentList
        equipment={equipment}
        onEdit={setEditing}
        onDelete={handleDelete}
      />
      <hr />
      <h2>{editing ? 'Редактировать оборудование' : 'Добавить оборудование'}</h2>
      <EquipmentForm
        initialData={editing}
        onCancel={() => setEditing(null)}
        onSubmit={editing ? (data) => handleUpdate(editing._id, data) : handleCreate}
      />
    </div>
  );
};

export default CategoryPage;
