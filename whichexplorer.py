# Created by CQ

import re
import sys
import webbrowser


ASSET_REGEX = {
	'BTC': r'\bbc1[02-9ac-hj-np-z]{11,71}\b|\b[13][a-zA-HJ-NP-Z0-9]{23,39}\b',
	'LTC': r'\bltc1[02-9ac-hj-np-z]{10,71}$|\b[LM][a-km-zA-HJ-NP-Z1-9]{26,33}\b',
	'BCH': r'\bbitcoincash:q[a-z0-9]{41}\b|\bq[a-z0-9]{41}\b',
	'ZEC': r'\bt[123][a-zA-HJ-NP-Z0-9]{33}$|\bzs[02-9ac-hj-np-z]{76}\b|\bzc[a-zA-HJ-NP-Z0-9]{93}\b',
	'ETH': r'\b0x[a-fA-F0-9]{40}\b',
	'DASH': r'\bX[1-9A-HJ-NP-Za-km-z]{33}\b',
	'XMR': r'\b[48][0-9AB][1-9A-HJ-NP-Za-km-z]{93}\b',
	'XRP': r'\br[0-9a-zA-Z]{33}\b',
	'ZIL': r'\bzil1[a-hj-np-z0-9]{38}\b',
	'BNB': r'\bbnb1[a-hj-np-z0-9]{38}\b',
	'XLM': r'\b[G][A-Z0-9]{55}\b',
	'ZEN': r'\bzn[a-km-zA-HJ-NP-Z1-9]{24,33}\b',
	'XTZ': r'\bKT1[1-9A-HJ-NP-Za-km-z]{33}\b|\btz[1,2,3][1-9A-HJ-NP-Za-km-z]{33}\b', #Guessed by yours truly
	'CRO': r'^\b(cro|crocncl|crocnclcons)[a-zA-HJ-NP-Z0-9]{39}\b',
	# 'ADA': r'',
	'DOGE': r'\bD{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}\b',
	'SOL': r'\b[1-9A-HJ-NP-Za-km-z]{32,44}\b',
	'NEAR': r'^(([a-z\d]+[\-_])*[a-z\d]+\.)*([a-z\d]+[\-_])*[a-z\d]+$' #From near foundation & converted, not the best so put at the bottom
}

ADDRESS_URL = {
	'blockchair': {'BTC': 'https://blockchair.com/bitcoin/address', 'BCH': 'https://blockchair.com/bitcoin-cash/address/'},
	'etherscan': {'ETH': 'https://etherscan.io/address/'},
	'tzkt.io': {'XTZ': 'https://tzkt.io/'},
	'explorer.near.org': {'NEAR':'https://wallet.near.org/profile/'},
	'mintscan': {'BNB':'https://binance.mintscan.io/account/'},
	'crypto.com': {'CRO':'https://crypto.org/explorer/account/'}

}
# List of assets to cover: 
# BTC, ETH, LTC, BCH, ZEC, 
PREFERENCES = {
	'BTC': 'blockchair',
	'LTC': 'blockchair',
	'BCH': 'blockchair',
	'ZEC': 'blockchair',
	'ETH': 'etherscan',
	'DASH': 'blockchair',
	'XMR': '',
	'XRP': '',
	'ZIL': '',
	'BNB': 'mintscan',
	'XLM': '',
	'ZEN': '',
	'XTZ': 'tzkt.io',
	'NEAR': 'explorer.near.org',
	'CRO': 'crypto.com',
	'ADA': '',
	'DOGE': 'blockchair',
	'SOL': ''
}


def asset_from_address(address) -> str or None:
	for asset, regex in ASSET_REGEX.items():
		if bool(re.fullmatch(regex, address)):
			return asset
	return None

for line in sys.stdin:

	addr = str(line.rstrip())
	print(f"line from sys.stdin is: {addr}")

	asset = asset_from_address(addr)
	if asset is None:
		print(f"No asset matched")
		continue
		
	print(f"Asset is: {asset_from_address(addr)}")

	preference = PREFERENCES[asset]
	print(f"Preference vendor is: {preference}")

	addr_url = ADDRESS_URL[preference][asset] + addr
	print(f"address url is: {addr_url}")

	webbrowser.open(addr_url)

	if 'q' == line.rstrip():
		break


