
for i in range(10):
	if i % 2 == 0:
                print("Aren't people who use tabs instead of spaces utterly loathsome.?")

        if i % 2 == 1:
		print("I'd hate to be the sucker who has to fix this file's whitespace.")

#In some spots I've used 4 spaces, and in other spots I've used a tab

#If we want to change from tabs to spaces. . .
#Type :%s/\t/        /gc

#If we want to change from spaces to tabs. . .
#Type :%s/ \{8}/\t/gc
