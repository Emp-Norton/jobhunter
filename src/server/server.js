const express = require('express');
const { Pool } = require('pg');

const app = express();

const pool = new Pool({
    user: 'your_username',
    host: 'your_host',
    database: 'your_database',
    password: 'your_password',
    port: 5432,
});

// Create
app.post('/applications', (req, res) => {
    const { coverletter_id, role_id, resume_id, date_submitted } = req.body;
    const query = {
        text: `INSERT INTO application (coverletter_id, role_id, resume_id, date_submitted) VALUES ($1, $2, $3, $4) RETURNING *`,
        values: [coverletter_id, role_id, resume_id, date_submitted],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error creating application' });
        } else {
            res.send({ message: 'Application created successfully' });
        }
    });
});

// Read
app.get('/applications', (req, res) => {
    const query = {
        text: 'SELECT * FROM application',
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error fetching applications' });
        } else {
            res.send(result.rows);
        }
    });
});

// Update
app.put('/applications/:application_id', (req, res) => {
    const application_id = req.params.application_id;
    const { coverletter_id, role_id, resume_id, date_submitted } = req.body;
    const query = {
        text: `UPDATE application SET coverletter_id = $1, role_id = $2, resume_id = $3, date_submitted = $4 WHERE application_id = $5 RETURNING *`,
        values: [coverletter_id, role_id, resume_id, date_submitted, application_id],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error updating application' });
        } else {
            res.send({ message: 'Application updated successfully' });
        }
    });
});

// Delete
app.delete('/applications/:application_id', (req, res) => {
    const application_id = req.params.application_id;
    const query = {
        text: 'DELETE FROM application WHERE application_id = $1',
        values: [application_id],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error deleting application' });
        } else {
            res.send({ message: 'Application deleted successfully' });
        }
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
