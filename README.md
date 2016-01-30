Overview

This project is composed of 3 parts
1) tournament.sql: Defines and creates the schema used in the tournamnet program.
2) tournament.py: Defines the functions used in the tester script.
3) tournamnet_test.py: The tester script used to make sure the project was done correctly.

How to use these files
1. Setting up schema
After pulling the files into your target repo from github, type 

```
psql -f tournament.sql
```
into your command line.
NOTE: This will overwrite any previous database named "tournament" that you may have created

2. Run the tests

To test whether all of the code is working correctly, type
```
python tournament_test.py
```
into your command line. If everything works correctly, you should see the following results
on come up on your screen

```
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
[(70, 'Bruno Walton', 0L, 0L), (71, "Boots O'Neal", 0L, 0L), (72, 'Cathy Burton', 0L, 0L), (73, 'Diane Grant', 0L, 0L)]
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```

3. Enjoy!
