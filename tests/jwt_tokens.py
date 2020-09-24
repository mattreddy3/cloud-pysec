# pylint: disable=line-too-long
''' Test jwt tokens '''
import jwt
from tests.keys import PRIVATE_KEY


def token(payload):
    return jwt.encode({**DEFAULT_END_USER_TOKEN_PAYLOAD, **payload}, PRIVATE_KEY, algorithm="RS256",
                      headers=END_USER_TOKEN_HEADERS).decode("utf-8")


END_USER_TOKEN_HEADERS = {
    "jku": "https://api.cf.test.com",
    "kid": "key-id-0"
}

DEFAULT_END_USER_TOKEN_PAYLOAD = {
    "jti": "c6831125-1ed6-41b0-8ea8-e60a341a2787",
    "sub": "425130",
    "scope": [
        "openid",
        "uaa.resource"
    ],
    "client_id": "sb-xssectest",
    "cid": "sb-xssectest",
    "azp": "sb-xssectest",
    "grant_type": "password",
    "user_id": "425130",
    "user_name": "NODETESTUSER",
    "email": "Nodetest@sap.com",
    "origin": "testidp",
    "given_name": "NodetestFirstName",
    "family_name": "NodetestLastName",
    "iat": 1470815434,
    "exp": 2101535434,
    "iss": "http://paas.localhost:8080/uaa/oauth/token",
    "zid": "test-idz",
    "hdb.nameduser.saml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><saml2:Assertion xmlns:saml2=\"urn:oasis:names:tc:SAML:2.0:assertion\" ID=\"_71ee1776-9d2f-4973-aca8-9e22b2967ac8\" IssueInstant=\"2016-08-10T07:45:34.347Z\" Version=\"2.0\"><saml2:Issuer>TST-saml</saml2:Issuer><ds:Signature xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm=\"http://www.w3.org/2001/10/xml-exc-c14n#\"/><ds:SignatureMethod Algorithm=\"http://www.w3.org/2000/09/xmldsig#rsa-sha1\"/><ds:Reference URI=\"#_71ee1776-9d2f-4973-aca8-9e22b2967ac8\"><ds:Transforms><ds:Transform Algorithm=\"http://www.w3.org/2000/09/xmldsig#enveloped-signature\"/><ds:Transform Algorithm=\"http://www.w3.org/2001/10/xml-exc-c14n#\"/></ds:Transforms><ds:DigestMethod Algorithm=\"http://www.w3.org/2000/09/xmldsig#sha1\"/><ds:DigestValue>ou8r3R0WBHG1bp4KKOx1PyVOiYA=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>LbRKv1r/h7IMmiSyx10WkM7JuekrmwyVNsB53pkFRnrjCGWtmFkQsknsL7eTUN4+gcJGW0qGTUmvUkfXE1O8rf2CmTcC01cYsGAZWbNpOLNmpP9gG6572pveRqjTXLGSilM2ejJiylq2JnFLhXpgrnTbCvQW6a9JTpRpvMz8SiSodxax7rJw7C0yZzUq862M5yNjdoIHhEkngMcC5LDDhfpf6TkQMsyVcMamDqjTS7WTgvkQKl5pkOPKEuhTjCR7P7KAekeDmYoqs7yEZrrdKEixSY4i5F3weM+dw+A1ue9jF2KmeRvjoxs2hwfsWwUvCxy+2Jhr54vatmweG8dI0Q==</ds:SignatureValue></ds:Signature><saml2:Subject><saml2:NameID Format=\"urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified\">NODETESTUSER</saml2:NameID><saml2:SubjectConfirmation Method=\"urn:oasis:names:tc:SAML:2.0:cm:bearer\"><saml2:SubjectConfirmationData NotOnOrAfter=\"2016-08-10T11:50:34.347Z\"/></saml2:SubjectConfirmation></saml2:Subject><saml2:Conditions NotBefore=\"2016-08-10T07:45:34.347Z\" NotOnOrAfter=\"2016-08-10T11:50:34.347Z\"/><saml2:AuthnStatement AuthnInstant=\"2016-08-10T07:50:34.347Z\" SessionNotOnOrAfter=\"2016-08-10T07:55:34.347Z\"><saml2:AuthnContext><saml2:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</saml2:AuthnContextClassRef></saml2:AuthnContext></saml2:AuthnStatement></saml2:Assertion>",
    "az_attr": {
        "external_group": "domaingroup1",
        "external_id": "abcd1234"
    },
    "ext_attr": {
        "serviceinstanceid": "abcd1234",
        "zdn": "paas"
    },
    "xs.system.attributes": {
        "xs.saml.groups": [
            "Canary_RoleBuilder"
        ],
        "xs.rolecollections": []
    },
    "xs.user.attributes": {
        "country": [
            "USA"
        ]
    },
    "aud": [
        "sb-xssectest",
        "openid"
    ]
}

CORRECT_END_USER_TOKEN = token({})

