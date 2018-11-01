import enum


# simple in-memory registry for created services
_SERVICES = []


def clear_services():
    _SERVICES[:] = []


def get_services(names=None):
    def _skip(service):
        return names is not None and service.name not in names
    
    return [service for service in _SERVICES if not _skip(service)]


class OGCServiceType(enum.Enum):
    """Defines the subset of OGC service types that are proxied from GeoServer.
    """
    WFS = 'Web Features Service'
    WMS = 'Web Map Service'


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
