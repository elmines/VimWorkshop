
grades = [88, 72, 83, 60, 99]
print("How long is grades? {} elements".format(len(grades)))


print("TODO: Get rid of all these debug statements")

sumGrades = sum(grades[:-1])
print("How large is sumGrades? {}".format(sumGrades))
avgGrade = sumGrades / len(grades)

print("Your average grade is {}".format(avgGrade))

#I'm a bit annoyed by most of those() print statements
#Go to the same line as a print statement
#Hit <SHIFT>-i to go the front of the line in INSERT mode
#Insert the comment symbol (for Python, #)
#Hit <ESC> to leave INSERT mode
#Now, go to the other lines you want to comment, and hit . to comment those out, too
	# Hitting . just repeats your last command

#Maybe I want to put some more comments in my code, because I believe in good documentation
#Go to a line where you want to make a short comment at the end
#Hit <SHIFT>-a to go to the end of the line in INSERT mode (the a stands for "append")
#Type whatever comment you want to put there

#If you ever happen to just want to go to the end of the line but not necessarily type stuff there, just hit $
