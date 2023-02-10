import random
import requests

print('Welcome to Top Trumps, Pokemon Edition'.upper())

#This function is fetching a random pokemon from the API
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'experience': pokemon['base_experience']  # added extra stats
    }

#This function is used to fetch the data for a specific pokemon that has been chosen by the player --line 62
def get_stats(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'experience': pokemon['base_experience']  # added extra stats
    }



def run():
    #setting the score for player and opponent
    player_score = 0
    opponents_score = 0

    #Allowing the player to play multiple rounds if they want to and giving them three random pokemon cards to choose for each round played.
    no_of_rounds = int(input('How many rounds do you want to play?'))
    for rounds_to_play in range(no_of_rounds):
        my_pokemon_1 = random_pokemon()
        my_pokemon_2 = random_pokemon()
        my_pokemon_3 = random_pokemon()

        print('These are your card options:')
        print('Pokemon 1: {}'.format(my_pokemon_1['name'].title()))
        print('Pokemon 2: {}'.format(my_pokemon_2['name'].title()))
        print('Pokemon 3: {}'.format(my_pokemon_3['name'].title()))

        players_choice = input('Which Pokemon would you like to choose? (Pick: 1, 2, or 3) ')
        if players_choice == '1':
            print('You have chosen {}'.format(my_pokemon_1['name'].title()))
            players_choice = my_pokemon_1
        elif players_choice == '2':
            print('You have chosen {}'.format(my_pokemon_2['name'].title()))
            players_choice = my_pokemon_2
        elif players_choice == '3':
            print('You have chosen {}'.format(my_pokemon_3['name'].title()))
            players_choice = my_pokemon_3

        #Asking the player which stat they want to play with from their chosen card
        player_pokemon_stats = get_stats(players_choice['name'])

        print('Here are the stats for {}'.format(players_choice['name'].title()))
        # print('1. Name: {} '.format(player_pokemon_stats['name'].title()))
        print('2. Id: {} '.format(player_pokemon_stats['id']))
        print('3. Height: {} '.format(player_pokemon_stats['height']))
        print('4. Weight: {} '.format(player_pokemon_stats['weight']))
        print('5. Experience: {} '.format(player_pokemon_stats['experience']))

        stat_choice = input('Which stat do you want to use? (id, height, weight or experience ) ')

        #Allowing the opponent (computer) to choose which stat they want to play with from the chosen card
        opponent_pokemon = random_pokemon()

        opponent_choice = [opponent_pokemon['id'], opponent_pokemon['height'], opponent_pokemon['weight'],
                           opponent_pokemon['experience']]

        #The max function will choose the highest value from the opponent's choice of stats
        if opponent_pokemon['id'] == max(opponent_choice):
            opponent_stat_choice = 'id'
        elif opponent_pokemon['height'] == max(opponent_choice):
            opponent_stat_choice = 'height'
        elif opponent_pokemon['weight'] == max(opponent_choice):
            opponent_stat_choice = 'weight'
        elif opponent_pokemon['experience'] == max(opponent_choice):
            opponent_stat_choice = 'experience'

        my_stat = player_pokemon_stats[stat_choice]
        opponent_stat = opponent_pokemon[opponent_stat_choice]
        print('The opponent chose Pokemon: {} and the following stat, {}: {}'.format(opponent_pokemon['name'], opponent_stat_choice,opponent_stat))
        # print('The opponent stat is {}'.format(opponent_stat))
        # print('Your stat is {}'.format(my_stat))

        #This function will decide who won the round and show the current score for each player
        if my_stat > opponent_stat:
            player_score += 1
            print('You Win!')
            print('--------SCORE BOARD--------')
            print('YOUR SCORE--------{}'.format(player_score))
            print('OPPONENT\'S SCORE--{}'.format(opponents_score))
        elif my_stat < opponent_stat:
            opponents_score += 1
            print('You Lose!')
            print('--------SCORE BOARD--------')
            print('YOUR SCORE--------{}'.format(player_score))
            print('OPPONENT\'S SCORE--{}'.format(opponents_score))
        else:
            print('Draw!')
            print('--------SCORE BOARD--------')
            print('YOUR SCORE--{}'.format(player_score))
            print('OPPONENT\'S SCORE--{}'.format(opponents_score))


run()