CORRECT_END_USER_TOKEN_NO_ATTR = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiJjNjgzMTEyNS0xZWQ2LTQxYjAtOGVhOC1lNjB' \
    'hMzQxYTI3ODciLCJzdWIiOiI0MjUxMzAiLCJzY29wZSI6WyJvcGVuaWQiLCJ1YWEucmVzb3VyY2' \
    'UiXSwiZXh0X2F0dHIiOnsiemRuIjoicGFhcyJ9LCJjbGllbnRfaWQiOiJzYi14c3NlY3Rlc3QiL' \
    'CJjaWQiOiJzYi14c3NlY3Rlc3QiLCJhenAiOiJzYi14c3NlY3Rlc3QiLCJncmFudF90eXBlIjoi' \
    'cGFzc3dvcmQiLCJ1c2VyX2lkIjoiNDI1MTMwIiwidXNlcl9uYW1lIjoiTk9ERVRFU1RVU0VSIiw' \
    'iZW1haWwiOiJOb2RldGVzdEBzYXAuY29tIiwiZ2l2ZW5fbmFtZSI6Ik5vZGV0ZXN0Rmlyc3ROYW' \
    '1lIiwiZmFtaWx5X25hbWUiOiJOb2RldGVzdExhc3ROYW1lIiwib3JpZ2luIjoidGVzdGlkcCIsI' \
    'mlhdCI6MTQ3MDgxNTQzNCwiZXhwIjoyMTAxNTM1NDM0LCJpc3MiOiJodHRwOi8vcGFhcy5sb2Nh' \
    'bGhvc3Q6ODA4MC91YWEvb2F1dGgvdG9rZW4iLCJ6aWQiOiJ0ZXN0LWlkeiIsImhkYi5uYW1lZHV' \
    'zZXIuc2FtbCI6Ijw_eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVURi04XCI_PjxzYW' \
    '1sMjpBc3NlcnRpb24geG1sbnM6c2FtbDI9XCJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6Y' \
    'XNzZXJ0aW9uXCIgSUQ9XCJfNzFlZTE3NzYtOWQyZi00OTczLWFjYTgtOWUyMmIyOTY3YWM4XCIg' \
    'SXNzdWVJbnN0YW50PVwiMjAxNi0wOC0xMFQwNzo0NTozNC4zNDdaXCIgVmVyc2lvbj1cIjIuMFw' \
    'iPjxzYW1sMjpJc3N1ZXI-VFNULXNhbWw8L3NhbWwyOklzc3Vlcj48ZHM6U2lnbmF0dXJlIHhtbG' \
    '5zOmRzPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI1wiPjxkczpTaWduZWRJb' \
    'mZvPjxkczpDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFsZ29yaXRobT1cImh0dHA6Ly93d3cudzMu' \
    'b3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuI1wiLz48ZHM6U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXR' \
    'obT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyNyc2Etc2hhMVwiLz48ZHM6Um' \
    'VmZXJlbmNlIFVSST1cIiNfNzFlZTE3NzYtOWQyZi00OTczLWFjYTgtOWUyMmIyOTY3YWM4XCI-P' \
    'GRzOlRyYW5zZm9ybXM-PGRzOlRyYW5zZm9ybSBBbGdvcml0aG09XCJodHRwOi8vd3d3LnczLm9y' \
    'Zy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZVwiLz48ZHM6VHJhbnNmb3JtIEF' \
    'sZ29yaXRobT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuI1wiLz48L2' \
    'RzOlRyYW5zZm9ybXM-PGRzOkRpZ2VzdE1ldGhvZCBBbGdvcml0aG09XCJodHRwOi8vd3d3LnczL' \
    'm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMVwiLz48ZHM6RGlnZXN0VmFsdWU-b3U4cjNSMFdCSEcx' \
    'YnA0S0tPeDFQeVZPaVlBPTwvZHM6RGlnZXN0VmFsdWU-PC9kczpSZWZlcmVuY2U-PC9kczpTaWd' \
    'uZWRJbmZvPjxkczpTaWduYXR1cmVWYWx1ZT5MYlJLdjFyL2g3SU1taVN5eDEwV2tNN0p1ZWtybX' \
    'd5Vk5zQjUzcGtGUm5yakNHV3RtRmtRc2tuc0w3ZVRVTjQrZ2NKR1cwcUdUVW12VWtmWEUxTzhyZ' \
    'jJDbVRjQzAxY1lzR0FaV2JOcE9MTm1wUDlnRzY1NzJwdmVScWpUWExHU2lsTTJlakppeWxxMkpu' \
    'RkxoWHBncm5UYkN2UVc2YTlKVHBScHZNejhTaVNvZHhheDdySnc3QzB5WnpVcTg2Mk01eU5qZG9' \
    'JSGhFa25nTWNDNUxERGhmcGY2VGtRTXN5VmNNYW1EcWpUUzdXVGd2a1FLbDVwa09QS0V1aFRqQ1' \
    'I3UDdLQWVrZURtWW9xczd5RVpycmRLRWl4U1k0aTVGM3dlTStkdytBMXVlOWpGMkttZVJ2am94c' \
    'zJod2ZzV3dVdkN4eSsySmhyNTR2YXRtd2VHOGRJMFE9PTwvZHM6U2lnbmF0dXJlVmFsdWU-PC9k' \
    'czpTaWduYXR1cmU-PHNhbWwyOlN1YmplY3Q-PHNhbWwyOk5hbWVJRCBGb3JtYXQ9XCJ1cm46b2F' \
    'zaXM6bmFtZXM6dGM6U0FNTDoxLjE6bmFtZWlkLWZvcm1hdDp1bnNwZWNpZmllZFwiPk5PREVURV' \
    'NUVVNFUjwvc2FtbDI6TmFtZUlEPjxzYW1sMjpTdWJqZWN0Q29uZmlybWF0aW9uIE1ldGhvZD1cI' \
    'nVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpjbTpiZWFyZXJcIj48c2FtbDI6U3ViamVjdENv' \
    'bmZpcm1hdGlvbkRhdGEgTm90T25PckFmdGVyPVwiMjAxNi0wOC0xMFQxMTo1MDozNC4zNDdaXCI' \
    'vPjwvc2FtbDI6U3ViamVjdENvbmZpcm1hdGlvbj48L3NhbWwyOlN1YmplY3Q-PHNhbWwyOkNvbm' \
    'RpdGlvbnMgTm90QmVmb3JlPVwiMjAxNi0wOC0xMFQwNzo0NTozNC4zNDdaXCIgTm90T25PckFmd' \
    'GVyPVwiMjAxNi0wOC0xMFQxMTo1MDozNC4zNDdaXCIvPjxzYW1sMjpBdXRoblN0YXRlbWVudCBB' \
    'dXRobkluc3RhbnQ9XCIyMDE2LTA4LTEwVDA3OjUwOjM0LjM0N1pcIiBTZXNzaW9uTm90T25PckF' \
    'mdGVyPVwiMjAxNi0wOC0xMFQwNzo1NTozNC4zNDdaXCI-PHNhbWwyOkF1dGhuQ29udGV4dD48c2' \
    'FtbDI6QXV0aG5Db250ZXh0Q2xhc3NSZWY-dXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFjO' \
    'mNsYXNzZXM6UGFzc3dvcmQ8L3NhbWwyOkF1dGhuQ29udGV4dENsYXNzUmVmPjwvc2FtbDI6QXV0' \
    'aG5Db250ZXh0Pjwvc2FtbDI6QXV0aG5TdGF0ZW1lbnQ-PC9zYW1sMjpBc3NlcnRpb24-IiwiYXV' \
    'kIjpbInNiLXhzc2VjdGVzdCIsIm9wZW5pZCJdfQ.u4GWH7-e-jI368DDEFSfmaBLcsPa1Vdd37HtUe7BV4Q'

