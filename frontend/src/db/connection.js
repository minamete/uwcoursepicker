const mongoose = require('mongoose')
// require('dotenv').config() 

const conn = await mongoose.connect(process.env.REACT_APP_MONGO_URL);

conn.on('error', console.error.bind(console, 'MongoDB connection error:'));