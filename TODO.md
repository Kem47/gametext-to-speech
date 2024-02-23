

# Interface
Thoughts:
- The user upon the launch of the game highlights the area where text is to be detected.
- An automatic system that scans the screen and detects text.
    - How much text should be detected though? CRPGs have a lot of text everywhere. Do we detect it all? Logically you might want to detect only big blocks of text.
- Maybe it's a mixture of both. The system tries to identify big text blocks. However there is an option for the user to bring up the tool and select a box within which is text they want read.
- How is TTS activated?
    - Is it automatic? This carries way too much config with it. When does it start reading? What does it read? etc. 
    - Manual mode is better I believe. The system can identify places with text using one of the above methods. Then an on-screen button shows up next to the text. When you press the button TTS is activated. Maybe if you press the button again TTS is paused or stopped.

- Each text box has these buttons:
    - Before playing:
        - Play
        - Add to queue
    - After playing:
        - Stop
        - Pause

- Ability to select an area manually. This is good for CRPGs and their dialogue boxes. 
    - The system will not look for text within this box if text is already found in it.
- Ability to support continuous text scroll:
    - Text is detected within a box. 
    - The box stays the same but text changes
    - Look for some of that text in the "played" queue.
    - If some of the text is found there then cut the text that has not been played yet and add to the queue after the beginning part so that it's seemless.
- The refresh rate is maybe 2 times per second but maybe it can be slowed down if it affects performance.


Interface algorith:
- Open voice choice window with voice samples
- Open transparent full screen window
- Screen capture
- Run through opencv text finder
- Get text coordinates and pass them to tkinter
- Draw a nice box around the text
- Draw buttons
- Pass the text to TTS module to make ready the call
- If the button is pressed then trigger TTS Azure call and get the soundfile





# Text-to-speech
Options:
- Free out-the-box implementation like gTTS
- A pretrained model that is used.
    - I tried Mozilla TTS and I just could not install it to be used within Python. I tried on Mac but worth trying on Linux or Win.
- An option to connect a paid API from Azure, Google Cloud or AWS that will use a good advanced voice.
- Use my own voice to train a good voice. (This may be too advanced and worth the time)
- Use the user's voice to fine tune a pre-trained model.





# General 

- Free Python solution that is open-source. This will be published on my GitHub. It will use a free TTS solution and have an additional ability to plug in your own Azure AI Speech service. This version requires the person to know Python and run it from the terminal and have all the right packages.
Features:
- same functionality
- no ability to connect Azure
- free built in TTS. maybe a few options, whatever I can find.


- Paid version (monthly sub) which is a packaged version that has an .exe file. The payment is to provide good voice from Azure AI Speech. I'm thinking of packaging it in Mojo.
Features:
- Azure AI Speech
- choose the voice upon start
- SSML functionality ?
- Free trial based on number of characters and not time.
