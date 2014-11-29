import scraperwiki
from apiclient.discovery import build as discovery_build

tableId = '08198754560717916103-08551925598041685897'
electionKey = 'victorian_election_2014'
publicAPIKey = 'AIzaSyBuOuavKmg0pKmdGEPdugThfnKQ7v1sSH0'

resource = discovery_build('mapsengine', 'v1', developerKey=publicAPIKey)
features = resource.tables().features().list(
    id=tableId,
    version='published',
    where='has_bbq = 1 OR has_caek = 1 OR has_nothing = 1',
    maxResults=1000).execute()

scraperwiki.sqlite.save(unique_keys=['election'], data={'election': electionKey, 'count': len(features['features'])})
