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

CREATE TABLE Players (Player_ID serial PRIMARY KEY,
					  Player_Name text NOT NULL);

CREATE TABLE Matches (Match_ID serial PRIMARY KEY,
					  winner integer references Players(Player_ID) ON DELETE CASCADE,
					  loser integer  CHECK (winner <> loser) references Players(Player_ID) ON DELETE CASCADE);

CREATE VIEW vPlayer_Status as SELECT base.Player_ID,base.Player_Name,Wins.n as wins,losses.n+Wins.n as Matches
                 From Players base
                 LEFT JOIN( 
                       select a.player_id, count(b.winner) AS n 
                       FROM players a
                       LEFT JOIN matches b
                       On a.Player_ID = b.winner
                       group by a.player_id) Wins
                on base.Player_ID=Wins.player_id
                LEFT JOIN(
                        Select a.Player_ID,count(b.loser) as n
                        From Players a
                        left join matches b 
                        on a.Player_ID=b.loser
                        group by a.Player_ID) losses
                 on base.Player_ID=losses.Player_ID;
