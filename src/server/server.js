const express = require('express');
const { Pool } = require('pg');

// const resolvers = require('./resolvers');
const app = express();

const pool = new Pool({
    user: process.env.PG_USER,
    host: process.env.PG_HOST,
    database: process.env.PG_DB,
    password: process.env.PG_PW,
    port: process.env.PG_PORT,
});

// Companies

// Create
app.post('/companies', (req, res) => {
    const { name } = req.body;
    const query = {
        text: `INSERT INTO company (name) VALUES ($1) RETURNING *`,
        values: [name],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error creating company' });
        } else {
            res.send({ message: 'Company created successfully' });
        }
    });
});

// Read
app.get('/companies', (req, res) => {
    const query = {
        text: 'SELECT * FROM company',
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error fetching companies' });
        } else {
            res.send(result.rows);
        }
    });
});

// Update
app.put('/companies/:company_id', (req, res) => {
    const company_id = req.params.company_id;
    const { name } = req.body;
    const query = {
        text: `UPDATE company SET name = $1 WHERE company_id = $2 RETURNING *`,
        values: [name, company_id],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error updating company' });
        } else {
            res.send({ message: 'Company updated successfully' });
        }
    });
});

// Delete
app.delete('/companies/:company_id', (req, res) => {
    const company_id = req.params.company_id;
    const query = {
        text: 'DELETE FROM company WHERE company_id = $1',
        values: [company_id],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error deleting company' });
        } else {
            res.send({ message: 'Company deleted successfully' });
        }
    });
});


// Roles

// Create
app.post('/roles', (req, res) => {
    const { company_id, description } = req.body;
    const query = {
        text: `INSERT INTO role (company_id, description) VALUES ($1, $2) RETURNING *`,
        values: [company_id, description],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error creating role' });
        } else {
            res.send({ message: 'Role created successfully' });
        }
    });
});

// Read
app.get('/roles', (req, res) => {
    const query = {
        text: 'SELECT * FROM role',
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error fetching roles' });
        } else {
            res.send(result.rows);
        }
    });
});

// Update
app.put('/roles/:role_id', (req, res) => {
    const role_id = req.params.role_id;
    const { company_id, description } = req.body;
    const query = {
        text: `UPDATE role SET company_id = $1, description = $2 WHERE role_id = $3 RETURNING *`,
        values: [company_id, description, role_id],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error updating role' });
        } else {
            res.send({ message: 'Role updated successfully' });
        }
    });
});

// Delete
app.delete('/roles/:role_id', (req, res) => {
    const role_id = req.params.role_id;
    const query = {
        text: 'DELETE FROM role WHERE role_id = $1',
        values: [role_id],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error deleting role' });
        } else {
            res.send({ message: 'Role deleted successfully' });
        }
    });
});


// Cover Letters

// Create
app.post('/coverletters', (req, res) => {
    const { body, name } = req.body;
    const query = {
        text: `INSERT INTO coverletter (body, name) VALUES ($1, $2) RETURNING *`,
        values: [body, name],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error creating cover letter' });
        } else {
            res.send({ message: 'Cover letter created successfully' });
        }
    });
});

// Read
app.get('/coverletters', (req, res) => {
    const query = {
        text: 'SELECT * FROM coverletter',
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error fetching cover letters' });
        } else {
            res.send(result.rows);
        }
    });
});

// Update
app.put('/coverletters/:coverletter_id', (req, res) => {
    const coverletter_id = req.params.coverletter_id;
    const { body, name } = req.body;
    const query = {
        text: `UPDATE coverletter SET body = $1, name = $2 WHERE coverletter_id = $3 RETURNING *`,
        values: [body, name, coverletter_id],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error updating cover letter' });
        } else {
            res.send({ message: 'Cover letter updated successfully' });
        }
    });
});

// Delete
app.delete('/coverletters/:coverletter_id', (req, res) => {
    const coverletter_id = req.params.coverletter_id;
    const query = {
        text: 'DELETE FROM coverletter WHERE coverletter_id = $1',
        values: [coverletter_id],
    };
    pool.query(query, (err, result) => {
        if (err) {
            console.error(err);
            res.status(500).send({ message: 'Error deleting cover letter' });
        } else {
            res.send({ message: 'Cover letter deleted successfully' });
        }
    });
});


app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