CORRECT_END_USER_TOKEN_NAMES_IN_EXT_ATTR = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29t' \
    'Iiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiJjNjgzMTEyNS0xZWQ2LTQxYjAtOG' \
    'VhOC1lNjBhMzQxYTI3ODciLCJzdWIiOiI0MjUxMzAiLCJzY29wZSI6WyJvcGVuaWQiLCJ1YWEuc' \
    'mVzb3VyY2UiXSwiY2xpZW50X2lkIjoic2IteHNzZWN0ZXN0IiwiY2lkIjoic2IteHNzZWN0ZXN0' \
    'IiwiYXpwIjoic2IteHNzZWN0ZXN0IiwiZ3JhbnRfdHlwZSI6InBhc3N3b3JkIiwidXNlcl9pZCI' \
    '6IjQyNTEzMCIsInVzZXJfbmFtZSI6Ik5PREVURVNUVVNFUiIsImVtYWlsIjoiTm9kZXRlc3RAc2' \
    'FwLmNvbSIsImlhdCI6MTQ3MDgxNTQzNCwiZXhwIjoyMTAxNTM1NDM0LCJpc3MiOiJodHRwOi8vb' \
    'G9jYWxob3N0OjgwODAvdWFhL29hdXRoL3Rva2VuIiwiemlkIjoidGVzdC1pZHoiLCJoZGIubmFt' \
    'ZWR1c2VyLnNhbWwiOiI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz4' \
    '8c2FtbDI6QXNzZXJ0aW9uIHhtbG5zOnNhbWwyPVwidXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi' \
    '4wOmFzc2VydGlvblwiIElEPVwiXzcxZWUxNzc2LTlkMmYtNDk3My1hY2E4LTllMjJiMjk2N2FjO' \
    'FwiIElzc3VlSW5zdGFudD1cIjIwMTYtMDgtMTBUMDc6NDU6MzQuMzQ3WlwiIFZlcnNpb249XCIy' \
    'LjBcIj48c2FtbDI6SXNzdWVyPlRTVC1zYW1sPC9zYW1sMjpJc3N1ZXI-PGRzOlNpZ25hdHVyZSB' \
    '4bWxuczpkcz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyNcIj48ZHM6U2lnbm' \
    'VkSW5mbz48ZHM6Q2Fub25pY2FsaXphdGlvbk1ldGhvZCBBbGdvcml0aG09XCJodHRwOi8vd3d3L' \
    'nczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biNcIi8-PGRzOlNpZ25hdHVyZU1ldGhvZCBBbGdv' \
    'cml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjcnNhLXNoYTFcIi8-PGR' \
    'zOlJlZmVyZW5jZSBVUkk9XCIjXzcxZWUxNzc2LTlkMmYtNDk3My1hY2E4LTllMjJiMjk2N2FjOF' \
    'wiPjxkczpUcmFuc2Zvcm1zPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPVwiaHR0cDovL3d3dy53M' \
    'y5vcmcvMjAwMC8wOS94bWxkc2lnI2VudmVsb3BlZC1zaWduYXR1cmVcIi8-PGRzOlRyYW5zZm9y' \
    'bSBBbGdvcml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biNcIi8' \
    '-PC9kczpUcmFuc2Zvcm1zPjxkczpEaWdlc3RNZXRob2QgQWxnb3JpdGhtPVwiaHR0cDovL3d3dy' \
    '53My5vcmcvMjAwMC8wOS94bWxkc2lnI3NoYTFcIi8-PGRzOkRpZ2VzdFZhbHVlPm91OHIzUjBXQ' \
    'khHMWJwNEtLT3gxUHlWT2lZQT08L2RzOkRpZ2VzdFZhbHVlPjwvZHM6UmVmZXJlbmNlPjwvZHM6' \
    'U2lnbmVkSW5mbz48ZHM6U2lnbmF0dXJlVmFsdWU-TGJSS3Yxci9oN0lNbWlTeXgxMFdrTTdKdWV' \
    'rcm13eVZOc0I1M3BrRlJucmpDR1d0bUZrUXNrbnNMN2VUVU40K2djSkdXMHFHVFVtdlVrZlhFMU' \
    '84cmYyQ21UY0MwMWNZc0dBWldiTnBPTE5tcFA5Z0c2NTcycHZlUnFqVFhMR1NpbE0yZWpKaXlsc' \
    'TJKbkZMaFhwZ3JuVGJDdlFXNmE5SlRwUnB2TXo4U2lTb2R4YXg3ckp3N0MweVp6VXE4NjJNNXlO' \
    'amRvSUhoRWtuZ01jQzVMRERoZnBmNlRrUU1zeVZjTWFtRHFqVFM3V1RndmtRS2w1cGtPUEtFdWh' \
    'UakNSN1A3S0Fla2VEbVlvcXM3eUVacnJkS0VpeFNZNGk1RjN3ZU0rZHcrQTF1ZTlqRjJLbWVSdm' \
    'pveHMyaHdmc1d3VXZDeHkrMkpocjU0dmF0bXdlRzhkSTBRPT08L2RzOlNpZ25hdHVyZVZhbHVlP' \
    'jwvZHM6U2lnbmF0dXJlPjxzYW1sMjpTdWJqZWN0PjxzYW1sMjpOYW1lSUQgRm9ybWF0PVwidXJu' \
    'Om9hc2lzOm5hbWVzOnRjOlNBTUw6MS4xOm5hbWVpZC1mb3JtYXQ6dW5zcGVjaWZpZWRcIj5OT0R' \
    'FVEVTVFVTRVI8L3NhbWwyOk5hbWVJRD48c2FtbDI6U3ViamVjdENvbmZpcm1hdGlvbiBNZXRob2' \
    'Q9XCJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6Y206YmVhcmVyXCI-PHNhbWwyOlN1YmplY' \
    '3RDb25maXJtYXRpb25EYXRhIE5vdE9uT3JBZnRlcj1cIjIwMTYtMDgtMTBUMTE6NTA6MzQuMzQ3' \
    'WlwiLz48L3NhbWwyOlN1YmplY3RDb25maXJtYXRpb24-PC9zYW1sMjpTdWJqZWN0PjxzYW1sMjp' \
    'Db25kaXRpb25zIE5vdEJlZm9yZT1cIjIwMTYtMDgtMTBUMDc6NDU6MzQuMzQ3WlwiIE5vdE9uT3' \
    'JBZnRlcj1cIjIwMTYtMDgtMTBUMTE6NTA6MzQuMzQ3WlwiLz48c2FtbDI6QXV0aG5TdGF0ZW1lb' \
    'nQgQXV0aG5JbnN0YW50PVwiMjAxNi0wOC0xMFQwNzo1MDozNC4zNDdaXCIgU2Vzc2lvbk5vdE9u' \
    'T3JBZnRlcj1cIjIwMTYtMDgtMTBUMDc6NTU6MzQuMzQ3WlwiPjxzYW1sMjpBdXRobkNvbnRleHQ' \
    '-PHNhbWwyOkF1dGhuQ29udGV4dENsYXNzUmVmPnVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMD' \
    'phYzpjbGFzc2VzOlBhc3N3b3JkPC9zYW1sMjpBdXRobkNvbnRleHRDbGFzc1JlZj48L3NhbWwyO' \
    'kF1dGhuQ29udGV4dD48L3NhbWwyOkF1dGhuU3RhdGVtZW50Pjwvc2FtbDI6QXNzZXJ0aW9uPiIs' \
    'ImF1ZCI6WyJzYi14c3NlY3Rlc3QiLCJvcGVuaWQiXSwiZXh0X2F0dHIiOnsiZ2l2ZW5fbmFtZSI' \
    '6Ik5vZGV0ZXN0Rmlyc3ROYW1lRXh0QXR0ciIsImZhbWlseV9uYW1lIjoiTm9kZXRlc3RMYXN0Tm' \
    'FtZUV4dEF0dHIifX0.fJQ22JFxdqyWL22_Uq4cByBSZpTcNG-XVne81W51Sss'

CORRECT_END_USER_TOKEN_SCOPE_UAA_USER = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiJjNjgzMTEyNS0xZWQ2LTQxYjAtOG' \
    'VhOC1lNjBhMzQxYTI3ODciLCJzdWIiOiI0MjUxMzAiLCJzY29wZSI6WyJvcGVuaWQiLCJ1YWEud' \
    'XNlciIsInVhYS5yZXNvdXJjZSJdLCJjbGllbnRfaWQiOiJzYi14c3NlY3Rlc3QiLCJjaWQiOiJz' \
    'Yi14c3NlY3Rlc3QiLCJhenAiOiJzYi14c3NlY3Rlc3QiLCJncmFudF90eXBlIjoicGFzc3dvcmQ' \
    'iLCJ1c2VyX2lkIjoiNDI1MTMwIiwidXNlcl9uYW1lIjoiTk9ERVRFU1RVU0VSIiwiZW1haWwiOi' \
    'JOb2RldGVzdEBzYXAuY29tIiwiZ2l2ZW5fbmFtZSI6Ik5vZGV0ZXN0Rmlyc3ROYW1lIiwiZmFta' \
    'Wx5X25hbWUiOiJOb2RldGVzdExhc3ROYW1lIiwiaWF0IjoxNDcwODE1NDM0LCJleHAiOjIxMDE1' \
    'MzU0MzQsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC91YWEvb2F1dGgvdG9rZW4iLCJ6aWQ' \
    'iOiJ0ZXN0LWlkeiIsImhkYi5uYW1lZHVzZXIuc2FtbCI6Ijw_eG1sIHZlcnNpb249XCIxLjBcIi' \
    'BlbmNvZGluZz1cIlVURi04XCI_PjxzYW1sMjpBc3NlcnRpb24geG1sbnM6c2FtbDI9XCJ1cm46b' \
    '2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YXNzZXJ0aW9uXCIgSUQ9XCJfNzFlZTE3NzYtOWQyZi00' \
    'OTczLWFjYTgtOWUyMmIyOTY3YWM4XCIgSXNzdWVJbnN0YW50PVwiMjAxNi0wOC0xMFQwNzo0NTo' \
    'zNC4zNDdaXCIgVmVyc2lvbj1cIjIuMFwiPjxzYW1sMjpJc3N1ZXI-VFNULXNhbWw8L3NhbWwyOk' \
    'lzc3Vlcj48ZHM6U2lnbmF0dXJlIHhtbG5zOmRzPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC8wO' \
    'S94bWxkc2lnI1wiPjxkczpTaWduZWRJbmZvPjxkczpDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFs' \
    'Z29yaXRobT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuI1wiLz48ZHM' \
    '6U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG' \
    '1sZHNpZyNyc2Etc2hhMVwiLz48ZHM6UmVmZXJlbmNlIFVSST1cIiNfNzFlZTE3NzYtOWQyZi00O' \
    'TczLWFjYTgtOWUyMmIyOTY3YWM4XCI-PGRzOlRyYW5zZm9ybXM-PGRzOlRyYW5zZm9ybSBBbGdv' \
    'cml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25' \
    'hdHVyZVwiLz48ZHM6VHJhbnNmb3JtIEFsZ29yaXRobT1cImh0dHA6Ly93d3cudzMub3JnLzIwMD' \
    'EvMTAveG1sLWV4Yy1jMTRuI1wiLz48L2RzOlRyYW5zZm9ybXM-PGRzOkRpZ2VzdE1ldGhvZCBBb' \
    'Gdvcml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMVwiLz48ZHM6' \
    'RGlnZXN0VmFsdWU-b3U4cjNSMFdCSEcxYnA0S0tPeDFQeVZPaVlBPTwvZHM6RGlnZXN0VmFsdWU' \
    '-PC9kczpSZWZlcmVuY2U-PC9kczpTaWduZWRJbmZvPjxkczpTaWduYXR1cmVWYWx1ZT5MYlJLdj' \
    'FyL2g3SU1taVN5eDEwV2tNN0p1ZWtybXd5Vk5zQjUzcGtGUm5yakNHV3RtRmtRc2tuc0w3ZVRVT' \
    'jQrZ2NKR1cwcUdUVW12VWtmWEUxTzhyZjJDbVRjQzAxY1lzR0FaV2JOcE9MTm1wUDlnRzY1NzJw' \
    'dmVScWpUWExHU2lsTTJlakppeWxxMkpuRkxoWHBncm5UYkN2UVc2YTlKVHBScHZNejhTaVNvZHh' \
    'heDdySnc3QzB5WnpVcTg2Mk01eU5qZG9JSGhFa25nTWNDNUxERGhmcGY2VGtRTXN5VmNNYW1EcW' \
    'pUUzdXVGd2a1FLbDVwa09QS0V1aFRqQ1I3UDdLQWVrZURtWW9xczd5RVpycmRLRWl4U1k0aTVGM' \
    '3dlTStkdytBMXVlOWpGMkttZVJ2am94czJod2ZzV3dVdkN4eSsySmhyNTR2YXRtd2VHOGRJMFE9' \
    'PTwvZHM6U2lnbmF0dXJlVmFsdWU-PC9kczpTaWduYXR1cmU-PHNhbWwyOlN1YmplY3Q-PHNhbWw' \
    'yOk5hbWVJRCBGb3JtYXQ9XCJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoxLjE6bmFtZWlkLWZvcm' \
    '1hdDp1bnNwZWNpZmllZFwiPk5PREVURVNUVVNFUjwvc2FtbDI6TmFtZUlEPjxzYW1sMjpTdWJqZ' \
    'WN0Q29uZmlybWF0aW9uIE1ldGhvZD1cInVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpjbTpi' \
    'ZWFyZXJcIj48c2FtbDI6U3ViamVjdENvbmZpcm1hdGlvbkRhdGEgTm90T25PckFmdGVyPVwiMjA' \
    'xNi0wOC0xMFQxMTo1MDozNC4zNDdaXCIvPjwvc2FtbDI6U3ViamVjdENvbmZpcm1hdGlvbj48L3' \
    'NhbWwyOlN1YmplY3Q-PHNhbWwyOkNvbmRpdGlvbnMgTm90QmVmb3JlPVwiMjAxNi0wOC0xMFQwN' \
    'zo0NTozNC4zNDdaXCIgTm90T25PckFmdGVyPVwiMjAxNi0wOC0xMFQxMTo1MDozNC4zNDdaXCIv' \
    'PjxzYW1sMjpBdXRoblN0YXRlbWVudCBBdXRobkluc3RhbnQ9XCIyMDE2LTA4LTEwVDA3OjUwOjM' \
    '0LjM0N1pcIiBTZXNzaW9uTm90T25PckFmdGVyPVwiMjAxNi0wOC0xMFQwNzo1NTozNC4zNDdaXC' \
    'I-PHNhbWwyOkF1dGhuQ29udGV4dD48c2FtbDI6QXV0aG5Db250ZXh0Q2xhc3NSZWY-dXJuOm9hc' \
    '2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFjOmNsYXNzZXM6UGFzc3dvcmQ8L3NhbWwyOkF1dGhuQ29u' \
    'dGV4dENsYXNzUmVmPjwvc2FtbDI6QXV0aG5Db250ZXh0Pjwvc2FtbDI6QXV0aG5TdGF0ZW1lbnQ' \
    '-PC9zYW1sMjpBc3NlcnRpb24-IiwiYXVkIjpbInNiLXhzc2VjdGVzdCIsIm9wZW5pZCJdfQ.' \
    'c1SyhbDOoqGUVljcVZwrZEw6W4XPF-gVkL5NZiKV_6Y'

