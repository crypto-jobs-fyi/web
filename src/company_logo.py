def build_img_tag(name):
    return f'<img src="resources/{name}.png" alt="{name.title()}" loading="lazy" width="188" height: auto >'


def get_logo(company_name):
    company_logos = [
        'galaxydigitalservices',
        'ethereumfoundation',
        'chainsafesystems',
        'ramp.network',
        'econetwork',
        'penumbralabs',
        'gauntlet', 'kadena',
        'royal', 'swissborg',
        'copperco',
        'messari', 'Coinshift',
        'storyprotocol',
        'tron', 'OpenSea',
        'subspacelabs',
        'digitalasset',
        'exodus54', 'request',
        'offchainlabs',
        'tokenmetrics',
        'crypto', 'syndica',
        'aave', 'Swissquote',
        'alchemy', 'immutable',
        'amun', 'ellipsislabs',
        'dfinity', 'web3auth',
        'parity', 'kiln',
        'ankr', 'ultra',
        'solana', 'osmosisdex',
        'ledger', 'Keyrock',
        'flashbots',
        'oplabs', 'optimism',
        'bitfinex',
        'magiceden',
        'nethermind',
        'trustwallet',
        'coinmarketcap',
        'chainalysis',
        'quiknodeinc',
        'wintermute',
        'mobilecoin',
        'bitpanda',
        'bitgo', 'blox-route',
        'shardeum',
        'bitmex', 'StationLabs',
        'OKX', 'jumpcrypto',
        'tether', 'poap',
        'paradigm.co',
        'paradigm.xyz',
        'dune', 'cere-network',
        'bitfury', 'enso',
        'archblock', 'dourolabs',
        '0x', 'oasisnetwork',
        'chia', 'iofinnet',
        'AQX', 'conduit',
        'kraken', 'taxbit',
        'ethglobal', 'linera.io',
        'harmony', 'theblock',
        'bebop', 'Notabene',
        'chainstack',
        'chainlink', 'phantom',
        'axiomzen', 'bitwise',
        'paxos', 'with-foundation',
        'eigenlabs', 'HQxyz',
        'bitcoin', 'brave',
        'tatum', 'binance',
        'bitget', 'hextrust',
        'stably', 'bitstamp',
        'consensys', 'ripple',
        'aztec', 'toku',
        'stellar', 'sygnum',
        'okcoin', 'matterlabs',
        'clearmatics', 'worldcoin',
        'edgeandnode', 'risklabs',
        'exponential', 'circle',
        'auroralabs', 'rain',
        'kaiko', 'coinmetrics',
        'hiro', 'serotonin',
        'zora', 'aptoslabs',
        'filecoinfoundation',
        'celestia', 'gate.io',
        'polymerlabs', 'lido',
        'uniswaplabs', 'li.fi',
        'moonpay', 'swellnetwork',
        'moonwalk', 'near',
        'figment', 'blockdaemon',
        'avalabs', 'Polygon',
        'base', 'injectivelabs',
        'multiversx',
        'status', 'Blockworks',
        'cexio', 'ethenalabs',
        'dappradar',
        'web3', 'xapo',
        '21co', 'goldsky',
        'smart-token-labs',
        'avantgarde',
        'cryptofinance',
        'Luxor', 'wirex',
        'anchorage', 'Tenderly',
        'dydx', 'biconomy',
        'solanafoundation',
        'fuellabs', 'iyield',
        'immunefi', 'obol-tech',
        'protocollabs',
        'foundrydigital',
        'o1labs', 'trmlabs',
        '3boxlabs', 'coinspaid',
        'BlockSwap', 'fortress',
        'orderlynetwork',
        'sprucesystems',
        'arbitrumfoundation',
        'magic', 'evmos',
        'outlierventures',
        'walletconnect',
        'almanak', 'dydxopsdao',
        'grayscaleinvestments',
        'prepo', 'safe.global',
        'RabbitHole', 'clockwork-labs',
        'Sui.Foundation', 'center',
        'paraswap', 'stakefish',
        'connext-network',
        'request.network',
        'superfluid', 'thetie',
        'glassnode', 'impossiblecloud',
        'zodia-custody', 'Bastion',
        'Artemisxyz', 'cryptio',
        'scroll', 'cointracker',
        'coinbase', 'gemini',
        'tusd', 'enjin',
        'nomic.foundation',
        'mina-foundation',
        'pyth', 'coingecko',
        'omni-network', 'windranger',
        'mystenlabs', 'emergentx',
        'aragon', 'animocabrands',
    ]
    if company_name in company_logos:
        return build_img_tag(company_name)
    return company_name.upper()
