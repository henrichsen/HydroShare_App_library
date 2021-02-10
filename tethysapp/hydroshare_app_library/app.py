from tethys_sdk.base import TethysAppBase, url_map_maker


class HydroshareAppLibrary(TethysAppBase):
    """
    Tethys app class for HydroShare App Library.
    """

    name = 'HydroShare App Library'
    index = 'hydroshare_app_library:home'
    icon = 'hydroshare_app_library/images/icon.gif'
    package = 'hydroshare_app_library'
    root_url = 'hydroshare-app-library'
    color = '#AFD487'
    description = 'This is the Hydroshare app library. This page acts as a landing page for all Hydroshare webapp resources. The app is divided into three tables: CUAHSI apps, Community apps, and My apps. '
    tags = '"HydroShare","App Library", "Web Resources","CUAHSI","Development"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hydroshare-app-library',
                controller='hydroshare_app_library.controllers.home'
            ),
        )

        return url_maps