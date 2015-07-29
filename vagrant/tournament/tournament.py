#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def commit(sql, data=None):
    """ Execute SQL statement and commits transaction
    Args:
      sql: the sql statement to be executed
      data: variable to be used in sql query (optional)
    """
    DB = connect()
    c = DB.cursor()
    if data == None:
      c.execute(sql)
    else:
      c.execute(sql, (data,))
    DB.commit()
    DB.close()

def query(sql):
    """ Execute SQL query
    # uses fetchall() for reusability - might see performance hits with larger data sets
    Args:
      sql: the sql query to be executed
    """
    DB = connect()
    c = DB.cursor()
    c.execute(sql)
    result=c.fetchall()
    DB.close()
    return result

def deleteMatches():
    """Remove all the match records from the database."""
    sql = "DELETE FROM matches"
    commit(sql)

def deletePlayers():
    """Remove all the player records from the database."""
    sql = "DELETE FROM players"
    commit(sql)


def countPlayers():
    """Returns the number of players currently registered."""
    sql = "SELECT count(*) FROM players"
    result = query(sql)
    return result[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    sql = "INSERT INTO players(name) VALUES (%s)"
    commit(sql, name)


def playerStandings():
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
    sql = "SELECT * FROM standings"
    return query(sql)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    sql = "INSERT INTO matches(winner, loser) VALUES (%s, %s)"
    DB = connect()
    c = DB.cursor()
    c.execute(sql, (winner, loser))
    DB.commit()
    DB.close()

def swissPairings():
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
    sql = "SELECT id, name FROM standings"
    standings = query(sql)
    pairings = []
    for x in range(0, countPlayers()-1,2):
        pairings.append(standings[x] + standings[x+1])

    return pairings


