from ckan.common import config
from six import text_type


def get_gtm_code():
    # To get Google Tag Manager Code
    gtm_code = config.get('ckan.google_tag_manager.gtm_container_id', False)
    return text_type(gtm_code)
