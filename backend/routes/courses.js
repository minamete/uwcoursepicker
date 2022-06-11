const express = require('express');
const router = express.Router();
const Course = require('../db/coursesc');

/* GET users listing. */
router.get('/:dept', async function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  var coursePromise = await Course.find({dept: req.params.dept});
  res.send(coursePromise);
});

module.exports = router;
