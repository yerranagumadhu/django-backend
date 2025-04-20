-- Table: public.department
CREATE TABLE IF NOT EXISTS public.department (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

-- Table: public.job_title
CREATE TABLE IF NOT EXISTS public.job_title (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT
);

-- Table: public.project
CREATE TABLE IF NOT EXISTS public.project (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    start_date DATE,
    end_date DATE
);

-- Table: public.employee
CREATE TABLE IF NOT EXISTS public.employee (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    department_id INTEGER REFERENCES department(id),
    job_title_id INTEGER REFERENCES job_title(id),
    salary NUMERIC(10, 2),
    hire_date DATE
);

-- Table: public.employee_project
CREATE TABLE IF NOT EXISTS public.employee_project (
    employee_id INTEGER REFERENCES employee(id),
    project_id INTEGER REFERENCES project(id),
    role VARCHAR(100),
    assigned_date DATE,
    PRIMARY KEY (employee_id, project_id)
);

-- Table: public.attendance
CREATE TABLE IF NOT EXISTS public.attendance (
    employee_id INTEGER REFERENCES employee(id),
    date DATE,
    check_in TIME,
    check_out TIME,
    status VARCHAR(50),
    PRIMARY KEY (employee_id, date)
);

-- Table: public.leave
CREATE TABLE IF NOT EXISTS public.leave (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id),
    leave_type VARCHAR(50),
    start_date DATE,
    end_date DATE,
    reason TEXT,
    status VARCHAR(50)
);

-- Table: public.performance_review
CREATE TABLE IF NOT EXISTS public.performance_review (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id),
    reviewer_id INTEGER REFERENCES employee(id),
    review_date DATE,
    rating NUMERIC(3, 2),
    comments TEXT
);

-- Table: public.salary_history
CREATE TABLE IF NOT EXISTS public.salary_history (
    employee_id INTEGER REFERENCES employee(id),
    amount NUMERIC(10, 2),
    effective_date DATE,
    PRIMARY KEY (employee_id, effective_date)
);

-- Table: public.manager_relation
CREATE TABLE IF NOT EXISTS public.manager_relation (
    employee_id INTEGER REFERENCES employee(id),
    manager_id INTEGER REFERENCES employee(id),
    PRIMARY KEY (employee_id)
);
