var createError = require('http-errors');
var express = require('express');
require('dotenv').config() 
var mongoose = require('mongoose')
var usersRouter = require('./routes/courses');

mongoose.connect(process.env.REACT_APP_MONGO_URL).then(() => {
  const app = express();
  app.use('/courses', usersRouter);

  // catch 404 and forward to error handler
  app.use(function (req, res, next) {
    next(createError(404));
  });

  // error handler
  app.use(function (err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render('error', {
      message: err.message,
      error: err
    });
  });

  app.listen(8080, () => {
    console.log("Server started on port 8080")
  })
})

