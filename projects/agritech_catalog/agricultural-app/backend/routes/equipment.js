const express = require('express');
const router = express.Router();
const Equipment = require('../models/Equipment');

// Create new equipment
router.post('/', async (req, res) => {
  try {
    const equipment = new Equipment(req.body);
    const saved = await equipment.save();
    res.status(201).json(saved);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all equipment or filtered by category and/or search
router.get('/', async (req, res) => {
  try {
    const { category, search } = req.query;
    let filter = {};
    if (category) filter.category = category;
    if (search) {
      const regex = new RegExp(search, 'i');
      filter.$or = [
        { name: regex },
        { manufacturer: regex },
        { model: regex },
        { description: regex }
      ];
    }
    const equipmentList = await Equipment.find(filter).sort({ createdAt: -1 });
    res.json(equipmentList);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get equipment by id
router.get('/:id', async (req, res) => {
  try {
    const equipment = await Equipment.findById(req.params.id);
    if (!equipment) return res.status(404).json({ error: 'Not found' });
    res.json(equipment);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update equipment by id
router.put('/:id', async (req, res) => {
  try {
    const updated = await Equipment.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
    if (!updated) return res.status(404).json({ error: 'Not found' });
    res.json(updated);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Delete equipment by id
router.delete('/:id', async (req, res) => {
  try {
    const deleted = await Equipment.findByIdAndDelete(req.params.id);
    if (!deleted) return res.status(404).json({ error: 'Not found' });
    res.json({ message: 'Deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
