const mysql = require('mysql');
const password = require('./config');

//Connection to the database
const connection = mysql.createConnection({
    host: 'localhost',
    port: 3306,
    user: 'root',
    password: password,
    database: 'student_db',
});

//Export Connection
module.exports = connection;