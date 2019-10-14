# Introduction to Relational Databases in SQL on DataCamp

#######################################

# Part 1: Your first database

#######################################

## Query information_schema with SELECT

# Get information on all table names in the current database, while limiting your query to the 'public' table_schema.
# Query the right table in information_schema
SELECT table_name
FROM information_schema.tables
# Specify the correct table_schema value
WHERE table_schema = 'public';

# Now have a look at the columns in university_professors by selecting all entries in information_schema.columns that correspond to that table.
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'university_professors' AND table_schema = 'public';

# Finally, print the first five rows of the university_professors table.
SELECT *
FROM university_professors
LIMIT 5;

## CREATE your first few TABLEs

# Create a table professors with two text columns: firstname and lastname.
# Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

#Print the contents of this table
SELECT *
FROM professors

#Create a table universities with three text columns: university_shortname, university, and university_city.
#Create a table for the universities entity type
CREATE TABLE universities (
 university_shortname text,
 university text,
 university_city text
);

#Print the contents of this table
SELECT *
FROM universities

## ADD a COLUMN with ALTER TABLE

# Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;

# Print the contents of this table
SELECT *
FROM professors;

## RENAME and DROP COLUMNs in affiliations

#Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

#Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;

## Migrate data with INSERT INTO SELECT DISTINCT

#Insert unique professors into the new table
INSERT INTO professors
SELECT DISTINCT firstname, lastname, university_shortname
FROM university_professors;

#Doublecheck the contents of professors
SELECT *
FROM professors;

#Insert unique affiliations into the new table
INSERT INTO affiliations
SELECT DISTINCT firstname, lastname, function, organization
FROM university_professors;

#Doublecheck the contents of affiliations
SELECT *
FROM affiliations;

## Delete tables with DROP TABLE

# Delete the university_professors table
DROP TABLE university_professors;

#######################################

# Part 2: Enforce data consistency with attribute constraints

#######################################

## Conforming with data types

# Let's add a record to the table
INSERT INTO transactions (transaction_date, amount, fee)
VALUES ('2018-09-24', 5454, '30');

# Doublecheck the contents
SELECT *
FROM transactions;

## Type CASTs

# Calculate the net amount as amount + fee
SELECT transaction_date, amount + CAST(fee AS integer) AS net_amount
FROM transactions;

## Change types with ALTER COLUMN

# Have a look at the distinct university_shortname values and take note of the length of the strings.
#Select the university_shortname column
SELECT DISTINCT(university_shortname)
FROM professors;

# Now specify a fixed-length character type with the correct length for university_shortname.
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE char(3);

# Change the type of the firstname column to varchar(64).
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(64);

## Convert types USING a function

#Convert the values in firstname to a max. of 16 characters
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(16)
USING SUBSTRING(firstname FROM 1 FOR 16);

## Disallow NULL values with SET NOT NULL

# Add a not-null constraint for the firstname column.
ALTER TABLE professors
ALTER COLUMN firstname SET NOT NULL;

# Add a not-null constraint for the lastname column.
ALTER TABLE professors
ALTER COLUMN lastname SET NOT NULL;

## Make your columns UNIQUE with ADD CONSTRAINT

# Add a unique constraint to the university_shortname column in universities. Give it the name university_shortname_unq.
ALTER TABLE universities
ADD CONSTRAINT university_shortname_unq UNIQUE(university_shortname);

# Add a unique constraint to the organization column in organizations. Give it the name organization_unq.
ALTER TABLE organizations
ADD CONSTRAINT organization_unq UNIQUE(organization);

#######################################

# Part 3: Uniquely identify records with key constraints

#######################################

## Get to know SELECT COUNT DISTINCT

# First, find out the number of rows in universities.
SELECT COUNT(DISTINCT(university_shortname))
FROM universities;

# Then, find out how many unique values there are in the university_city column.
SELECT COUNT(DISTINCT(university_city))
FROM universities;

## Identify keys with SELECT COUNT DISTINCT
SELECT COUNT(DISTINCT(firstname, lastname))
FROM professors;

## ADD key CONSTRAINTs to the tables

# Rename the organization column to id in organizations.
ALTER TABLE organizations
RENAME COLUMN organization TO id;

#Make id a primary key
ALTER TABLE organizations
ADD CONSTRAINT organization_pk PRIMARY KEY (id);

