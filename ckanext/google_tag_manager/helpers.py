from ckan.common import config
from builtins import str

def get_gtm_code():
    # To get Google Tag Manager Code
    gtm_code = config.get('ckan.google_tag_manager.gtm_container_id', False)
    return str(gtm_code)
