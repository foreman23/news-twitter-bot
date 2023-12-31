teamHashtagsNBA = {
    'Hawks': '#TrueToAtlanta',
    'Celtics': '#DifferentHere',
    'Nets': '#NetsWorld',
    'Hornets': '#LetsFly',
    'Bulls': '#BullsNation',
    'Cavaliers': '#LetEmKnow',
    'Cavs': '#LetEmKnow',
    'Mavericks': '#MFFL',
    'Mavs': '#MFFL',
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
    'Sixers': '#BrotherlyLove',
    'Suns': '#WeAreTheValley',
    'Blazers': '#RipCity',
    'Kings': '#LightTheBeam',
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
        # Check for apostrophe
        if "'" in word:
            # ex. Lakers' or Thunder's
            if word[len(word) - 1] == "'" or word[len(word) - 2] == "'":
                split_word = word.split("'")
                if split_word[0] in teamHashtagsNBA:
                    payload.append(teamHashtagsNBA[split_word[0]])

        if '-' in word:
            words = word.split('-')
            for w in words:
                if w in teamHashtagsNBA:
                    payload.append(teamHashtagsNBA[w])
        elif word in teamHashtagsNBA:
            payload.append(teamHashtagsNBA[word])

    return payload
