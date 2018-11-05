from .service import resource


@resource('schools', layer_name='sv_fc_poi_school')
class SchoolResource:
    pass


@resource('health-facilities', layer_name='sv_fc_poi_health_facilities')
class HealthFacilityResource:
    pass


@resource('boundary-states', layer_name='sv_boundary_states')
class BoundaryStatesResource:
    pass