CORRECT_END_USER_SAML_BEARER_TOKEN = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiJjNjgzMTEyNS0xZWQ2LTQxYjAtOG' \
    'VhOC1lNjBhMzQxYTI3ODciLCJzdWIiOiI0MjUxMzAiLCJzY29wZSI6WyJvcGVuaWQiXSwiY2xpZ' \
    'W50X2lkIjoic2IteHNzZWN0ZXN0IiwiY2lkIjoic2IteHNzZWN0ZXN0IiwiYXpwIjoic2IteHNz' \
    'ZWN0ZXN0IiwiZ3JhbnRfdHlwZSI6InVybjppZXRmOnBhcmFtczpvYXV0aDpncmFudC10eXBlOnN' \
    'hbWwyLWJlYXJlciIsInVzZXJfaWQiOiI0MjUxMzAiLCJ1c2VyX25hbWUiOiJOT0RFVEVTVFVTRV' \
    'IiLCJlbWFpbCI6Ik5vZGV0ZXN0QHNhcC5jb20iLCJnaXZlbl9uYW1lIjoiTm9kZXRlc3RGaXJzd' \
    'E5hbWUiLCJmYW1pbHlfbmFtZSI6Ik5vZGV0ZXN0TGFzdE5hbWUiLCJpYXQiOjE0NzA4MTU0MzQs' \
    'ImV4cCI6MjEwMTUzNTQzNCwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3VhYS9vYXV0aC9' \
    '0b2tlbiIsInppZCI6InRlc3QtaWR6IiwieHMudXNlci5hdHRyaWJ1dGVzIjp7fSwieHMuc3lzdG' \
    'VtLmF0dHJpYnV0ZXMiOnt9LCJhdWQiOlsic2IteHNzZWN0ZXN0Iiwib3BlbmlkIl19.' \
    '1Y8epau4mC_xEEEE3YF_9al_v9JfPoyHjPWKArdeEr8'

CORRECT_END_USER_APPLICATION_PLAN_TOKEN = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiJjNjgzMTEyNS0xZWQ2LTQxYjAtOG' \
    'VhOC1lNjBhMzQxYTI3ODciLCJzdWIiOiI0MjUxMzAiLCJzY29wZSI6WyJvcGVuaWQiLCJ1YWEuc' \
    'mVzb3VyY2UiXSwiY2xpZW50X2lkIjoic2IteHNzZWN0ZXN0IXQ0IiwiY2lkIjoic2IteHNzZWN0' \
    'ZXN0IXQ0IiwiYXpwIjoic2IteHNzZWN0ZXN0IiwiZ3JhbnRfdHlwZSI6InBhc3N3b3JkIiwidXN' \
    'lcl9pZCI6IjQyNTEzMCIsInVzZXJfbmFtZSI6Ik5PREVURVNUVVNFUiIsImVtYWlsIjoiTm9kZX' \
    'Rlc3RAc2FwLmNvbSIsImdpdmVuX25hbWUiOiJOb2RldGVzdEZpcnN0TmFtZSIsImZhbWlseV9uY' \
    'W1lIjoiTm9kZXRlc3RMYXN0TmFtZSIsImlhdCI6MTQ3MDgxNTQzNCwiZXhwIjoyMTAxNTM1NDM0' \
    'LCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvdWFhL29hdXRoL3Rva2VuIiwiemlkIjoidGV' \
    'zdC1pZHoiLCJoZGIubmFtZWR1c2VyLnNhbWwiOiI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2' \
    'Rpbmc9XCJVVEYtOFwiPz48c2FtbDI6QXNzZXJ0aW9uIHhtbG5zOnNhbWwyPVwidXJuOm9hc2lzO' \
    'm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvblwiIElEPVwiXzcxZWUxNzc2LTlkMmYtNDk3My1h' \
    'Y2E4LTllMjJiMjk2N2FjOFwiIElzc3VlSW5zdGFudD1cIjIwMTYtMDgtMTBUMDc6NDU6MzQuMzQ' \
    '3WlwiIFZlcnNpb249XCIyLjBcIj48c2FtbDI6SXNzdWVyPlRTVC1zYW1sPC9zYW1sMjpJc3N1ZX' \
    'I-PGRzOlNpZ25hdHVyZSB4bWxuczpkcz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZ' \
    'HNpZyNcIj48ZHM6U2lnbmVkSW5mbz48ZHM6Q2Fub25pY2FsaXphdGlvbk1ldGhvZCBBbGdvcml0' \
    'aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biNcIi8-PGRzOlNpZ25' \
    'hdHVyZU1ldGhvZCBBbGdvcml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaW' \
    'cjcnNhLXNoYTFcIi8-PGRzOlJlZmVyZW5jZSBVUkk9XCIjXzcxZWUxNzc2LTlkMmYtNDk3My1hY' \
    '2E4LTllMjJiMjk2N2FjOFwiPjxkczpUcmFuc2Zvcm1zPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGht' \
    'PVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI2VudmVsb3BlZC1zaWduYXR1cmV' \
    'cIi8-PGRzOlRyYW5zZm9ybSBBbGdvcml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3' \
    'htbC1leGMtYzE0biNcIi8-PC9kczpUcmFuc2Zvcm1zPjxkczpEaWdlc3RNZXRob2QgQWxnb3Jpd' \
    'GhtPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3NoYTFcIi8-PGRzOkRpZ2Vz' \
    'dFZhbHVlPm91OHIzUjBXQkhHMWJwNEtLT3gxUHlWT2lZQT08L2RzOkRpZ2VzdFZhbHVlPjwvZHM' \
    '6UmVmZXJlbmNlPjwvZHM6U2lnbmVkSW5mbz48ZHM6U2lnbmF0dXJlVmFsdWU-TGJSS3Yxci9oN0' \
    'lNbWlTeXgxMFdrTTdKdWVrcm13eVZOc0I1M3BrRlJucmpDR1d0bUZrUXNrbnNMN2VUVU40K2djS' \
    'kdXMHFHVFVtdlVrZlhFMU84cmYyQ21UY0MwMWNZc0dBWldiTnBPTE5tcFA5Z0c2NTcycHZlUnFq' \
    'VFhMR1NpbE0yZWpKaXlscTJKbkZMaFhwZ3JuVGJDdlFXNmE5SlRwUnB2TXo4U2lTb2R4YXg3ckp' \
    '3N0MweVp6VXE4NjJNNXlOamRvSUhoRWtuZ01jQzVMRERoZnBmNlRrUU1zeVZjTWFtRHFqVFM3V1' \
    'RndmtRS2w1cGtPUEtFdWhUakNSN1A3S0Fla2VEbVlvcXM3eUVacnJkS0VpeFNZNGk1RjN3ZU0rZ' \
    'HcrQTF1ZTlqRjJLbWVSdmpveHMyaHdmc1d3VXZDeHkrMkpocjU0dmF0bXdlRzhkSTBRPT08L2Rz' \
    'OlNpZ25hdHVyZVZhbHVlPjwvZHM6U2lnbmF0dXJlPjxzYW1sMjpTdWJqZWN0PjxzYW1sMjpOYW1' \
    'lSUQgRm9ybWF0PVwidXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6MS4xOm5hbWVpZC1mb3JtYXQ6dW' \
    '5zcGVjaWZpZWRcIj5OT0RFVEVTVFVTRVI8L3NhbWwyOk5hbWVJRD48c2FtbDI6U3ViamVjdENvb' \
    'mZpcm1hdGlvbiBNZXRob2Q9XCJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6Y206YmVhcmVy' \
    'XCI-PHNhbWwyOlN1YmplY3RDb25maXJtYXRpb25EYXRhIE5vdE9uT3JBZnRlcj1cIjIwMTYtMDg' \
    'tMTBUMTE6NTA6MzQuMzQ3WlwiLz48L3NhbWwyOlN1YmplY3RDb25maXJtYXRpb24-PC9zYW1sMj' \
    'pTdWJqZWN0PjxzYW1sMjpDb25kaXRpb25zIE5vdEJlZm9yZT1cIjIwMTYtMDgtMTBUMDc6NDU6M' \
    'zQuMzQ3WlwiIE5vdE9uT3JBZnRlcj1cIjIwMTYtMDgtMTBUMTE6NTA6MzQuMzQ3WlwiLz48c2Ft' \
    'bDI6QXV0aG5TdGF0ZW1lbnQgQXV0aG5JbnN0YW50PVwiMjAxNi0wOC0xMFQwNzo1MDozNC4zNDd' \
    'aXCIgU2Vzc2lvbk5vdE9uT3JBZnRlcj1cIjIwMTYtMDgtMTBUMDc6NTU6MzQuMzQ3WlwiPjxzYW' \
    '1sMjpBdXRobkNvbnRleHQ-PHNhbWwyOkF1dGhuQ29udGV4dENsYXNzUmVmPnVybjpvYXNpczpuY' \
    'W1lczp0YzpTQU1MOjIuMDphYzpjbGFzc2VzOlBhc3N3b3JkPC9zYW1sMjpBdXRobkNvbnRleHRD' \
    'bGFzc1JlZj48L3NhbWwyOkF1dGhuQ29udGV4dD48L3NhbWwyOkF1dGhuU3RhdGVtZW50Pjwvc2F' \
    'tbDI6QXNzZXJ0aW9uPiIsImF6X2F0dHIiOnsiZXh0ZXJuYWxfZ3JvdXAiOiJkb21haW5ncm91cD' \
    'EiLCJleHRlcm5hbF9pZCI6ImFiY2QxMjM0In0sImV4dF9hdHRyIjp7InNlcnZpY2VpbnN0YW5jZ' \
    'WlkIjoiYWJjZDEyMzQifSwieHMuc3lzdGVtLmF0dHJpYnV0ZXMiOnsieHMuc2FtbC5ncm91cHMi' \
    'OlsiQ2FuYXJ5X1JvbGVCdWlsZGVyIl0sInhzLnJvbGVjb2xsZWN0aW9ucyI6W119LCJ4cy51c2V' \
    'yLmF0dHJpYnV0ZXMiOnsiY291bnRyeSI6WyJVU0EiXX0sImF1ZCI6WyJzYi14c3NlY3Rlc3QiLC' \
    'JvcGVuaWQiXX0.NcOlYLFYb-a6mhCd85KckLYFOQ2uQXW8YWP1o1hRz1M'

INVALID_TRUSTED_APPLICATION_PLAN_TOKEN = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiJhM2I2NDNmODhlOTY0YmNhYjJmN2U5OTZkYjRiNTE4MyIsImV4dF9hdHRyIjp7ImVuaGFuY2VyIjoiWFNVQUEiLCJ6ZG4iOiJhcGkifSwic3ViIjoic2ItdGVuYW50LXRlc3QhdDEzIiwic2NvcGUiOlsiZG94LXVpLXBvYyFiNzg1Ny5DYWxsYmFjayJdLCJjbGllbnRfaWQiOiJzYi10ZW5hbnQtdGVzdCF0MTMiLCJjaWQiOiJzYi10ZW5hbnQtdGVzdCF0MTMiLCJhenAiOiJzYi10ZW5hbnQtdGVzdCF0MTMiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6ImYyYTFhOWQxIiwiaXNzIjoiaHR0cHM6Ly9hcGkuY2YudGVzdC5jb20vdWFhL29hdXRoL3Rva2VuIiwiemlkIjoiYXBpIiwiYXVkIjpbImRveC11aS1wb2MhYjc4NTciLCJzYi10ZW5hbnQtdGVzdCF0MTMiXX0.EVuclqGbDSWVFPHGjLUOgkViBQHVYVjEl51SX00JBuM'

