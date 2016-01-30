-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

DROP TABLE IF EXISTS Players CASCADE;
DROP TABLE IF EXISTS Matches CASCADE;

CREATE TABLE Players (Player_ID serial PRIMARY KEY,Player_Name text);
CREATE TABLE Matches (Match_ID serial PRIMARY KEY,winner integer references Players,loser integer references Players);
\c postgres

-- -- Insert some data into players table
-- -- INSERT INTO players (Player_Name) VALUES ('Maria');
-- -- INSERT INTO players (Player_Name) VALUES ('Serena');
-- -- INSERT INTO players (Player_Name) VALUES ('Hingis');



-- -- Insert data into matches table
-- -- INSERT INTO matches (winner, loser) VALUES (1, 2);
-- -- INSERT INTO matches (winner, loser) VALUES (3, 2);
-- -- INSERT INTO matches (winner, loser) VALUES (1, 3);