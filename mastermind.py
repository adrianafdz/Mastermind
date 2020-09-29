#!D:\Program Files\python.exe

# Adriana Fernandez
# Sept 28 2020

import cgi
import random

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

# fichas
red = 0 # correct digit and position
white = 0 # correct digit, wrong position

def compareAns(guess, answer, red, white):
	i=0

	# first check all the digits that in the correct position
	while i!=len(answer):
		if guess[i]==answer[i]:
			red=red+1
			# remove it to avoid counting it again later
			answer=answer[:i]+answer[i+1:]
			guess=guess[:i]+guess[i+1:]
			# print("Modified:",answer)
			i=i-1
		i=i+1

	# check white ones
	for x in guess:
		if x in answer:
			white = white +1
			ind=answer.index(x)
			# remove digit from ans to avoid repetition
			answer=answer[:ind]+answer[ind+1:]

	return (red, white)


# done through the form
# check if answer is set or generate it
if "answer" in form:
	answer=form.getvalue("answer")
else:
	# number as string for easier comparison
	number = ""
	for i in range(4):
		number=number+str(random.randint(0,9))
	answer=number

# Check number of attempts made
if "attempts" in form:
	attempts=int(form.getvalue("attempts"))+1
else:
	attempts=0
	msg = "I chose a 4 digit number. Try to guess it!"


# check if form has been sent/a guess has been made
if "guess" in form:
	guess = form.getvalue("guess")
	red, white = compareAns(guess, answer, red, white)
	#print("Red:", red)
	#print("White:", white)
else:
	guess=""

if red==4:
	msg = "Correct! You got it in " + str(attempts) + " attempts."
elif attempts>0:
	msg = msg + "<p>You have " + str(red) + " correct digits and " + str(white) + " at the wrong position."

# Form
print('<h1>Mastermind</h1>')
print('<h2>'+msg+'</h2>')
print('<p> Adaptation of <a href="https://www.youtube.com/watch?v=dMHxyulGrEk" target="_blank">this game</a></p>')
print('<form method="POST">')
print('<input type="text" name="guess" minlength="4" maxlength="4" value="' + guess + '">')
print('<input type="submit" value="Check">')
print('<input type="hidden" name="attempts" value="' + str(attempts) + '">')
print('<input type="hidden" name="answer" value="' + answer + '">')
print('</form>')

if red==4:
	print('<a href="">Play again</a>')