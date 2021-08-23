# Overview
![GitHub repo size](https://img.shields.io/github/repo-size/terratrapezium/modsuggestionsbot)
![GitHub](https://img.shields.io/github/license/terratrapezium/modsuggestionsbot)
![GitHub last commit](https://img.shields.io/github/last-commit/terratrapezium/modsuggestionsbot)

Quick [discord.py](https://github.com/Rapptz/discord.py) bot to add reactions to every message sent in a channel, used for gathering tModLoader mod suggestions.

## Setup
- Clone the repo with `git clone https://github.com/TerraTrapezium/ModSuggestionsBot.git`
- Create a `.env` file in the root directory (See [dotenv](#dotenv) below)
- Run the bot using `py react.py`

## Dotenv
Example `.env` file:
```
TOKEN=bot token here
CHANNEL_ID=849058117773033513
```

| property | use |
| --- | --- |
| **`TOKEN`** | discord bot token |
| **`CHANNEL_ID`** | channel id that you want reactions in |

<details><summary><strong>How do I get a Discord bot token?</strong></summary>
Go to https://discordapp.com/developers.

Click `My apps` in the top left:

![img](https://i.imgur.com/msNDtLt.png)
Click `New App`:

![img](https://i.imgur.com/zSTbluP.png)
Give your bot a name and optionally a description and avatar:  

![img](https://i.imgur.com/mwmIn1y.png)
Click `Create App`:

![img](https://i.imgur.com/MbH7tX2.png)
Scroll down and click `Create a Bot User`:

![img](https://i.imgur.com/G4L7X0l.png)
Click `Yes, do it!`:

![img](https://i.imgur.com/Mdfar29.png)
Click `click to reveal` nex to `Token:`:

![img](https://i.imgur.com/sOIvcXU.png)
</details>
