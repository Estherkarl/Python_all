-- Task 1: 
SELECT name 
FROM site_user 
WHERE array_length(siblings, 1) > 1;

-- Task 2: 
UPDATE site_user 
SET siblings = array_append(siblings, 'Jordi') 
WHERE name = 'Louise Clark';

-- Task 3: 
UPDATE site_user 
SET availability = '{{09:00:00,10:00:00}}' 
WHERE name = 'Louise Clark';

-- Task 4: 
UPDATE site_user 
SET site_settings = jsonb_set(site_settings, '{notifications}', 'false'::jsonb) 
WHERE name = 'Louise Clark';

-- Task 5: 
SELECT name 
FROM site_user 
WHERE role < 'Moderator';

UPDATE site_user 
SET role = 'Moderator' 
WHERE name = 'Johann Müller';

-- Task 6: 
SELECT name 
FROM site_user 
WHERE (site_settings->>'notifications')::boolean = false;

-- Task 7: 
SELECT name 
FROM site_user 
WHERE NOT (site_settings->>'background') IS NOT NULL;
