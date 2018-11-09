from .service import resource, model


@model("""School:
            type: object
            properties:
                state_code:
                    type: string
                state_name:
                    type: string
                ward_code:
                    type: string""",
       """{
           "type":"Feature",
           "id":"sv_fc_poi_school.fid--587d98af_166e9e2bbdd_-1774",
           "geometry":{"type":"Point","coordinates":[7.341849000000025,5.118416000000026]},
           "geometry_name":"geom",
           "properties":{
               "geometry_type":"POINT",
               "latitude":5.118416000000025,
               "longitude":7.341849000000025,
               "global_id":"cb649267-9250-43d0-8773-a89fb9b96969",
               "name":"Infantary Batalion Primary School II",
               "category":"Primary",
               "sub_type":"Standard",
               "management":"Public",
               "education":"Formal",
               "poi_type":"School",
               "number_of_teachers":null,
               "number_of_students":null,
               "ward_code":"ABSEZA01",
               "ward_name":"Ariaria",
               "lga_code":"1001",
               "lga_name":"Aba North",
               "state_code":"AB",
               "state_name":"Abia"
            }
           }""")
@resource('schools', layer_name='sv_fc_poi_school')
class SchoolResource:
    pass


@resource('health-facilities', layer_name='sv_fc_poi_health_facilities')
class HealthFacilityResource:
    pass


@resource('boundary-states', layer_name='sv_boundary_states')
class BoundaryStatesResource:
    pass
