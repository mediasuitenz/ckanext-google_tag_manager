import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.google_tag_manager import helpers

class Google_Tag_ManagerPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, '../templates')
        toolkit.add_public_directory(config_, '../public')
        toolkit.add_resource('fanstatic', 'google_tag_manager')

    def get_helpers(self):
        return {'get_gtm_container_id' : helpers.get_gtm_code}
