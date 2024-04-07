CREATE TABLE company (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE role (
    role_id SERIAL PRIMARY KEY,
    company_id INTEGER NOT NULL,
    description VARCHAR(255) NOT NULL,
    FOREIGN KEY (company_id) REFERENCES company(company_id)
);

CREATE TABLE resume (
    resume_id SERIAL PRIMARY KEY,
    body TEXT NOT NULL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE coverletter (
    coverletter_id SERIAL PRIMARY KEY,
    body TEXT NOT NULL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE application (
    application_id SERIAL PRIMARY KEY,
    coverletter_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    resume_id INTEGER NOT NULL,
    date_submitted DATE NOT NULL,
    FOREIGN KEY (coverletter_id) REFERENCES coverletter(coverletter_id),
    FOREIGN KEY (role_id) REFERENCES role(role_id),
    FOREIGN KEY (resume_id) REFERENCES resume(resume_id)
);
