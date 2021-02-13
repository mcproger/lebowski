import os

SESSION_URL = 'https://www.tinkoff.ru/api/common/v1/session?origin=web%2Cib5%2Cplatform'
SIGN_UP_URL = (
    'https://www.tinkoff.ru/api/common/v1/sign_up?'
    'origin=web%2Cib5%2Cplatform&sessionid={session_id}&wuid=af3b1c996a3e2678fb05a25fab603e17'
)
LEVEL_UP_URL = (
    'https://www.tinkoff.ru/api/common/v1/level_up'
    '?wuid=af3b1c996a3e2678fb05a25fab603e17&origin=web%2Cib5%2Cplatform&sessionid={signed_up_session_id}'
)
OPERATIONS_PIECHART_URL = (
    # NOTE convert end to current month end
    'https://www.tinkoff.ru/api/common/v1/operations_piechart?end={to_timestamp}&'
    'groupBy=spendingCategory&notInner=true&start={from_timestamp}&type=Debit'
    '&sessionid={signed_up_session_id}&wuid=af3b1c996a3e2678fb05a25fab603e17'
)


CANDIDATE_ACCESS_LEVEL_MARKER = 'CANDIDATE'
CLIENT_ACCESS_LEVEL_MARKER = 'CLIENT'

FINGERPRINT = os.getenv('BROWSER_FINGERPRINT', '')
SIGN_UP_FORM_PAYLOAD = {
    'wuid': os.getenv('WUID', ''),
    'entrypoint_type': 'context',
    'fingerprint': FINGERPRINT,
    'fingerprint_gpu_shading_language_version': 'WebGL+GLSL+ES+1.0+%28OpenGL+ES+GLSL+ES+1.0+Chromium%29',
    'fingerprint_gpu_vendor': 'WebKit',
    'fingerprint_gpu_extensions_hash': os.getenv('FINGERPRINT_GPU_EXTENSIONS_HASH', ''),
    'fingerprint_gpu_extensions_count': '31',
    'fingerprint_device_platform': 'MacIntel',
    'fingerprint_client_timezone': '-180',
    'fingerprint_client_language': 'en-GB',
    'fingerprint_canvas': os.getenv('FINGERPRINT_CANVAS', ''),
    'fingerprint_accept_language': 'en-GB%2Cen-US%2Cen%2Cru',
    'mid': os.getenv('MID', ''),
    'device_type': 'desktop',
    'form_view_mode': 'desktop',
    'password': os.getenv('TINKOFF_PASSWORD', ''),
}
