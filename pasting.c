/*
Anything you delete (with the d or x keys) can be pasted.
Press dd to delete the current line.

In Vim , we "yank" something rather than copy it.
Press yy to yank the current line.

You can only paste whatever you just deleted "yanked."

Press p to paste after the cursor.

To yank or delete multiple lines, press v to go into VISUAL mode
Use h,j,k, and l to scroll and highlight more lines
Press d to delete the lines, or y to yank them
*/

#include<stdio.h>
int main(void)
{

	printf("You know, the loop should really come before this print statement.\n");

	for (int i = 0; i < 20; ++i)
	{
		printf("Deleting is the same thing as cutting in Vim!");
		printf("In Vim, we don't copy--we yank.");
	}

}
