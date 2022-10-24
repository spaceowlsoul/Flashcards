# :memo: Flashcards

When learning a new language, it can be hard to remember all the new vocabulary, which is exactly where flashcards come in handy!

Typically, flashcards show a task or a picture on one side and the right answer on the other. 

Flashcards can be used to remember any sort of data, and this program can be a useful tool to improve your learning progress! :wink:

## How exactly does it work?

1.Download the 'flashcards' folder and copy the path to the flashcards.py.

2.Run the command prompt, paste the copied path and start executing the python file as follows:

    python flashcards.py                                              
                                                            
At this step you can make use of the import and export features.

To import file add _'i={filename}'_ to the aforementioned line, to export resulting data write _'e={filename}'_ respectively.

For example:

    python flashcards.py -i="capitals.txt"

To read the data correctly, here and later, please, __stick to this format__ of lines in your file:

    term:definition

or

    term:definition: X mistakes

where X represents the counter of the errors made while answering the words before.

This number will be taken into account in the general statistics. Providing no numbers, the counter will be interpreted as 0.

When exporting, the strings will be saved in exactly the same format (with mistakes counter for every word) after the session ending.

3.Having made the previous steps, you'll be shown the main menu, which provides you with the following options:
   
   - add --> add a new card to your dictionary. Specify the new term along with its definition;
   - import --> write the filename with words you intend to use for training during the session;
   - export --> provide the filename where you would like to save the updated dictionary;
   - ask --> opt for how many times you would like to be asked, and the program will ask you the terms, picked on the random base exactly as many times
   - hardest cards --> choose this option, and the program will display the terms in the answer to which you made the most mistakes;
   - reset stats --> clear the statictics of mistakes made;
   - log --> come up with a filename and extension, and all the history of the session will be saved in this file;
   - exit --> terminate the program execution.
   
That's it! Good luck with your studies! :blush:
