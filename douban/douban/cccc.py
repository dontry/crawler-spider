import json
import io

d = {u'keyword': u'bad credit  \xe7redit cards'}
with io.open('filename', 'w', encoding='utf-8') as json_file:
    data = json.dumps(d, ensure_ascii=False).decode('utf-8')
    try:
        json_file.write(data)
    except TypeError:
        # Decode data to Unicode first
        json_file.write(data.decode('utf8'))
