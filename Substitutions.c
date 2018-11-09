#include <stdio.h>

void printPlayer(char* player, int number) //Isn't printPlayer a great function?
{

	printf("Number %d is %s!!\n", number, player);
}

//I really want to move to full-upper camelcase and say "PrintPlayer"
//So, I can type :%s/printPlayer/PrintPlayer/gc
//The : lets you access some certain commands from an editor that Vim was built on top of
//The % means "do this for every line of the file"
//The s means subsitute
//The text after the first slash is what you want to change
//The text after the second slash is what you want to replace it with
//The g means replace every instance on a given line (not just the first one)

int main(void)
{
	char* players[] = {"Jalen Hurts", "Tua Tagovailoa", "Jerry Jeudy", "Taylor Wilson"};
	int numbers[] = {2, 13, 4, 96};

	for (int i = 0; i < sizeof(players) / sizeof(char*); ++i) printPlayer(players[i], numbers[i]);

	return 0;
}
