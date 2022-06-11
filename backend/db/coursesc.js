var mongoose = require('mongoose');
const Schema = mongoose.Schema

const CourseSchema = new Schema({
    name: String,
    desc: String,
    dept: String,
    faculty: String,
    course_num: String,
    credits: Number,
    offerred: {},
    crosslisted: {},
    prereqs: {},
    coreqs: {},
    antireqs: {},
})

const CourseModel = mongoose.model('Course', CourseSchema, 'coursesStr');

module.exports = CourseModel;