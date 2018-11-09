
wonNationalChampionship = input("Have you won a national championship? (y/n) ").lower().startswith("y");

#I really want to make those print statements part of the loop so they print five times
#
#So, put your cursor at the start of the first print() statement
#Hit Ctrl-V to go into VISUAL-BLOCK mode
#Use the j key to scroll down and highlight the other print() statements
#Hit Shift-<ENTER>. This puts your cursor at the beginning of the line in (sort-of) INSERT mode
#Hit the Tab key twice to get the first statement inside the loop body
#Hit Esc to leave VISUAL-BLOCK mode. All the other statements should have indented as well.


if wonNationalChampionship:
    for i in range(5):
        pass #That's just a placeholder
print("You are a winner!")
print("You know, not everyone deserves a trophy. That's we use if statements to check.")
print("We strongly believe in proper indentation here at Alabama.")
print()
