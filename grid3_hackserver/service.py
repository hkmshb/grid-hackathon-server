import os
from .client import OGCServiceType, GeoServerAPIClient


# simple in-memory registry for created services
_SERVICES = []


def resource(name=None, **kwargs):
    """Class decorator to declare resource endpoints.

    Sample usage:

        @resource('schools', layer_name='sv_fc_poi_school')
    """
    def wrapper(cls):
        kwargs.setdefault('name', name)
        return add_resource(cls, **kwargs)
    return wrapper


def add_resource(cls, **kwargs):
    """Function to create a service for a resource endpoint.
    """
    service_name = kwargs.pop('name', None)
    if not service_name:
        service_name = cls.__name__.lower().replace('resource', '')

    service = Service(name=service_name, **kwargs)
    setattr(cls, '_service', service)
    return cls


def clear_services():
    """Clears in-memory registered services.
    """
    _SERVICES[:] = []


def get_services(names=None):
    """Returns a list of registered services.

    Limits returned services to those named otherwise all registered services
    are returned.
    """
    def _skip(service):
        return names is not None and service.name not in names
    
    return [service for service in _SERVICES if not _skip(service)]


class Service:
    """Contains an API endpoint definition.

    A service is composed of GeoServer specifics for accessing a layer and
    possibly the fields exposed therein.
    """

    def __init__(self, name, layer_name, workspace='GRIDMaster',
                 service_type=OGCServiceType.WFS):
        """Initializes a new instance of the Service object.

        :param name: endpoint name for the service.
        :param layer_name: name of the layer on GeoServer.
        :param workspace: GeoServer workspace containing layer.
        :param service_type: The OGC service to interact over for the specified
            layer.
        """
        self.name = name
        self.layer_name = layer_name
        self.workspace = workspace
        self.service_type = service_type

        # add this to list of available servides
        _SERVICES.append(self)

    def get_apiclient(self):
        propkey = '_gs_apiclient'
        if not hasattr(self.__class__, propkey):
            client = GeoServerAPIClient(
                urlbase= os.getenv('G3H_GEOSERVER_URLBASE'),
                apikey=os.getenv('G3H_GEOSERVER_AUTHKEY')
            )
            setattr(self.__class__, propkey, client)
        return getattr(self.__class__, propkey)

    def __call__(self, **query_params):
        urlpath = 'geoserver/{workspace}/ows'.format(workspace=self.workspace)
        query_params.update({
            'typeName': '{workspace}:{layer_name}'.format(
                workspace=self.workspace, layer_name=self.layer_name
            )
        })
        
        client = self.get_apiclient()
        return client(urlpath, query_params)
