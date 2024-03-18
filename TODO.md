

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
    - A zone is selected that the user wants the program to monitor.
        - The buttons I mention above appear next to these
    - A one-off zone that is selected and the text within it played immediately after selection.
    - A button to show or hide the zones' bounding boxes
        - Maybe have a setting that allows to set the colour, the brightness and prominence of the bounding boxes.
- Ability to support continuous text scroll:
    - Text is detected within a box. 
    - The box stays the same but text changes
    - Look for some of that text in the "played" queue.
    - If some of the text is found there then cut the text that has not been played yet and add to the queue after the beginning part so that it's seemless.
- The refresh rate is maybe 2 times per second but maybe it can be slowed down if it affects performance.
- Where do the buttons appear around the bounding box. Maybe a setting that allows the person to set it various corners around the bounding box
    - if the buttons would appear off-screen then change them to the next available position in the pecking order
- The appearance of the bounding box:
    - The colour
    - Maybe some cool animation
    - The thickness
- The appearance of the buttons:
    - size
    - high contrast
- Have an always on top button somewhere on screen that enables or disables the system.
    - It will disable the drawing of bounding boxes.
- Upon launch there should be a window that pulls a message from backend. This is a message from me about updates and other things.
- What do I do with multiple monitor setups?

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
- Monetisation:
    - Monthly
    - Token purchase
        - I'm leaning more towards this as this is easier to translate to usage. A person might use a lot of tokens quickly if they are blasting through games whereas another might be playing games much slower. This way they don't get that feeling from a subscription.
        - It's much eaier for me to do costing - essentially 1 character from Azure AI Speech + other Azure service costs + margins. If I did it monthly I would need to estimate how much an average user would user and charge a monthly fee which might be good for those users who play a lot and bad for those who do not.
- Here is how I envision the paid model to work:
    - The user registers on the website - create an account
    - They get a key that they input into the software
    - When the software makes an API call to my Azure AI Speech service it checks the account and then sends back the processed audio file.
    - How to handle authentication? Can every single API call authenticate user?
    - Every single call checks how many tokens are left in the user's account.
        - Notifies with a popup when the tokens are finished.
- As a result of me doing doing a manual selection of the reading zone I am able to offer 2 paid versions:
    - The cheaper version but it involves data collection of the screenshot and the zone selection - both predetermined and one-off. I will use this data to train a text identification model.
    - The full price version that does not collect this data.