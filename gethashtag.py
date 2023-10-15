teamHashtagsNBA = {
    'Hawks': '#TrueToAtlanta',
    'Celtics': '#DifferentHere',
    'Nets': '#NetsWorld',
    'Hornets': '#LetsFly',
    'Bulls': '#BullsNation',
    'Cavaliers': '#LetEmKnow',
    'Mavericks': '#MFFL',
    'Nuggets': '#MileHighBasketball',
    'Pistons': '#Pistons',
    'Warriors': '#DubNation',
    'Rockets': '#Rockets',
    'Pacers': '#BoomBaby',
    'Clippers': '#ClipperNation',
    'Lakers': '#LakeShow',
    'Grizzlies': '#BigMemphis',
    'Heat': '#HeatCulture',
    'Bucks': '#FearTheDeer',
    'Timberwolves': '#RaisedByWolves',
    'Pelicans': '#Pelicans',
    'Knicks': '#NewYorkForever',
    'Thunder': '#ThunderUp',
    'Magic': '#MagicTogether',
    '76ers': '#BrotherlyLove',
    'Suns': '#WeAreTheValley',
    'Blazers': '#RipCity',
    'Kings': '#SacramentoProud',
    'Spurs': '#PorVida',
    'Raptors': '#WeTheNorth',
    'Jazz': '#TakeNote',
    'Wizards': '#DCAboveAll'
}


def getHashtagFromHeaderNBA(header):
    """
    Picks a team hashtag from header text if applicable
    """
    payload = []

    for word in header.split():
        if '-' in word:
            words = word.split('-')
            for w in words:
                if w in teamHashtagsNBA:
                    payload.append(teamHashtagsNBA[w])
        elif word in teamHashtagsNBA:
            payload.append(teamHashtagsNBA[word])

    return payload
