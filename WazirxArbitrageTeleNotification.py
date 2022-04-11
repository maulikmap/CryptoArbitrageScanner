import datetime as dt
import time
import requests
import json

#response = requests.get("https://api.wazirx.com//api/v2/tickers")
        
def parse_market_data(data):
    #print(data)
    print("Step - 2")

    coins_name = ['btc', 'trx', 'xrp', 'eos', 'eth', 'qkc', 'zil', 'ncash', 'icx', 'ltc', 'tusd', 'hot', 'bat', 'dash', 'zrx', 'bch', 'bchsv', 'pax', 'usdc', 'omg', 'poly', 'dent', 'iost', 'fun', 'snt', 'theta', 'req', 'xlm', 'xtz', 'btt', 'fet', 'tfuel', 'celr', 'matic', 'ada', 'rvn', 'xmr', 'atom', 'algo', 'link', 'qtum', 'etc', 'iota', 'zec', 'waves', 'ftm', 'enj', 'lsk', 'steem', 'xvg', 'loom', 'mana', 'rep', 'blz', 'nano', 'sc', 'btg', 'xem', 'bts', 'ardr', 'nas', 'win', 'bnb', 'chz', 'wrx', 'kava', 'ankr', 'busd', 'one', 'hive', 'ftt', 'band', 'jst', 'ctsi', 'chr', 'tomo', 'stmx', 'gxs', 'lrc', 'doge', 'neo', 'hbar', 'storj', 'comp', 'coti', 'dgb', 'grs', 'snx', 'ren', 'sxp', 'mkr', 'ava', 'bal', 'srm', 'egld', 'cos', 'nbs', 'aion', 'dot', 'yfi', 'iotx', 'sand', 'uni', 'data', 'paxg', 'cream', 'uma', 'ksm', 'yfii', 'bzrx', 'trb', 'adx', 'aave', 'fil', 'crv', 'near', 'hnt', 'avax', 'oxt', 'dock', 'dusk', 'wtc', 'strax', 'inj', 'vet', 'mtl', 'front', 'glm', 'sushi', 'firo', 'dexe', 'grt', 'bcha', 'bnt', 'rsr', '1inch', 'luna', 'uft', 'pundix', 'ckb', 'vib', 'gto', 'tko', 'push', 'cvc', 'cake', 'ez', 'ark', 'kmd', 'shib', 'rlc', 'reef', 'icp', 'ont', 'xvs', 'xmgd', 'xoom', 'xstyx', 'xbck', 'xpro', 'xyit', 'xtbe', 'xvols', 'xcbt', 'xnis', 'xbstf', 'xfact', 'xolo', 'xstr', 'xpayi', 'xmint', 'xjidt']

    #Price Convert
    inr_usdt = [x for x in data if x['quoteMarket'] == 'inr' and x['status'] == 'active' and x['baseMarket'] == 'usdt']
    inr_usdt = float(inr_usdt[0]['last'])

    inr_wrx = [x for x in data if x['quoteMarket'] == 'inr' and x['status'] == 'active' and x['baseMarket'] == 'wrx']
    inr_wrx = float(inr_wrx[0]['last'])

    inr_btc = [x for x in data if x['quoteMarket'] == 'inr' and x['status'] == 'active' and x['baseMarket'] == 'btc']
    inr_btc = float(inr_btc[0]['last'])

    try:
        for i in coins_name:

            diff = []
            diff_value = []
            notification_message = []
            print("Step - 3")

            inr_market = [x for x in data if x['quoteMarket'] == 'inr' and x['status'] == 'active' and x['baseMarket'] == i]
        
            usdt_market = [x for x in data if x['quoteMarket'] == 'usdt' and x['status'] == 'active' and x['baseMarket'] == i]
            
            wrx_market = [x for x in data if x['quoteMarket'] == 'wrx' and x['status'] == 'active' and x['baseMarket'] == i]
            
            btc_market = [x for x in data if x['quoteMarket'] == 'btc' and x['status'] == 'active' and x['baseMarket'] == i]

            if (len(inr_market) != 0 and len(usdt_market) != 0 and len(btc_market) != 0):

                print("Step - 4")
                for y in btc_market:
                    btc = float(y['last']) * inr_btc

                for y in inr_market:
                    inr = float(y['last'])

                for y in wrx_market:
                    wrx = float(y['last']) * inr_wrx

                for y in usdt_market:
                    usdt = float(y['last']) * inr_usdt

                # find difference between numbers
                diff.append(abs(inr - usdt)) #diff_inr_usdt
                diff.append(abs(inr - btc))  #diff_inr_btc
                diff.append(abs(btc - usdt)) #diff_btc_usdt
                if(len(wrx_market) != 0):
                    diff.append(abs(btc - wrx)) #diff_btc_wrx
                    diff.append(abs(inr - wrx)) #diff_inr_wrx
                    diff.append(abs(wrx - usdt)) #diff_wrx_usdt

                diff_perc = inr * 0.1  #It is 10% of actual price, You can change this % value to set your arbitraige observations.
                
                title = "i_u | i_b | b_u | b_w | i_w | w_u"
                notification_message.append(i)
                notification_message.append(inr)
                notification_message.append(title)

                for k in range(0,len(diff)):
                    print("Step - 5")
                    if diff[k] >= diff_perc:
                        diff_value.append(diff[k])
                        #print(notification_message)
                    else:
                        diff_value.append(0)
                
                #print(diff)
                
                if sum(diff_value) > 0:
                    notification_message.extend(diff_value)

                    bot_token = '' # add your telegram token and chatID detials here.
                    bot_chatID = ''
                    tele_bot_url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + format(notification_message)

                    requests.get(tele_bot_url)
                    print("Done")
    except:
        return "0"

def main():
    try:
        response = requests.get('https://api.wazirx.com/api/v2/market-status')
        if response.status_code == 200:
            print("Step - 1")
            data = response.json()
            return(parse_market_data(data['markets']))
        return "0"
    except:
        return "0"

if __name__ == "__main__":
    main()