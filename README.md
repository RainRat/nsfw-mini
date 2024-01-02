"# NSFW-mini" 

A neural network that you can download, that takes an image and returns a score based on how NSFW it is. This is a smaller version of one I've used in my Telegram bot.

I'm not the first to try making a neural network to try to distinguish SFW from NSFW, but there's a combination of advantages here:

1. Trained on both furry art, and photographs. So it can interpret the features of either type of image.
2. You can actually download it. Commercial NSFW detectors usually have you upload the image to them and they do the processing on their services. With mine, you can even process offline.
3. Small and fast (for a neural network). With reasonable hardware, it would be possible to process video in real time.
4. Not sure how to put this, but hopefully you will find the tagging fairly open-minded. The rating instruction was to only mark it NSFW if it would be disallowed in all SFW groups. The network should reflect this.

The neural network is distributed with small python program to demonstrate it with your webcam. To use the demo, you'll need a computer with a webcam.

1. Install python, and the packages opencv and tensorflow.
2. type "python nsfw-mini.py"
3. Press "q" in the window when you are done.

Internally, the neural network returns a number between 0 and 1, but in the demo, it is formatted as a percentage for human use.

Hopefully you find the demo interesting, but I distribute the whole network in the hopes that programmers can use it in their own pipelines. Content distributors sometimes throw up their hands at posting user-generated content because they don't have any way to sift through everything and separate likely-SFW from likely-NSFW.

A reminder that it isn't infallible, and you shouldn't take punitive action based on the results. For instance your site might quarantine anything over 95% SFW until reviewed by a moderator, while 50% to 95% NSFW is let through and prioritized for moderators when available. If you have a use case where it doesn't seem to be catching on to your needs, contact me to discuss possibly training a custom model.
