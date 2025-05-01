import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_saml_settings():
    return {
        'strict': True,
        'debug': True,
        'sp': {
            'entityId': 'http://localhost:8000/sso/saml/metadata/',
            'assertionConsumerService': {
                'url': 'http://localhost:8000/sso/saml/acs/',
                'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
            },
            'singleLogoutService': {
                'url': 'http://localhost:8000/sso/saml/logout/',
                'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
            },
            'NameIDFormat': 'urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress',  # ✅ Required
            'x509cert': '',
            'privateKey': '',
        },
        'idp': {
            'entityId': 'http://www.okta.com/exkohf5ub1PaOtCuN5d7',
            'singleSignOnService': {
                'url': 'https://dev-53717893.okta.com/app/dev-53717893_djangosaml_1/exkohf5ub1PaOtCuN5d7/sso/saml',
                'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
            },
            'singleLogoutService': {
                'url': 'https://dev-53717893.okta.com',
                'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
            },
            'x509cert': open(os.path.join(BASE_DIR, 'employee/OKTA/okta.cert')).read(),
        },
        'security': {
            'authnRequestsSigned': False,
            'logoutRequestSigned': False,
            'logoutResponseSigned': False,
            'signMetadata': False,
            'wantMessagesSigned': False,
            'wantAssertionsSigned': False,
            'wantNameId': True,
            'wantNameIdEncrypted': False,
        },
        'attribute_mapping': {
            'User.email': 'email',
            'User.first_name': 'firstName',
            'User.last_name': 'lastName',
        },
    }
