# Recap Time Telegram Bot x pyTelegramBotAPI

In this Glitch project, we host our Recap Time Telegram bot and its code here. Please be note that the codebase you see in GitHub may be not synchorized/updated as what do you see in Glitch.

## Setting up on your own place

### Forking the Example Bot Project

Remix this project to your account to use it. Just click the quick **Remix This** button below to get the latest update,
freshly baked from Glitch. Some things, such as what is stored in `.env` file
are not included when remixing this one.

<a href="https://glitch.com/edit/#!/remix/garnet-crate">
  <img src="https://cdn.glitch.com/2bdfb3f8-05ef-4035-a06e-2043962a3a13%2Fremix%402x.png?1513093958726" alt="remix this" height="33">
</a>

P.S.: If you want the latest commit from GitHub, try this: <https://glitch.com/edit/#!/remix/github/AndreiJirohHaliliDev2006/RecapTime-TelegramBot>

The another way to remix this is using Git. Follow these:
- Open terminal and type `cd /path/to/your-desired-git-projectname-here`.
- Type `git clone https://github.com/AndreiJirohHaliliDev2006/RecapTime-TelegramBot.git` or `git clone https://api.glitch.com/git/garnet-crate.git`.
Hit Enter (or Return) to start importing source code to your target folder.
- The setup is finished! See [this documentation about pyTelegramBotAPI on GitHub](https://github.com/eternnoir/pyTelegramBotAPI#readme) on how to set up it.
Please skip the installation steps, as the pyTelegramBotAPI is pre-loaded here.
- When you remixed the code on Glitch, it will automatically deployed and available online to work for your Telegram bot.

### Remixing Code

You can configure your code whether you want, but don't forget to read the comments in `telegram-bot-production.py` file and follow environmental variables
template in the `.env.sample` file.

To avoid problems, please test your bot first before deploying for general use. Your bot users must provide an way to get support, such as our `/support` command implementation.

Also, we made `telegram-bot-staging.py` file for you to play codes there. (Stay tuned for any commits for that file.)

## See in action

> **WARNING: The official bot is under canary testing! Not for production use.**
> The bot is currently in canary testing. Please use it at your own risk.
> In case the bot ran into problems, please notify me on Telegram at [Recap Time Live Chat](https://t.me/RecapTime_LiveChat) or [create an new issue on GitHub](https://github.com/AndreiJirohHaliliDev2006/RecapTime-TelegramBot/issues/new).
>
> You can also help in improving the codebase to make the bot better. See `CONTRIBUTING.md` for more info.

To see how this bot works in action and in realtime, start a Telegram chat with the official Recap Time bot at <https://t.me/RecapTime_bot>.