INVALID_SIGNATURE_END_USER_TOKEN = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiJjNjgzMTEyNS0xZWQ2LTQxYjAtOG' \
    'VhOC1lNjBhMzQxYTI3ODciLCJzdWIiOiI0MjUxMzAiLCJzY29wZSI6WyJvcGVuaWQiLCJ1YWEuc' \
    'mVzb3VyY2UiXSwiY2xpZW50X2lkIjoic2IteHNzZWN0ZXN0IiwiY2lkIjoic2IteHNzZWN0ZXN0' \
    'IiwiYXpwIjoic2IteHNzZWN0ZXN0IiwiZ3JhbnRfdHlwZSI6InBhc3N3b3JkIiwidXNlcl9pZCI' \
    '6IjQyNTEzMCIsInVzZXJfbmFtZSI6Ik5PREVURVNUVVNFUiIsImVtYWlsIjoiTm9kZXRlc3RAc2' \
    'FwLmNvbSIsImdpdmVuX25hbWUiOiJOb2RldGVzdEZpcnN0TmFtZSIsImZhbWlseV9uYW1lIjoiT' \
    'm9kZXRlc3RMYXN0TmFtZSIsImlhdCI6MTQ3MDgxNTQzNCwiZXhwIjoyMTAxNTM1NDM0LCJpc3Mi' \
    'OiJodHRwOi8vbG9jYWxob3N0OjgwODAvdWFhL29hdXRoL3Rva2VuIiwiemlkIjoidGVzdC1pZHo' \
    'iLCJoZGIubmFtZWR1c2VyLnNhbWwiOiI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XC' \
    'JVVEYtOFwiPz48c2FtbDI6QXNzZXJ0aW9uIHhtbG5zOnNhbWwyPVwidXJuOm9hc2lzOm5hbWVzO' \
    'nRjOlNBTUw6Mi4wOmFzc2VydGlvblwiIElEPVwiXzcxZWUxNzc2LTlkMmYtNDk3My1hY2E4LTll' \
    'MjJiMjk2N2FjOFwiIElzc3VlSW5zdGFudD1cIjIwMTYtMDgtMTBUMDc6NDU6MzQuMzQ3WlwiIFZ' \
    'lcnNpb249XCIyLjBcIj48c2FtbDI6SXNzdWVyPlRTVC1zYW1sPC9zYW1sMjpJc3N1ZXI-PGRzOl' \
    'NpZ25hdHVyZSB4bWxuczpkcz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyNcI' \
    'j48ZHM6U2lnbmVkSW5mbz48ZHM6Q2Fub25pY2FsaXphdGlvbk1ldGhvZCBBbGdvcml0aG09XCJo' \
    'dHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biNcIi8-PGRzOlNpZ25hdHVyZU1' \
    'ldGhvZCBBbGdvcml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjcnNhLX' \
    'NoYTFcIi8-PGRzOlJlZmVyZW5jZSBVUkk9XCIjXzcxZWUxNzc2LTlkMmYtNDk3My1hY2E4LTllM' \
    'jJiMjk2N2FjOFwiPjxkczpUcmFuc2Zvcm1zPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPVwiaHR0' \
    'cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI2VudmVsb3BlZC1zaWduYXR1cmVcIi8-PGR' \
    'zOlRyYW5zZm9ybSBBbGdvcml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leG' \
    'MtYzE0biNcIi8-PC9kczpUcmFuc2Zvcm1zPjxkczpEaWdlc3RNZXRob2QgQWxnb3JpdGhtPVwia' \
    'HR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3NoYTFcIi8-PGRzOkRpZ2VzdFZhbHVl' \
    'Pm91OHIzUjBXQkhHMWJwNEtLT3gxUHlWT2lZQT08L2RzOkRpZ2VzdFZhbHVlPjwvZHM6UmVmZXJ' \
    'lbmNlPjwvZHM6U2lnbmVkSW5mbz48ZHM6U2lnbmF0dXJlVmFsdWU-TGJSS3Yxci9oN0lNbWlTeX' \
    'gxMFdrTTdKdWVrcm13eVZOc0I1M3BrRlJucmpDR1d0bUZrUXNrbnNMN2VUVU40K2djSkdXMHFHV' \
    'FVtdlVrZlhFMU84cmYyQ21UY0MwMWNZc0dBWldiTnBPTE5tcFA5Z0c2NTcycHZlUnFqVFhMR1Np' \
    'bE0yZWpKaXlscTJKbkZMaFhwZ3JuVGJDdlFXNmE5SlRwUnB2TXo4U2lTb2R4YXg3ckp3N0MweVp' \
    '6VXE4NjJNNXlOamRvSUhoRWtuZ01jQzVMRERoZnBmNlRrUU1zeVZjTWFtRHFqVFM3V1RndmtRS2' \
    'w1cGtPUEtFdWhUakNSN1A3S0Fla2VEbVlvcXM3eUVacnJkS0VpeFNZNGk1RjN3ZU0rZHcrQTF1Z' \
    'TlqRjJLbWVSdmpveHMyaHdmc1d3VXZDeHkrMkpocjU0dmF0bXdlRzhkSTBRPT08L2RzOlNpZ25h' \
    'dHVyZVZhbHVlPjwvZHM6U2lnbmF0dXJlPjxzYW1sMjpTdWJqZWN0PjxzYW1sMjpOYW1lSUQgRm9' \
    'ybWF0PVwidXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6MS4xOm5hbWVpZC1mb3JtYXQ6dW5zcGVjaW' \
    'ZpZWRcIj5OT0RFVEVTVFVTRVI8L3NhbWwyOk5hbWVJRD48c2FtbDI6U3ViamVjdENvbmZpcm1hd' \
    'GlvbiBNZXRob2Q9XCJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6Y206YmVhcmVyXCI-PHNh' \
    'bWwyOlN1YmplY3RDb25maXJtYXRpb25EYXRhIE5vdE9uT3JBZnRlcj1cIjIwMTYtMDgtMTBUMTE' \
    '6NTA6MzQuMzQ3WlwiLz48L3NhbWwyOlN1YmplY3RDb25maXJtYXRpb24-PC9zYW1sMjpTdWJqZW' \
    'N0PjxzYW1sMjpDb25kaXRpb25zIE5vdEJlZm9yZT1cIjIwMTYtMDgtMTBUMDc6NDU6MzQuMzQ3W' \
    'lwiIE5vdE9uT3JBZnRlcj1cIjIwMTYtMDgtMTBUMTE6NTA6MzQuMzQ3WlwiLz48c2FtbDI6QXV0' \
    'aG5TdGF0ZW1lbnQgQXV0aG5JbnN0YW50PVwiMjAxNi0wOC0xMFQwNzo1MDozNC4zNDdaXCIgU2V' \
    'zc2lvbk5vdE9uT3JBZnRlcj1cIjIwMTYtMDgtMTBUMDc6NTU6MzQuMzQ3WlwiPjxzYW1sMjpBdX' \
    'RobkNvbnRleHQ-PHNhbWwyOkF1dGhuQ29udGV4dENsYXNzUmVmPnVybjpvYXNpczpuYW1lczp0Y' \
    'zpTQU1MOjIuMDphYzpjbGFzc2VzOlBhc3N3b3JkPC9zYW1sMjpBdXRobkNvbnRleHRDbGFzc1Jl' \
    'Zj48L3NhbWwyOkF1dGhuQ29udGV4dD48L3NhbWwyOkF1dGhuU3RhdGVtZW50Pjwvc2FtbDI6QXN' \
    'zZXJ0aW9uPiIsImF6X2F0dHIiOnsiZXh0ZXJuYWxfZ3JvdXAiOiJkb21haW5ncm91cDEiLCJleH' \
    'Rlcm5hbF9pZCI6ImFiY2QxMjM0In0sImV4dF9hdHRyIjp7InNlcnZpY2VpbnN0YW5jZWlkIjoiY' \
    'WJjZDEyMzQifSwieHMuc3lzdGVtLmF0dHJpYnV0ZXMiOnsieHMuc2FtbC5ncm91cHMiOlsiQ2Fu' \
    'YXJ5X1JvbGVCdWlsZGVyIl0sInhzLnJvbGVjb2xsZWN0aW9ucyI6W119LCJ4cy51c2VyLmF0dHJ' \
    'pYnV0ZXMiOnsiY291bnRyeSI6WyJVU0EiXX0sImF1ZCI6WyJzYi14c3NlY3Rlc3QiLCJvcGVuaW' \
    'QiXX0.0H90i_3lOxk0K3Qvty3LDgCItI1IMXS0sBy5Dpi7ryU'

CORRECT_CLIENT_CREDENTIALS_TOKEN = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiIyODRhMjY1YS04ZWY1LTRiNzAtOTI1ZC1hYzA' \
    '2MTI3M2ViMjEiLCJzdWIiOiJzYi14c3NlY3Rlc3QiLCJhdXRob3JpdGllcyI6WyJ1YWEucmVzb3' \
    'VyY2UiXSwic2NvcGUiOlsidWFhLnJlc291cmNlIl0sImNsaWVudF9pZCI6InNiLXhzc2VjdGVzd' \
    'CIsImNpZCI6InNiLXhzc2VjdGVzdCIsImF6cCI6InNiLXhzc2VjdGVzdCIsImdyYW50X3R5cGUi' \
    'OiJjbGllbnRfY3JlZGVudGlhbHMiLCJpYXQiOjE0NzA4MTQ0ODIsImV4cCI6MjEwMTUzNDQ4Miw' \
    'iaXNzIjoiaHR0cDovL3NhYXMubG9jYWxob3N0OjgwODAvdWFhL29hdXRoL3Rva2VuIiwiemlkIj' \
    'oidGVzdC1pZHoiLCJhdWQiOlsic2IteHNzZWN0ZXN0IiwidWFhIl0sImF6X2F0dHIiOnsiZXh0Z' \
    'XJuYWxfZ3JvdXAiOiJkb21haW5ncm91cDEiLCJleHRlcm5hbF9pZCI6ImFiY2QxMjM0In0sImV4' \
    'dF9hdHRyIjp7InNlcnZpY2VpbnN0YW5jZWlkIjoiYWJjZDEyMzQiLCJ6ZG4iOiJzYWFzIn0sInh' \
    'zLnN5c3RlbS5hdHRyaWJ1dGVzIjp7InhzLnNhbWwuZ3JvdXBzIjpbIkNhbmFyeV9Sb2xlQnVpbG' \
    'RlciJdLCJ4cy5yb2xlY29sbGVjdGlvbnMiOltdfSwieHMudXNlci5hdHRyaWJ1dGVzIjp7ImNvd' \
    'W50cnkiOlsiVVNBIl19fQ.7VsLxcsqPCG7SpYBO6SwtU2Br58BK_TnKMnq0SeX-Qg'

