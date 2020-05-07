from random import randint

print( "\nWELCOME TO GUESS ME!" )
print( "I'm thinking of a number between 1 to 100." )
print( "If your guess is more than 10 away from my number, I'll tell you you're COLD." )
print( "If your guess is within 10 of my number, I'll tell you you're WARM." )
print( "If your guess is farther from my number than your last guess, I'll say you're getting COLDER." )
print( "If your guess is closer to my number than your last guess, I'll say you're getting WARMER." )
print( "LET'S PLAY!\n" )

randomInt = randint( 1, 100 )
# print( f'Random number is { randomInt }' )

# COUNTER FOR THE NUMBER OF ATTEMPTS
turn = 1

while True:
	# ERROR HANDLING FOR INVALID INPUT
	validGuess = False
	while ( not validGuess ):
		try:
			guess = int( input( 'What is your guess?: ' ) )
			break
		except:
			print( "That didn't count, enter numbers only." )
	# ONLY BREAKS OUT OF WHILE LOOP WHEN GUESS EQUALS RANDOM INT
	if ( guess != randomInt ):
		if ( guess < 1 or guess > 100 ):
			print( "OUT OF BOUNDS" )
		elif ( turn == 1 ):
			if ( guess >= randomInt - 10 and guess <= randomInt + 10 ):
				print( "WARM!" )
			else:
				print( "COLD!" )
		else:
			if ( prevGuess == guess ):
				print( "You guessed the same number, try again." )
			elif ( abs( guess - randomInt ) < abs( prevGuess - randomInt ) ):
				print( "WARMER!" )
			else:
				print( "COLDER!" )
		prevGuess = guess
		turn += 1
	else:
		break

if ( turn == 1 ):
	print( f'CONGRATULATIONS, YOU GUESS IT IN ONLY {turn} GUESS!!\n' )
else:
	print( f'CONGRATULATIONS, YOU GUESS IT IN ONLY {turn} GUESSES!!\n' )