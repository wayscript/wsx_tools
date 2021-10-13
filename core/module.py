# Imports

def send_get_request( self, url ):
        return requests.get( url, headers = self.build_auth_header() )

def send_post_request( self, url, data = None, json = None ):
    return requests.post( url, headers = self.build_auth_header(), data = data, json = json )

def send_delete_request( self, url ):
    return requests.delete( url, headers = self.build_auth_header() )

def send_put_request( self, url, data = None, json = None ):
    return requests.put( url, headers = self.build_auth_header(), data = data, json = json )
