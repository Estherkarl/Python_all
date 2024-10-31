CREATE TABLE site_user (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    uuid UUID,
    avatar BYTEA,
    role VARCHAR(20), 
    birthdate DATE,
    siblings TEXT[],
    availability TIME[],
    site_settings JSONB,
    created_on TIMESTAMP,
    active_for INTERVAL
);
