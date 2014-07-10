


class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class ClientError(Error):
    """Errors on client side."""
    pass


class RemoteError(Error):
    """Errors on remote end"""
    pass


class NoSessionError(Error):
    """Raised when remote API end-point access is attempted before initialization 
    of session.
    
    """
    pass


class ParseError(Error):
    """Error in parsing data returned by API.
    
    """
    pass


class ParseValueError(Error):
    """Error in parsing value returned by API.
    
    """
    pass


class ParseParamError(Error):
    """Error in parsing parameter passed to API.
    
    """
    pass

