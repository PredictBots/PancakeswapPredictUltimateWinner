from ethersproject.units import parse_ether
from util import promisify
from lib import get_stats, prediction_contract, get_bnb_price, check_balance, reduce_waiting_time_by_two_blocks, save_round
from trading_view_recommends_parser_nodejs import TradingViewScan, SCREENERS_ENUM, EXCHANGES_ENUM, INTERVALS_ENUM

# Global Config
GLOBAL_CONFIG = {
    'BET_AMOUNT': 3,  # in USD
    'THRESHOLD': 30  # Minimum % of certainty of signals (50 - 100)
}

# Bet UP
async def bet_up(amount, epoch):
    try:
        tx = await prediction_contract.bet_bull(epoch, {
            'value': parse_ether(amount.toFixed(18).toString())
        })
        await tx.wait()
        print(f'Successful {amount} BNB to UP ')
    except Exception as error:
        print('Transaction Error', error)
        GLOBAL_CONFIG['WAITING_TIME'] = reduce_waiting_time_by_two_blocks(GLOBAL_CONFIG['WAITING_TIME'])

# Bet DOWN
async def bet_down(amount, epoch):
    try:
        tx = await prediction_contract.bet_bear(epoch, {
            'value': parse_ether(amount.toFixed(18).toString())
        })
        await tx.wait()
        print(f'Successful {amount} BNB to DOWN ')
    except Exception as error:
        print('Transaction Error', error)
        GLOBAL_CONFIG['WAITING_TIME'] = reduce_waiting_time_by_two_blocks(GLOBAL_CONFIG['WAITING_TIME'])

# Check Signals
async def get_signals():
    # 1 Minute signals
    result_min = await TradingViewScan(
        SCREENERS_ENUM['crypto'],
        EXCHANGES_ENUM['BINANCE'],
        'BNBUSDT',
        INTERVALS_ENUM['1m']
    ).analyze()
    min_obj = JSON.stringify(result_min.summary)
    min_recommendation = JSON.parse(min_obj)

    # 5 Minute signals
    result_med = await TradingViewScan(
        SCREENERS_ENUM['crypto'],
        EXCHANGES_ENUM['BINANCE'],
        'BNBUSDT',
        INTERVALS_ENUM['5m']
    ).analyze()
    med_obj = JSON.stringify(result_med.summary)
    med_recommendation = JSON.parse(med_obj)

    if min_recommendation and med_recommendation:
        average_buy = (int(min_recommendation['BUY']) + int(med_recommendation['BUY'])) / 2
        average_sell = (int(min_recommendation['SELL']) + int(med_recommendation['SELL'])) / 2
        average_neutral = (int(min_recommendation['NEUTRAL']) + int(med_recommendation['NEUTRAL'])) / 2

        return {
            'buy': average_buy,
            'sell': average_sell,
            'neutral': average_neutral
        }
    else:
        return False

def percentage(a, b):
    return int(100 * a / (a + b))

# Strategy of betting
async def strategy(min_accuracy, epoch):
    BNB_price = None
    earnings = await get_stats()
    if earnings['profit_USD'] >= GLOBAL_CONFIG['DAILY_GOAL']:
        print('🧙‍ Daily goal reached. Shuting down... ✨ ')
        sys.exit()
    try:
        BNB_price = await get_bnb_price()
    except Exception as err:
        return
    signals = await get_signals()
    if signals:
        if signals['buy'] > signals['sell'] and percentage(signals['buy'], signals['sell']) > min_accuracy:
            print(f'{epoch.toString()} Prediction: UP  {percentage(signals["buy"], signals["sell"])}%')
            await bet_up((GLOBAL_CONFIG['BET_AMOUNT'] / BNB_price), epoch)
            await save_round(epoch.toString(), [{'round': epoch.toString(), 'betAmount': (GLOBAL_CONFIG['BET_AMOUNT'] / BNB_price).toString(), 'bet': 'bull'}])
        elif signals['sell'] > signals['buy'] and percentage(signals['sell'], signals['buy']) > min_accuracy:
            print(f'{epoch.toString()} Prediction: DOWN  {percentage(signals["sell"], signals["buy"])}%')
            await bet_down((GLOBAL_CONFIG['BET_AMOUNT'] / BNB_price), epoch)
            await save_round(epoch.toString(), [{'round': epoch.toString(), 'betAmount': (GLOBAL_CONFIG['BET_AMOUNT'] / BNB_price).toString(), 'bet': 'bear'}])
        else:
            low_percentage = percentage(signals['buy'], signals['sell']) if signals['buy'] > signals['sell'] else percentage(signals['sell'], signals['buy'])
            print(f'Waiting {low_percentage}%')
    else:
        print('Error obtaining signals')

check_balance(GLOBAL_CONFIG['AMOUNT_TO_BET'])

print(' Welcome! Wait next round...')

# Betting
prediction_contract.on('StartRound', async epoch => {
    print(' Starting round ' + epoch.toString())
    print(' Waiting ' + (GLOBAL_CONFIG['WAITING_TIME'] / 60000).toFixed(1) + ' minutes')
    await sleep(GLOBAL_CONFIG['WAITING_TIME'])
    await strategy(GLOBAL_CONFIG['THRESHOLD'], epoch)
})

# Show stats
prediction_contract.on('EndRound', async epoch => {
    await save_round(epoch)
    stats = await get_stats()
})

