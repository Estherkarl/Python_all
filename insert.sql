-- Inserting Miriam Valira
INSERT INTO site_user (name, uuid, role, birthdate, siblings, availability, site_settings, created_on)
VALUES ('Miriam Valira', 'e41e1291-33b8-4316-8a86-28a618d5c338', 'Admin', '1995-08-29', '{"Dani", "Louis"}', '{"12:00:00", "15:00:00"}', '{"background": "red", "notifications": false}', '2015-09-23 08:56:00');

-- Inserting Johann Müller
INSERT INTO site_user (name, uuid, role, birthdate, availability, site_settings, created_on)
VALUES ('Johann Müller', 'd81331bf-a4f6-4ecd-8883-51dee509309e', 'User', '2002-05-09', '{"09:00:00", "14:00:00", "18:00:00", "20:00:00"}', '{"notifications": true}', '2017-05-01 13:03:00');

-- Inserting Louise Clark
INSERT INTO site_user (name, uuid, role, birthdate, siblings, availability, site_settings, created_on)
VALUES ('Louise Clark', 'e6168ec9-7306-44a5-9875-2c659e15740e', 'Moderator', '1992-05-03', '{"Monique"}', '{"09:00:00", "12:00:00", "13:00:00", "17:00:00"}', '{"notifications": true}', '2007-03-21 10:31:00');
