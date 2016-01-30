#!/usr/bin/env python
# 
#

import psycopg2

#Function to close out connection. Helpful to remove redundancy of opening a connection
def open_connection():
    conn=psycopg2.connect("dbname=tournament")
    c=conn.cursor()
    return c,conn

#Function to close out connection. Helpful to remove redundancy of closing a connection
def close_connection(conn):
    conn.commit()
    conn.close()


def registerPlayer(player):
    c,conn=open_connection()
    c.execute("INSERT INTO Players (Player_Name) Values (%s)",(player,))
    close_connection(conn)


"""Remove all the match records from the database."""
def deleteMatches():
    c,conn=open_connection()
    c.execute("DELETE FROM Matches;")
    close_connection(conn)

"""Remove all the player records from the database."""
def deletePlayers():
    c,conn=open_connection()
    c.execute("DELETE FROM Players;")
    close_connection(conn)

"""Returns the number of players currently registered."""
def countPlayers():
    c,conn=open_connection()
    c.execute("SELECT count(Player_ID) FROM Players;")
    result = c.fetchone()[0]
    close_connection(conn)
    return result
  
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

def playerStandings():
    c,conn=open_connection()
    c.execute("DROP VIEW IF EXISTS vPlayer_Status;")
    c.execute("""CREATE VIEW vPlayer_Status as SELECT base.Player_ID,base.Player_Name,Wins.n as wins,losses.n+Wins.n as Matches
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
                 on base.Player_ID=losses.Player_ID
                order by wins desc;
        """)
    c.execute("SELECT * FROM step")
    result = c.fetchall()
    close_connection(conn)
    return result

    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
def reportMatch(winner, loser):
    c,conn=open_connection()
    #This might need to be redone to match tuple notation.
    c.execute("INSERT INTO Matches (winner,loser) Values (%s,%s)",(winner,loser))    
    close_connection(conn)

    """Returns a list of pairs of players for the next round of a match. 
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
def swissPairings():
    c,conn=open_connection()
    c.execute("""SELECT a.Player_ID,a.Player_Name,b.Player_ID,b.Player_Name
                 FROM vPlayer_Status a,vPlayer_Status b
                 where a.wins=b.wins and a.Player_ID<b.Player_ID; """)
    result = c.fetchall()
    close_connection(conn)
    return result
