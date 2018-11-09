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


@resource('cold-chain-facilities', layer_name='fc_cold_chain_facility')
class ColdChainFacilityResource:
    pass


@resource('government-buildings', layer_name='sv_fc_poi_govt_building')
class GovernmentBuildingResource:
    pass


@resource('post-offices', layer_name='sv_fc_poi_post_office')
class PostOfficeResource:
    pass


@resource('prisons', layer_name='sv_fc_poi_prison')
class PrisonResource:
    pass


@resource('police-stations', layer_name='sv_fc_poi_police_station')
class PoliceStationResource:
    pass


@resource('filling-stations', layer_name='sv_fc_poi_filling_station')
class FIllingStationResource:
    pass


@resource('mosques', layer_name='sv_fc_poi_mosque')
class MosqueResource:
    pass


@resource('churches', layer_name='sv_fc_poi_church')
class ChurchResource:
    pass


@resource('markets', layer_name='sv_fc_poi_market')
class MarketResource:
    pass


@resource('farms', layer_name='sv_fc_poi_farm')
class FarmResource:
    pass


@resource('factory-industry-sites', layer_name='sv_fc_poi_factory_industry_site')
class FactoryIndustrySiteResource:
    pass


@resource('dump-sites', layer_name='fc_poi_dump_site')
class DumpSiteResource:
    pass


@resource('electricity-substations', layer_name='sv_fc_poi_electricity_substation')
class ElectricitySubstationResource:
    pass


@resource('nigeria-idp-surveys', layer_name='sv_fc_nigeria_idp_survey')
class NigeriaIDPSurveyResource:
    pass


@resource('emergency-services', layer_name='sv_fe_emergency_services')
class EmergencyServiceResource:
    pass


@resource('settlement-points', layer_name='sv_fc_poi_settlementpt')
class SettlementPointResource:
    pass


@resource('boundary-states', layer_name='sv_boundary_states')
class BoundaryStateResource:
    pass


@resource('boundary-lgas', layer_name='sv_boundary_lgas')
class BoundaryLGAResource:
    pass


@resource('boundary-wards', layer_name='sv_boundary_wards')
class BoundaryWardResource:
    pass


@resource('hamlet-areas', layer_name='sv_fe_hamletareas')
class HamletAreaResource:
    pass


@resource('small-settlement-areas', layer_name='sv_fe_smlsettlementareas')
class SmallSettlementAreaResource:
    pass


@resource('builtup-areas', layer_name='sv_fe_builtuparea')
class BuiltupAreaResource:
    pass


@resource('major-roads', layer_name='fe_roads_major')
class MajorRoadResource:
    pass


@resource('tertiary-roads', layer_name='fe_roads_tertiary')
class TertiaryRoadResource:
    pass


@resource('residential-roads', layer_name='fe_roads_residential')
class ResidentialRoadResource:
    pass


@resource('track-roads', layer_name='fe_roads_track')
class TrackRoadResource:
    pass


@resource('village-heads', layer_name='sv_fc_villagehead')
class VillageHeaResource:
    pass


# @resource('', layer_name='sv_')
# class Resource:
#     pass