CORRECT_CLIENT_CREDENTIALS_TOKEN_NO_ATTR = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiIyODRhMjY1YS04ZWY1LTRiNzAtOTI1ZC1hYzA' \
    '2MTI3M2ViMjEiLCJzdWIiOiJzYi14c3NlY3Rlc3QiLCJhdXRob3JpdGllcyI6WyJ1YWEucmVzb3' \
    'VyY2UiXSwic2NvcGUiOlsidWFhLnJlc291cmNlIl0sImV4dF9hdHRyIjp7InpkbiI6InNhYXMif' \
    'SwiY2xpZW50X2lkIjoic2IteHNzZWN0ZXN0IiwiY2lkIjoic2IteHNzZWN0ZXN0IiwiYXpwIjoi' \
    'c2IteHNzZWN0ZXN0IiwiZ3JhbnRfdHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTQ' \
    '3MDgxNDQ4MiwiZXhwIjoyMTAxNTM0NDgyLCJpc3MiOiJodHRwOi8vc2Fhcy5sb2NhbGhvc3Q6OD' \
    'A4MC91YWEvb2F1dGgvdG9rZW4iLCJ6aWQiOiJ0ZXN0LWlkeiIsImF1ZCI6WyJzYi14c3NlY3Rlc' \
    '3QiLCJ1YWEiXX0.lFcpIgsgCfn-8Q58X2zvAMFe2u9iJaLnrH61shnIBzI'

CORRECT_CLIENT_CREDENTIALS_BROKER_PLAN_TOKEN = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiIyODRhMjY1YS04ZWY1LTRiNzAtOT' \
    'I1ZC1hYzA2MTI3M2ViMjEiLCJzdWIiOiJzYi14c3NlY3Rlc3QiLCJhdXRob3JpdGllcyI6WyJ1Y' \
    'WEucmVzb3VyY2UiXSwic2NvcGUiOlsidWFhLnJlc291cmNlIl0sImNsaWVudF9pZCI6InNiLXhz' \
    'c2VjdGVzdGNsb25lIWI0fHNiLXhzc2VjdGVzdCFiNCIsImNpZCI6InNiLXhzc2VjdGVzdGNsb25' \
    'lIWI0fHNiLXhzc2VjdGVzdCFiNCIsImF6cCI6InNiLXhzc2VjdGVzdCIsImdyYW50X3R5cGUiOi' \
    'JjbGllbnRfY3JlZGVudGlhbHMiLCJpYXQiOjE0NzA4MTQ0ODIsImV4cCI6MjEwMTUzNDQ4Miwia' \
    'XNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3VhYS9vYXV0aC90b2tlbiIsInppZCI6InRlc3Qt' \
    'aWR6IiwiYXVkIjpbInNiLXhzc2VjdGVzdCIsInVhYSJdLCJhel9hdHRyIjp7ImV4dGVybmFsX2d' \
    'yb3VwIjoiZG9tYWluZ3JvdXAxIiwiZXh0ZXJuYWxfaWQiOiJhYmNkMTIzNCJ9LCJleHRfYXR0ci' \
    'I6eyJzZXJ2aWNlaW5zdGFuY2VpZCI6ImFiY2QxMjM0In0sInhzLnN5c3RlbS5hdHRyaWJ1dGVzI' \
    'jp7InhzLnNhbWwuZ3JvdXBzIjpbIkNhbmFyeV9Sb2xlQnVpbGRlciJdLCJ4cy5yb2xlY29sbGVj' \
    'dGlvbnMiOltdfSwieHMudXNlci5hdHRyaWJ1dGVzIjp7ImNvdW50cnkiOlsiVVNBIl19fQ.' \
    'c42cXfVCP-iV57fVi3rJ-YAS-EvquvGe3ntv-kLeCCc'

