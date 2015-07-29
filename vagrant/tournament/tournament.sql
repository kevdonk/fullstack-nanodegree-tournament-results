-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- DROP DATABASE if it exists, and create new database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- connect to database

\c tournament;

-- players: name, id, and current tournament
CREATE TABLE players (id SERIAL PRIMARY KEY,
                      name TEXT
                      );

-- matches: stores the tournament, round, participants and outcome
CREATE TABLE matches (id SERIAL PRIMARY KEY,
                      winner INT REFERENCES players(id),
                      loser INT REFERENCES players(id)
                      );

-- standings: player rankings, including names and # of matches
CREATE VIEW standings AS
	SELECT players.id,
		players.name,
		(SELECT COUNT(*) FROM matches WHERE players.id = matches.winner) AS wins,
		(SELECT COUNT(*) FROM matches WHERE players.id = matches.winner OR players.id = matches.loser) AS matches
	FROM players
	ORDER BY wins DESC;


