def currency_rates(date):
    try:
        from requests import get, utils
        result = {}
        response = get('http://www.cbr.ru/scripts/XML_daily.asp')
        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encodings)
        content = content.split('</Valute>')
        for i in content:
            i = i.split("><")
            for x in i:
                if x.startswith('CharCode>'):
                    point = x[x.find('>') + 1: x.find('>') + 4]
                    result.setdefault(point)
        for z in result.keys():
            for blocks in content:
                if z in blocks:
                    point_value = blocks[blocks.find('<Value>') + 7: blocks.find('</Value>')]
                    result[z] = point_value
        return result[date.upper()], response.headers['Date']
    except:
        return None