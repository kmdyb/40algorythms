# transport layer security protocol utilising a trusted certificate authority
from xmlrpc.client import SafeTransport, ServerProxy
import ssl


class CertVerify(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if certfile:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def make_connection(self, host):
        s = super().make_connection((host, {'context': self._ssl_context}))
        return s

    s = ServerProxy('https://cloudanum.com:15000', transport=__init__('server_cert.pem'), allow_none=True)
