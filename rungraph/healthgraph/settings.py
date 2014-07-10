
API_AUTHORIZATION_URL = 'https://runkeeper.com/apps/authorize'
API_DEAUTHORIZATION_URL = 'https://runkeeper.com/apps/de-authorize'
API_ACCESS_TOKEN_URL = 'https://runkeeper.com/apps/token'
LOGIN_BUTTON_URL = "http://static1.runkeeper.com/images/assets/login-%s-%s-%s.png"
LOGIN_BUTTON_COLORS = ( 'blue', 'grey', 'black',)
LOGIN_BUTTON_SIZES = {200: '200x38',
                      300: '300x57',
                      600: '600x114',
                      None: '200x38',}
LOGIN_BUTTON_CAPTION_COLORS = ('white', 'black',)

API_URL = 'https://api.runkeeper.com'
USER_RESOURCE = '/user'
DEFAULT_PAGE_SIZE = 25

NUM2MONTH = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
             'Nov','Dec',)
MONTH2NUM = dict(zip(NUM2MONTH,range(1,13)))