#Rename the university_shortname column to id
ALTER TABLE universities
RENAME COLUMN university_shortname TO id;

#Make id a primary key
ALTER TABLE universities
ADD CONSTRAINT university_pk PRIMARY KEY (id);

## Add a SERIAL surrogate key

# Add the new column to the table
ALTER TABLE professors
ADD COLUMN id serial;

# Make id a primary key
ALTER TABLE professors
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);

# Have a look at the first 10 rows of professors
SELECT *
FROM professors
LIMIT 10;

## CONCATenate columns to a surrogate key

# Count the number of distinct rows with columns make, model
SELECT COUNT(DISTINCT(make, model))
FROM cars;

# Add the id column
ALTER TABLE cars
ADD COLUMN id varchar(128);

# Update id with make + model
UPDATE cars
SET id = CONCAT(make, model);

# Make id a primary key
ALTER TABLE cars
ADD CONSTRAINT id_pk PRIMARY KEY (id);

# Have a look at the table
SELECT * FROM cars;

## Test your knowledge before advancing

# Create the table
CREATE TABLE students (
  last_name varchar(128) NOT NULL,
  ssn integer PRIMARY KEY,
  phone_no char(12)
);

#######################################

# Part 4: Glue together tables with foreign keys

#######################################

## REFERENCE a table with a FOREIGN KEY

# Rename the university_shortname column
ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id;

# Add a foreign key on professors referencing universities
ALTER TABLE professors
ADD CONSTRAINT professors_fkey FOREIGN KEY (university_id) REFERENCES universities(id);

## Explore foreign key constraints

# Try to insert a new professor
INSERT INTO professors (firstname, lastname, university_id)
VALUES ('Albert', 'Einstein', 'UZH');

## JOIN tables linked by a foreign key

# Select all professors working for universities in the city of Zurich
SELECT professors.lastname, universities.id, universities.university_city
FROM professors
JOIN universities
ON professors.university_id = universities.id
WHERE universities.university_city = 'Zurich';

## Add foreign keys to the "affiliations" table

# Add a professor_id column
ALTER TABLE affiliations
ADD COLUMN professor_id integer REFERENCES professors (id);

# Rename the organization column to organization_id
ALTER TABLE affiliations
RENAME organization TO organization_id;

# Add a foreign key on organization_id
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id);

## Populate the "professor_id" column

# Have a look at the 10 first rows of affiliations
SELECT *
FROM affiliations
LIMIT 10;

# Update professor_id to professors.id where firstname, lastname correspond to rows in professors
UPDATE affiliations
SET professor_id = professors.id
FROM professors
WHERE affiliations.firstname = professors.firstname AND affiliations.lastname = professors.lastname;

# Have a look at the 10 first rows of affiliations again
SELECT *
FROM affiliations
LIMIT 10;

## Drop "firstname" and "lastname"

# Drop the firstname column
ALTER TABLE affiliations
DROP COLUMN firstname;

# Drop the lastname column
ALTER TABLE affiliations
DROP COLUMN lastname;

## Change the referential integrity behavior of a key

# Identify the correct constraint name
SELECT constraint_name, table_name, constraint_type
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';

# Drop the right foreign key constraint
ALTER TABLE affiliations
DROP CONSTRAINT affiliations_organization_id_fkey;

# Add a new foreign key constraint from affiliations to organizations which cascades deletion
ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_id_fkey FOREIGN KEY (organization_id) REFERENCES organizations (id) ON DELETE CASCADE;

# Delete an organization
DELETE FROM organizations
WHERE id = 'CUREM';

# Check that no more affiliations with this organization exist
SELECT * FROM organizations
WHERE id = 'CUREM';

## Count affiliations per university

SELECT COUNT(*), professors.university_id
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
GROUP BY professors.university_id
ORDER BY count DESC;

## Join all the tables together

# Join all tables
SELECT *
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id;

# Group the table by organization sector, professor and university city
SELECT COUNT(*), organizations.organization_sector,
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
GROUP BY organizations.organization_sector,
professors.id, universities.university_city;

# Filter the table and sort it
SELECT COUNT(*), organizations.organization_sector,
professors.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
WHERE organizations.organization_sector = 'Media & communication'
GROUP BY organizations.organization_sector,
professors.id, universities.university_city
ORDER BY count  DESC;
