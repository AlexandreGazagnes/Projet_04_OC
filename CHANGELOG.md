# 2024-07-02 - 10h00 - Code Review
* 
* 

# 2024-06-28 - 10h00 - Code Review
* Update App.py
* remove  sandbox code
* all views should use staticmethods
* delete useless comments 
* refcato .utils 
* moove config.py

# 2024-05-31 - 10h00 - Code Review

* always choose "" or 0 for return to upper menu
* Staticmethod and not classmethod (minor)


# 2024-05-24 - 10h00 - Code Review

## Done / Checklist / Work Review
- done : update all the views for player OK

## Updated / Done during the session
- fix in  views the ```return "nom.view.method", data ```
- small fixes 


### ToDo
- test "by hand" / ipython => all MainViews, PlayerViews (if needed PlayerTemplate, MainTemplate...)
- update all tournament TEMPLATES / check if  good 
- Update all tournaments VIEWS 
- DO NOT WORRY IF THE ROUTING SYSTEM is down (lets keep for next week)
- For Tournament => create, add a player, change status, launch, new round, record scores, classement, 
--> for each on these we need AT LEAST 1 view + 1 template


# 2024-05-17 - 10h00 - Code Review

## Done / Checklist / Work Review
- Write all views for player - Not checked from last week
- Vrite all templates for tournament - Not checked 
- write all views for tournament - Not checked 
- Done with week by Raz : change the template player (+ etc etc....)


## Updated / Done during the session
- Explain deeply the MVT structure 
- Revamp the player template
- No MODELS in the templates => only VIEWS
- Make dummy explaination about how to packing your stuff before moving house :) 

## ToDo
-----------------------------------------------
- 1. DO NOT TOUCH to templates / player  
-----------------------------------------------
- 2. READ MVT documentation on the web / youtube 😅
- 3. Read The template player
- 4. Update the views / player
- 5. (objective) Make the whole module Player work (Models, Views and Templates) 


# 2024-05-10 - 10h00 - Code Review

## Deleted
- Useles code in views 
- Comments some code in tempaltes / tournament


## Updated
- add comments code guideline to all views
- Review all the code templates in players ==> OK
- All the code in templates / tournament ==> to be written

## ToDo
- Validate templates / player
- Write all views for player 
- Vrite all templates for tournament
- write all views for tournament


# 2024-04-12 - 10h00 - Code Review

## Updated 
- added main.py 
- added tempaltes and vues placeholders 
- mooved the player template form vues to PlayerTemplate 

## Todo
- Update tournament menue vues and templates to really add playes to the tournament
- moove all the templates to the templates folder (no print OR input in vues)
- add logic code for all the tournament (add players, start tournament, update rounds, get results, get scores, get ranking)

# 2024-04-05 - 10h00 - Code Review

## Updated 
- Add a const.py to fix data fn problem
- clean code
- fix tests
- fix tournament management 

## Todo 
- Understand the code
- work on get_results, get_scores etc etc 

# 2024-03-22 - 10h00 - Code Review

## Updated 
- Add conftest
- Add new 4 players 
- rename fixture
- change curent round number at 0 when status change to in progress

# 2024-03-15 - 17h00 - Code Review


## Problem
- When i try to update the current round, the round is not updated in the tournament (in database )

- Example usage 
    - Supose we have a tournament with 3 rounds, 4 players, curent_id_round = 0
    - Suppose we have defaults score results at -1
    - Supose we have a new_res to push
    - t.update_current_round(new_res) => no update in the tournament DATABASE

    -  the proble is here : ```t.update_current_round(new_res)```   

## Todo
- Fix this 
- Start Front app / views and Controlers 
- Write print  functions to display the  menu / option how to read user input to store values for players in a dict




# 2024-03-15 - 09h00 - Code Review

## Todo
- Tackle update  tournament problem => we want score OK 1/0 not -1 -1 in the rounds.json !!!! Check
- What about computing results by player ???? get score Check
- write proto AND OR code about thi feature

## Updated
- MAJ classe Tournament with search pb
- Added code test for all 3 rounds all matches 
- Added test update tournament 
- clean code 

# 2024-03-08 - Code Review

## Todo
- [x] continue debug class Player to pass tests and run entire Tournament from creation to end

## Updated
- [x] Fix files errors 
- [x] Reset DB
- [x] Debug tets and Models

# 2024-03-01 - Code Review

## Todo

## Updated

# 2024-02-01 - Code Review

## Todo
- 

## Updated
- addded search to tournament
- moove attributes and methods of tournament to be more consistent with the other classes
- fix get current round and update curent round
- fix _add_round() in tournament => .create()
- upadate requirements.txt = > pycln isort black mypy and other staict code checkers

# 2024-01-22 - Code Review

## Updated
- fix / restructure test policy 
- fix/update Tournament class
- test_players PASSES
- test_tournaments PASSES

## Todo 
- specify librairies versions in requirements.txt - done
- update README.md : - done
    - add a section "About"
    - add a section "Install"
- read about tests and understand WHY, WHAT, HOW we want to use the code
- fix class Tournament 
- fix tournament. get_current_round,-(j'ai essayé une version) 
- update_current_round - (j'ai essayé)
- update 
- fix the Round class


# 2024-01-12 - Mentoring
## Validated
- 

## Updated
- Add pytest to utils
- Update test for tournaments 
- Update methods in tournament 
- Test policy 
- get_current_round_number
- next_round
- update_status
- added search, search_by, create, update to all 3 classes
## Todo

### MUST HAVE
- calculer les scores des jouers
- sortir le classement 
- maj la round en cours et passer a la round suivante
- update trounament must work 
- finish change status 
- validate round creattion when strat a tournament 
- add fucntionality to update each round for the tournament + method update_round

### NICE TO HAVE
- class testPlayer
- add verification that the player is not already in the tournament
- add verification that the player is not already in the Player DB Table
- Add verification that the player is not already in the Player DB Table
------------------------------------------------------------------------------------------------
get_current_round_id:
    self.list_id_round
    Round.search id recuperer la round
    return la round
    pouvoir consulter la round en cours 
update_current_round:
    modifier la round
    get la round. round.match list == new match list
    round.update
PYTEST COMMAND 
pytest -vvx --capture=tee-sys --log-cli-level=INFO tests/models

