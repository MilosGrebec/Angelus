Angelus is a video security platform. Originally, it was made as a baby monitor with some additional features.

Angelus is made in python using PyCharm. For the PC side, it’s made with the CustomTkinter library and, for the smartphone side, the KivyMD framework is used.
Voice recognition is done using Google’s Cloud Speech-to-Text API.

Angelus is divided into two apps, one on PC and one on a smartphone.
The PC side Angelus sends frames via sockets from your PC camera to the smartphone.
Also, PC Angelus works on voice commands and does things according to those commands.

On the PC side Angelus, you need a camera that's connected to the PC and is watching that object/place you want to monitor, and a mic if you want.

This is how the PC side of Angelus looks.
<img width="515" height="482" alt="image" src="https://github.com/user-attachments/assets/bc2c25bb-5901-48ce-be6a-d0aee6af8daf" />

You need to input a host ip that is shown and then connect. The reason why I didn't make it to automatically connect is that someone can have 2 host ips (it happened and only one works for this purpose). Not really sure why, but this is just a defense against it.
After that, you input the same IP to the mobile side, and then you will have a live video of your object and history when something on the screen (video) moves.

Btw, if you want to see Angelus voice assistant features (these are those additional features), you just press the Angelus logo, and he will start listening.
Depending on voice commands, he can sing, tell you a random fact or search the internet for you.

Here is how mobile Angelus looks.

<img width="294" height="470" alt="image" src="https://github.com/user-attachments/assets/885a62ba-f949-4e85-8517-f4acc5995d56" />