TOKEN_NEW_FORMAT = \
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImprdSI6Imh0dHBzOi8vYXBpLmNmLnRlc3QuY29' \
    'tIiwia2lkIjoia2V5LWlkLTAifQ.eyJqdGkiOiI2YzAwNzJmZDAxZmI0NDBiODZmOG' \
    'EyM2JmOTE2MTJiNC1yIiwic3ViIjoiYjU2MDdjMWUtNTQ5NC00YmYzLTgzMDUtZGUzNTM1N2UwM' \
    'DIxIiwic2NvcGUiOlsib3BlbmlkIl0sImV4dF9hdHRyIjp7ImVuaGFuY2VyIjoiWFNVQUEiLCJn' \
    'aXZlbl9uYW1lIjoibWljaGkiLCJmYW1pbHlfbmFtZSI6ImVuZ2xlciIsInNlcnZpY2VpbnN0YW5' \
    'jZWlkIjoicmV1c2Utc2VydmljZS1wYWFzLWxyLWNsb25lMi1pbnN0YW5jZWlkIn0sImV4dF9jeH' \
    'QiOnsiaGRiLm5hbWVkdXNlci5zYW1sIjoiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nP' \
    'VwiVVRGLThcIj8-PHNhbWwyOkFzc2VydGlvbiB4bWxuczpzYW1sMj1cInVybjpvYXNpczpuYW1l' \
    'czp0YzpTQU1MOjIuMDphc3NlcnRpb25cIiBJRD1cIl8xZGM4ZDdjZC1lYWM4LTRhNjctYmZhNC0' \
    '3NmNhNWVkZTJlNTJcIiBJc3N1ZUluc3RhbnQ9XCIyMDE3LTExLTE2VDExOjA2OjQwLjMyNVpcIi' \
    'BWZXJzaW9uPVwiMi4wXCIgeG1sbnM6eHM9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNja' \
    'GVtYVwiPjxzYW1sMjpJc3N1ZXI-bG9jYWwtaWRwPC9zYW1sMjpJc3N1ZXI-PGRzOlNpZ25hdHVy' \
    'ZSB4bWxuczpkcz1cImh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyNcIj48ZHM6U2l' \
    'nbmVkSW5mbz48ZHM6Q2Fub25pY2FsaXphdGlvbk1ldGhvZCBBbGdvcml0aG09XCJodHRwOi8vd3' \
    'd3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biNcIi8-PGRzOlNpZ25hdHVyZU1ldGhvZCBBb' \
    'Gdvcml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjcnNhLXNoYTFcIi8-' \
    'PGRzOlJlZmVyZW5jZSBVUkk9XCIjXzFkYzhkN2NkLWVhYzgtNGE2Ny1iZmE0LTc2Y2E1ZWRlMmU' \
    '1MlwiPjxkczpUcmFuc2Zvcm1zPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPVwiaHR0cDovL3d3dy' \
    '53My5vcmcvMjAwMC8wOS94bWxkc2lnI2VudmVsb3BlZC1zaWduYXR1cmVcIi8-PGRzOlRyYW5zZ' \
    'm9ybSBBbGdvcml0aG09XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biNc' \
    'Ij48ZWM6SW5jbHVzaXZlTmFtZXNwYWNlcyB4bWxuczplYz1cImh0dHA6Ly93d3cudzMub3JnLzI' \
    'wMDEvMTAveG1sLWV4Yy1jMTRuI1wiIFByZWZpeExpc3Q9XCJ4c1wiLz48L2RzOlRyYW5zZm9ybT' \
    '48L2RzOlRyYW5zZm9ybXM-PGRzOkRpZ2VzdE1ldGhvZCBBbGdvcml0aG09XCJodHRwOi8vd3d3L' \
    'nczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMVwiLz48ZHM6RGlnZXN0VmFsdWU-K1kxR1lmbXFT' \
    'NUpQVklWWFFTV0J4NSsrNmVjPTwvZHM6RGlnZXN0VmFsdWU-PC9kczpSZWZlcmVuY2U-PC9kczp' \
    'TaWduZWRJbmZvPjxkczpTaWduYXR1cmVWYWx1ZT5kR2xtNFF3Vkd6K056STl1ZktkYXY2YkRvVj' \
    'ZCTFUrRU9FUVhaR1JicHNyK0t5ek1qTkdjdXRxM0RjbW9oOUtPayt3eHFFMHVXd3lwUWZkMVlMV' \
    'jBmMkx1UUFGbzV6TkgwdXF4c3F0a3E0WWhQTnZ0MHE4NXZ1cGEvRmFjeUJJakpzS1hUbmgwT3JN' \
    'UzdhRHUvajRUazRKN2JrOTY0L0I0ZnpWbGFuUHhCdWxoL2FsY0EzRm5EcEFPZVN3bHI5aVRxajI' \
    'ybDlMU0h1Z2xGN3dGaGZjWkNUK2VtVWJKUjlSTDl1eTRES3pJK3BNL3E4YmxQZm1pcnJXV0t0aU' \
    'VGc3F4Z1JXRmpKVE1NOXZ3Rm9kVWxaQm54b1FZcVJIYVczTmZzbndjbCs2NDJsU3hNeVJBY2tiW' \
    'WxPMkRYTDhRc0paeE9BWEM4N01ya2g0bHRwaHRrd1ltREE9PTwvZHM6U2lnbmF0dXJlVmFsdWU-' \
    'PC9kczpTaWduYXR1cmU-PHNhbWwyOlN1YmplY3Q-PHNhbWwyOk5hbWVJRCBGb3JtYXQ9XCJ1cm4' \
    '6b2FzaXM6bmFtZXM6dGM6U0FNTDoxLjE6bmFtZWlkLWZvcm1hdDp1bnNwZWNpZmllZFwiPlRlc3' \
    'RVc2VyPC9zYW1sMjpOYW1lSUQ-PHNhbWwyOlN1YmplY3RDb25maXJtYXRpb24gTWV0aG9kPVwid' \
    'XJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmNtOmJlYXJlclwiPjxzYW1sMjpTdWJqZWN0Q29u' \
    'ZmlybWF0aW9uRGF0YSBOb3RPbk9yQWZ0ZXI9XCIyMDE3LTExLTE2VDE1OjExOjQwLjMyNVpcIi8' \
    '-PC9zYW1sMjpTdWJqZWN0Q29uZmlybWF0aW9uPjwvc2FtbDI6U3ViamVjdD48c2FtbDI6Q29uZG' \
    'l0aW9ucyBOb3RCZWZvcmU9XCIyMDE3LTExLTE2VDExOjA2OjQwLjMyNVpcIiBOb3RPbk9yQWZ0Z' \
    'XI9XCIyMDE3LTExLTE2VDE1OjExOjQwLjMyNVpcIi8-PHNhbWwyOkF0dHJpYnV0ZVN0YXRlbWVu' \
    'dD48c2FtbDI6QXR0cmlidXRlIE5hbWU9XCJhY3JcIj48c2FtbDI6QXR0cmlidXRlVmFsdWUgeG1' \
    'sbnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB4c2' \
    'k6dHlwZT1cInhzOnN0cmluZ1wiPnVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphYzpjbGFzc' \
    '2VzOlBhc3N3b3JkPC9zYW1sMjpBdHRyaWJ1dGVWYWx1ZT48L3NhbWwyOkF0dHJpYnV0ZT48c2Ft' \
    'bDI6QXR0cmlidXRlIE5hbWU9XCJHcm91cHNcIj48c2FtbDI6QXR0cmlidXRlVmFsdWUgeG1sbnM' \
    '6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB4c2k6dH' \
    'lwZT1cInhzOnN0cmluZ1wiPmcxPC9zYW1sMjpBdHRyaWJ1dGVWYWx1ZT48L3NhbWwyOkF0dHJpY' \
    'nV0ZT48L3NhbWwyOkF0dHJpYnV0ZVN0YXRlbWVudD48c2FtbDI6QXV0aG5TdGF0ZW1lbnQgQXV0' \
    'aG5JbnN0YW50PVwiMjAxNy0xMS0xNlQxMToxMTo0MC4zMjZaXCIgU2Vzc2lvbk5vdE9uT3JBZnR' \
    'lcj1cIjIwMTctMTEtMTZUMTE6MTY6NDAuMzI2WlwiPjxzYW1sMjpBdXRobkNvbnRleHQ-PHNhbW' \
    'wyOkF1dGhuQ29udGV4dENsYXNzUmVmPnVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphYzpjb' \
    'GFzc2VzOlBhc3N3b3JkPC9zYW1sMjpBdXRobkNvbnRleHRDbGFzc1JlZj48L3NhbWwyOkF1dGhu' \
    'Q29udGV4dD48L3NhbWwyOkF1dGhuU3RhdGVtZW50Pjwvc2FtbDI6QXNzZXJ0aW9uPiIsInhzLnV' \
    'zZXIuYXR0cmlidXRlcyI6eyJjb3VudHJ5IjpbImRlIl19LCJ4cy5zeXN0ZW0uYXR0cmlidXRlcy' \
    'I6eyJ4cy5zYW1sLmdyb3VwcyI6WyJnMSJdLCJ4cy5yb2xlY29sbGVjdGlvbnMiOltdfX0sImlhd' \
    'CI6MTUxMDgzMDcxNywiZXhwIjoyMTc3MzY2NDAwLCJjaWQiOiJzYi1jbG9uZTIhYjF8TFItbWFz' \
    'dGVyIWIxIiwiY2xpZW50X2lkIjoic2ItY2xvbmUyIWIxfExSLW1hc3RlciFiMSIsImlzcyI6Imh' \
    '0dHA6Ly9wYWFzLmxvY2FsaG9zdDo4MDgwL3VhYS9vYXV0aC90b2tlbiIsInppZCI6InBhYXMiLC' \
    'JyZXZvY2FibGUiOnRydWUsImdyYW50X3R5cGUiOiJ1c2VyX3Rva2VuIiwidXNlcl9uYW1lIjoiV' \
    'GVzdFVzZXIiLCJvcmlnaW4iOiJ1c2VyaWRwIiwidXNlcl9pZCI6ImI1NjA3YzFlLTU0OTQtNGJm' \
    'My04MzA1LWRlMzUzNTdlMDAyMSIsInJldl9zaWciOiJmMmI4YWRlOCIsImF1ZCI6W119.' \
    '62ebaE4eJDTK4UYirluOXwj1mM_P9AP6hPcekSkPyTU'

TOKEN_XSA_FORMAT = \
    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJIREIwMCIsIm5hbWUiOiJTWVNURU' \
    '0iLCJjaWQiOiJzYi14c3NlY3Rlc3QiLCJ6aWQiOiJ1YWEiLCJhZG1pbiI6dHJ1ZSwiYXV0aG9yaX' \
    'RpZXMiOlsidWFhLnJlc291cmNlIl0sInNjb3BlIjpbInVhYS51c2VyIiwib3BlbmlkIiwidWFhLn' \
    'Jlc291cmNlIl0sInVzZXJfbmFtZSI6IkFETUlOIn0.FuOJCAKe94bOI0r4YdNAAL89rexX6KwDKD' \
    'qwfwklsB27-9iFVdilncsyc7au8Hwg_2KB5Bq9mijASHY5OVgu5bVWODa7l8EQIdETBRfREpWZMv' \
    '4cX45X3D7ueGviCmrYScnuL3d6QXr1JZp-g1N8RCOKn1PkiP4Bk_WIsoVPM1wrPbZsHcm6FT1LOz' \
    'O1JswQFtqV7r1oK5B8zLONgZ8cquubDaoK7OmSh2iKFxGrRJ7clMO5GtTe18L93KKNdp7FWU4yWR' \
    'xvwXfxjtEvIOw4-Kom2KuUbl84rwLQieW_bNiwdlLPgUg4ohODT2mPK5mS6VDNYjGctIUkivThmk' \
    'YoVQ'
