#!/usr/bin/env python
# 
#

import psycopg2

#Function to close out connection. Helpful to remove redundancy of opening a connection
def open_connection(database_name="tournament"):
    try:
        conn=psycopg2.connect("dbname={}".format(database_name))
        c=conn.cursor()
        return c,conn
    except:
        print("Connection could not be established")

#Function to close out connection. Helpful to remove redundancy of closing a connection
def close_connection(conn):
    conn.commit()
    conn.close()

#Register a new player
def registerPlayer(name):
    c,conn=open_connection()
    c.execute("INSERT INTO Players (Player_Name) Values (%s)",(name,))
    close_connection(conn)


#Remove all the match records from the database.
def deleteMatches():
    c,conn=open_connection()
    c.execute("DELETE FROM Matches;")
    close_connection(conn)

#Remove all the player records from the database.
def deletePlayers():
    c,conn=open_connection()
    c.execute("DELETE FROM Players;")
    close_connection(conn)

#Returns the number of players currently registered.
def countPlayers():
    c,conn=open_connection()
    c.execute("""SELECT count(Player_ID)
                 FROM Players
                 """)
    result = c.fetchone()[0]
    close_connection(conn)
    return result
  

#Returns from the vPlayer_Status View a list of the players and their win records, 
# sorted by wins in descending order (Player_id, name, wins, matches).
def playerStandings():
    c,conn=open_connection()
    c.execute("""SELECT Player_ID,Player_Name,wins,Matches 
                 FROM vPlayer_Status
                 ORDER by wins desc;""")
    result = c.fetchall()
    close_connection(conn)
    return result

#Records the outcome of a single match between two players.
def reportMatch(winner, loser):
    c,conn=open_connection()
    #This might need to be redone to match tuple notation.
    c.execute("INSERT INTO Matches (winner,loser) Values (%s,%s)",(winner,loser))    
    close_connection(conn)

 #   Returns a list of pairs of players for the next round of a match.  
 #   Each player is paired with another player with an equal 
 #   or nearly-equal win record, that is, a player adjacent
 #   to him or her in the standings.

def swissPairings():
    c,conn=open_connection()
    c.execute("""SELECT COUNT(Player_ID) FROM Players""")
    c.execute("""SELECT a.Player_ID,a.Player_Name,b.Player_ID,b.Player_Name
                 FROM vPlayer_Status a,vPlayer_Status b
                 where a.wins=b.wins and a.Player_ID<b.Player_ID; """)
    result = c.fetchall()
    close_connection(conn)
    return result

#Scrap code for the next version. 
# Eventually my function for swiss pairings should be able to
# work with an odd number of players.
'''
def swissPairings():
    c,conn=open_connection()
    c.execute("""SELECT COUNT(Player_ID) FROM Players""")
    if c.fetchone()[0] %2==0: 
        c.execute("""SELECT a.Player_ID,a.Player_Name,b.Player_ID,b.Player_Name
                     FROM vPlayer_Status a,vPlayer_Status b
                     where a.wins=b.wins and a.Player_ID<b.Player_ID; """)
        result = c.fetchall()
        print "Even"
    else:
        c.execute("""SELECT a.Player_ID,a.Player_Name,b.Player_ID,b.Player_Name
                     FROM vPlayer_Status a,vPlayer_Status b
                     where a.wins=b.wins and a.Player_ID<b.Player_ID; """)
        result = c.fetchall()
        print "Odd"
    close_connection(conn)
    return result
'''