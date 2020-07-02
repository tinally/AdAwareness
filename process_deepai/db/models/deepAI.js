/* application.js application model */


const mongoose = require('mongoose');

const DetectionSchema = new mongoose.Schema({
    detection_type: String,
    count: Number
});

// Reservations will be embedded in the Restaurant model
const DeepAISchema = new mongoose.Schema({
    video_id: String,
    video_title: String,
    detection_list: [DetectionSchema]
});

const DeepAI = mongoose.model('DeepAi', DeepAISchema);