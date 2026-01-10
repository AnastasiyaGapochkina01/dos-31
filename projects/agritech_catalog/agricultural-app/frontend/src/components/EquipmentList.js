import React from 'react';

const EquipmentList = ({ equipment, onEdit, onDelete }) => (
  <table border="1" cellPadding="7" cellSpacing="0" width="100%">
    <thead>
      <tr>
        <th>Название</th>
        <th>Производитель</th>
        <th>Модель</th>
        <th>Цена</th>
        <th>Мощность</th>
        <th>Описание</th>
        <th>Действия</th>
      </tr>
    </thead>
    <tbody>
      {equipment.map(item => (
        <tr key={item._id}>
          <td>{item.name}</td>
          <td>{item.manufacturer}</td>
          <td>{item.model}</td>
          <td>{item.price}</td>
          <td>{item.power}</td>
          <td>{item.description}</td>
          <td>
            <button onClick={() => onEdit(item)}>Редактировать</button>{' '}
            <button onClick={() => onDelete(item._id)}>Удалить</button>
          </td>
        </tr>
      ))}
    </tbody>
  </table>
);

export default EquipmentList;
