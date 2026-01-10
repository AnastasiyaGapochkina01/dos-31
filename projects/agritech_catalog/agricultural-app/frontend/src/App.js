import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CategoryPage from './components/CategoryPage';

const App = () => {
  return (
    <Router>
      <div>
        <nav style={{ marginBottom: 20 }}>
          <Link to="/category/Трактор" style={{ marginRight: 10 }}>Тракторы</Link>
          <Link to="/category/Комбайн" style={{ marginRight: 10 }}>Комбайны</Link>
          <Link to="/category/Сеялка">Сеялки</Link>
        </nav>
        <Routes>
          <Route path="/category/:category" element={<CategoryPage />} />
          <Route path="*" element={<div>Выберите категорию техники</div>} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
