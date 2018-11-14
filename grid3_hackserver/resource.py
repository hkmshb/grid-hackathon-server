from .service import resource, model


@model("""type: object
properties:
    category:
		type: string
		description: Classification trhe the prison
	education:
		type: string
		description: Access to education
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	management:
		type: string
		description: Management of the school
	name:
		type: string
		description: Name of the schoool
	number_of_students:
		type: number
		description: Total number of students
	number_of_teachers:
		type: number
		description: Total number of teachers
	poi_type:
		type: string
		description: Point of Interest Type
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	sub_type:
		type: string
		description: School subtype
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
       """{
            "type": "FeatureCollection",
            "totalFeatures": 93843,
            "features": [
                {
                "type": "Feature",
                "id": "sv_fc_poi_school.fid--71209ea8_167073a1504_373a",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                    7.582548000000031,
                    9.073826000000054
                    ]
                },
                "geometry_name": "geom",
                "properties": {
                    "geometry_type": "POINT",
                    "latitude": 9.073826000000054,
                    "longitude": 7.582548000000031,
                    "global_id": "0001fbc2-8d66-44a2-a64e-3b704c85b032",
                    "name": "LEA Primary School Kudu",
                    "category": "Primary",
                    "sub_type": "Primary",
                    "management": "Private",
                    "education": "Formal",
                    "poi_type": "School",
                    "number_of_teachers": null,
                    "number_of_students": null,
                    "ward_code": "FCTABC01",
                    "ward_name": "City Center 1",
                    "lga_code": "15006",
                    "lga_name": "Municipal Area Council",
                    "state_code": "FC",
                    "state_name": "Fct, Abuja"
                }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/schools/?size=1&page=2&sort_by=global_id"
            }
           }""")
@resource('schools', layer_name='sv_fc_poi_school')
class SchoolResource:
    pass


@model("""type: object
properties:
    accessibility:
		type: string
		description: Is the health accessible
	alternate_name:
		type: string
		description: Alternative name for the health facility
	cce_availability:
		type: string
		description: Availability of cold chain equipment
	cce_last_updated:
		type: string
		description: Last updated information on the cold chain equipment
	cce_quantity:
		type: int
		description: Number of cold chain equipment at the health facility
	functional_status:
		type: string
		description: Functional status of the health facility
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	mnch2:
		type: string
		description: Maternal and child service avaliability
	mnch2_last_updated:
		type: string
		description: Last updated information on Maternal and child service
	name:
		type: string
		description: Name of the health facility
	ownership:
		type: string
		description: Who manage the facility
	ri_service_status:
		type: string
		description: Routine Immunization service avaliability
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	type:
		type: string
		description: Type of health facilities
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 43429,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_health_facilities.fid--71209ea8_16708b50071_-6343",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            10.380792,
                            11.094676999999999
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 11.094676999999999,
                        "longitude": 10.380792,
                        "global_id": "0002e613-dd01-40cd-8fe0-4f3e8914fca7",
                        "name": "Kwarati Dispensary",
                        "alternate_name": null,
                        "functional_status": "Functional",
                        "ri_service_status": "Yes",
                        "type": "Primary",
                        "ownership": "Others",
                        "ward_code": "BA0503",
                        "accessibility": null,
                        "cce_quantity": null,
                        "cce_availability": "No",
                        "cce_last_updated": "2018-03-30Z",
                        "mnch2": null,
                        "mnch2_last_updated": null,
                        "ward_name": "Gabarin East",
                        "lga_code": "5005",
                        "lga_name": "Darazo",
                        "state_code": "BA",
                        "state_name": "Bauchi"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/health-facilities/?size=1&page=2"
            }
           }""")
@resource('health-facilities', layer_name='sv_fc_poi_health_facilities')
class HealthFacilityResource:
    pass

@model("""type: object
properties:
    age:
		type: int
		description: Years of Use
	cce_global:
		type: int
		description: Global Unique Identifier for the Cold chain facility
	global_id:
		type: int
		description: Global Unique Identifier for the Cold chain facility
	cce_last_updated:
		type: string
		description: Date that the information on the CCE was updated by the state or assigned body/partner
	decision:
		type: string
		description: current status of each cce
	designation:
		type: string
		description: What type of equipment is it
	editor:
		type: string
		description: Name of the personnel that edit the data
	electricity_availability:
		type: string
		description: Electricity status of the facility
	energy_status:
		type: string
		description: Minimum Litres,Maximum, Litres, Optimal, Not Optimal, NA
	equipment_location:
		type: string
		description: where is the equipment located
	equipment_make:
		type: string
		description: Equipment manufacturer
	equipment_model:
		type: string
		description: Model of the equipment
	equipment_per_site:
		type: int
		description: Total number of equipment at the location/site
	equipment_type:
		type: string
		description: Cold Freezer, Cold Refrigerator, Walk in Cold Room, Walk in Freezer
	facility_globalid:
		type: int
		description: Global Unique Identifier for the health facility
	facility_name:
		type: string
		description: Name of the facility
	functional_status:
		type: string
		description: Is the equipment working or not
	id:
		type: int
		description: Numeric Unique Idenitifer
	installation_year:
		type: int
		description: The year the equipment was installed
	latitude:
		type: number
		description: geolocation of the site (Y)
	lgacode:
		type: string
		description: Unique identifier for local Government Area
	longitude:
		type: number
		description: geolocation of the site (X)
	maximum_volume:
		type: number
		description: Maximum Litres Capacity
	minimum_volume:
		type: number
		description: Minimum Litres Capacity
	optimal_status:
		type: string
		description: Working condition of the cold chain equipment
	owner:
		type: string
		description: The source of information added to the database
	performance_quality_safety:
		type: string
		description: Functionality levels for each of the cce
	refrigerant:
		type: string
		description: The name of the gas (chemical) that powers the cold chain equipment
	replacement_year:
		type: int
		description: year the items to be replaced, it is usually 10 years after the installation
	serial_number:
		type: string
		description: Numeric Identifier
	source:
		type: string
		description: Source of the data
	timestamp:
		type: string
		description: Latest time the data was edited/updated
	wardcode:
		type: string
		description: Unique identiier for the lowest administrative level in Nigeria""", 
        """{
            "type": "FeatureCollection",
            "totalFeatures": 11063,
            "features": [
                {
                "type": "Feature",
                "id": "fc_cold_chain_facility.fid--71209ea8_1670cd863b4_-5070",
                "geometry": null,
                "properties": {
                    "id": 32307,
                    "serial_number": "20VAC",
                    "facility_name": "Gadau Primary Health Center",
                    "wardcode": "BA1009",
                    "timestamp": "2018-07-27T09:46:26Z",
                    "source": "FGN/NPI",
                    "editor": "fashoto.busayo",
                    "owner": null,
                    "equipment_location": "Health Facility",
                    "electricity_availability": "Yes",
                    "designation": "Freezer",
                    "equipment_type": "Compression",
                    "equipment_make": "Vestfrost",
                    "equipment_model": "HF506",
                    "functional_status": "Functional",
                    "refrigerant": "R134a",
                    "minimum_volume": 0,
                    "maximum_volume": 220,
                    "optimal_status": "Unknown",
                    "energy_status": "Electric",
                    "installation_year": 2002,
                    "age": 16,
                    "equipment_per_site": null,
                    "cce_last_updated": null,
                    "replacement_year": null,
                    "facility_globalid": "016d213e-128d-4f5d-8d5c-f8ef787889a7",
                    "lgacode": "5010",
                    "cce_global": "00bad53e-a83b-42bb-84cf-56df1681d4b1",
                    "decision": "Good",
                    "performance_quality_safety": "Non Performance Quality Safety",
                    "latitude": 11.83397739,
                    "longitude": 10.16486094
                }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/cold-chain-facilities/?size=1&page=2"
            }
           }""")
@resource('cold-chain-facilities', layer_name='sv_fc_cold_chain_facility')
class ColdChainFacilityResource:
    pass

@model("""type: object
properties:
    alt_name:
		type: string
		description: Alternative name for the government building
	geometrytype:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lgacode:
		type: string
		description: Unique identifier for local Government Area
	lganame:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	poi_name:
		type: string
		description: Name for the government building
	statecode:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	statename:
		type: string
		description: Name of the second administrative level in Nigeria
	wardcode:
		type: string
		description: Unique identiier for the lowest administrative level in Nigeria
	wardname:
		type: string
		description: Unique identiier for the lowest administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 3502,
            "features": [
                {
                "type": "Feature",
                "id": "sv_fc_poi_govt_building.fid--71209ea8_1670cd863b4_-47c3",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                    7.3618733545185,
                    5.126542229440718
                    ]
                },
                "geometry_name": "geom",
                "properties": {
                    "geometrytype": "POINT",
                    "latitude": 5.126542229440718,
                    "longitude": 7.3618733545185,
                    "global_id": "404db9d5-6041-45f7-bb2a-57f96e20cad4",
                    "poi_name": "Abia States Signage And Advertisement Agency",
                    "alt_name": null,
                    "wardcode": "ABSEZA04",
                    "wardname": "Eziama Ward",
                    "lgacode": "1001",
                    "lganame": "Aba North                                         ",
                    "statecode": "AB        ",
                    "statename": "Abia                     "
                }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                "name": "urn:ogc:def:crs:EPSG::4326"
                }
            }
           }""")
@resource('government-buildings', layer_name='sv_fc_poi_govt_building')
class GovernmentBuildingResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of the post office
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 219,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_post_office.fid--71209ea8_16708b50071_-6358",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            5.128976117012062,
                            7.665912788589689
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 7.665912788589689,
                        "longitude": 5.128976117012062,
                        "global_id": "0338cf1d-e493-48d7-9164-653b842654f4",
                        "name": "Igede Post Office Igede",
                        "ward_code": "EKSIPN06",
                        "ward_name": "Igede B",
                        "lga_code": "13013",
                        "lga_name": "Irepodun/Ifelodun",
                        "state_code": "EK",
                        "state_name": "Ekiti"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/post-offices/?size=1&page=2"
            }
           }""")
@resource('post-offices', layer_name='sv_fc_poi_post_office')
class PostOfficeResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of the prison
	services:
		type: string
		description: Services avaliable 
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 34,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_prison.fid--71209ea8_16708b50071_-6353",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            7.392578814331646,
                            6.858380614889875
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 6.858380614889875,
                        "longitude": 7.392578814331646,
                        "global_id": "04324a99-b7cd-4e8a-9591-b22b51c73783",
                        "name": "Nigeria Prisons Services",
                        "services": "Prison Disease Control",
                        "ward_code": "ENSNSK20",
                        "ward_name": "Owerre Umuoyo",
                        "lga_code": "14013",
                        "lga_name": "Nsukka",
                        "state_code": "EN",
                        "state_name": "Enugu"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/prisons/?size=1&page=2"
            }
           }""")
@resource('prisons', layer_name='sv_fc_poi_prison')
class PrisonResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of the police station
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 760,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_police_station.fid--71209ea8_16708b50071_-6344",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            3.9018961335717455,
                            7.419211652656953
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 7.419211652656953,
                        "longitude": 3.9018961335717455,
                        "global_id": "006f28f4-c187-482f-a4ab-ad9d17816974",
                        "name": "Housing Police Station",
                        "ward_code": "OYSIBN08",
                        "ward_name": "Old Bodija",
                        "lga_code": "31006",
                        "lga_name": "Ibadan North",
                        "state_code": "OY",
                        "state_name": "Oyo"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/police-stations/?size=1&page=2"
            }
           }""")
@resource('police-stations', layer_name='sv_fc_poi_police_station')
class PoliceStationResource:
    pass


@model("""type: object
properties:
    alternate_name:
		type: string
		description: Alternative name for the filling station
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name for the filling station
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 6868,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_filling_station.fid--71209ea8_16708b50071_-6356",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            6.959198319932432,
                            6.054865650126688
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 6.054865650126688,
                        "longitude": 6.959198319932432,
                        "global_id": "00061a34-2676-4b99-946a-edc4ad4bb3f3",
                        "name": "Codry Oil 316",
                        "alternate_name": null,
                        "ward_code": "ANSJJT08",
                        "ward_name": "Nnokwa",
                        "lga_code": "4011",
                        "lga_name": "Idemili South",
                        "state_code": "AN",
                        "state_name": "Anambra"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/filling-stations/?size=1&page=2"
            }
           }""")
@resource('filling-stations', layer_name='sv_fc_poi_filling_station')
class FIllingStationResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of the mosque
	poi_type:
		type: string
		description: Point of Interest type
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 19827,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_mosque.fid--71209ea8_16708b50071_-634e",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            3.9192,
                            7.41105
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 7.41105,
                        "longitude": 3.9192,
                        "global_id": "0007743a-c092-408b-9eed-75bbbd12d6db",
                        "name": "Ikolaba Central Mosque Oluwo Kekere",
                        "poi_type": "Mosque",
                        "ward_code": "OYSIBN04",
                        "ward_name": "Bashorun",
                        "lga_code": "31006",
                        "lga_name": "Ibadan North",
                        "state_code": "OY",
                        "state_name": "Oyo"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/mosques/?size=1&page=2"
            }
           }""")
@resource('mosques', layer_name='sv_fc_poi_mosque')
class MosqueResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of Church
	poi_type:
		type: string
		description: Point of Interest Type
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 28427,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_church.fid--71209ea8_16708b50071_-6355",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            8.37039,
                            5.09576
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 5.09576,
                        "longitude": 8.37039,
                        "name": "St Patrick Catholic Church Mbacoco",
                        "poi_type": "Church",
                        "global_id": "0005a01d-d199-434e-ab9e-6de35dbf037a",
                        "ward_code": "CRSDUK06",
                        "ward_name": "Odukpani",
                        "lga_code": "9015",
                        "lga_name": "Odukpani",
                        "state_code": "CR",
                        "state_name": "Cross River"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/churches/?size=1&page=2"
            }
           }""")
@resource('churches', layer_name='sv_fc_poi_church')
class ChurchResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	market_days_friday:
		type: string
		description: Market days
	market_days_monday:
		type: string
		description: Market days
	market_days_saturday:
		type: string
		description: Market days
	market_days_sunday:
		type: string
		description: Market days
	market_days_thursday:
		type: string
		description: Market days
	market_days_tuesday:
		type: string
		description: Market days
	market_days_wednesday:
		type: string
		description: Market days
	market_type_goods:
		type: string
		description: type of goods sold in market
	name:
		type: string
		description: Name of the market 
	other_market_type_goods:
		type: string
		description: Other type of goods sold in market
	product_description:
		type: string
		description: Products description for goods sold in the market
	settlement_name:
		type: string
		description: Name of the settlement the market is located
	settlement_type:
		type: string
		description: Type of the settlements the market is located
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	total_market_days:
		type: int
		description: Total number of markets
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 10272,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_market.fid--71209ea8_16708b50071_-634d",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            8.838851667,
                            5.657815
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 5.657815,
                        "longitude": 8.838851667,
                        "global_id": "00051fe3-72fc-4317-bfc1-fdb2efaf80ee",
                        "name": "Mfaminyen Market",
                        "settlement_name": null,
                        "market_days_monday": "No",
                        "market_days_tuesday": "Yes",
                        "market_days_wednesday": "No",
                        "market_days_thursday": "No",
                        "market_days_friday": "No",
                        "market_days_saturday": "No",
                        "market_days_sunday": "No",
                        "total_market_days": null,
                        "settlement_type": null,
                        "market_type_goods": "Clothing Livestock Food Stuff",
                        "other_market_type_goods": null,
                        "product_description": null,
                        "ward_code": "CRSKAM07",
                        "ward_name": "Ikpai",
                        "lga_code": "9002",
                        "lga_name": "Akamkpa",
                        "state_code": "CR",
                        "state_name": "Cross River"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/markets/?size=1&page=2"
            }
           }""")
@resource('markets', layer_name='sv_fc_poi_market')
class MarketResource:
    pass


@model("""type: object
properties:
    farm_category:
		type: string
		description: Category of farm practice
	farm_type:
		type: string
		description: Type of farm
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of farm
	power_source:
		type: string
		description: The power source for the farm
	processing_facility:
		type: string
		description: The processing facility for the farm
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 42071,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_farm.fid--71209ea8_16708b50071_-634b",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            8.7514679,
                            5.9388942
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 5.9388942,
                        "longitude": 8.7514679,
                        "global_id": "0002da4c-9f53-40ee-bf40-ec064c4dbfd9",
                        "name": "Cassava Farm 22",
                        "farm_type": "Both",
                        "processing_facility": null,
                        "power_source": null,
                        "farm_category": "Unknown",
                        "ward_code": "CRSKMM03",
                        "ward_name": "Ikom 1",
                        "lga_code": "9011",
                        "lga_name": "Ikom",
                        "state_code": "CR",
                        "state_name": "Cross River"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/farms/?size=1&page=2"
            }
           }""")
@resource('farms', layer_name='sv_fc_poi_farm')
class FarmResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of the industry
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	status:
		type: string
		description: Cuurent status of the industry
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 7933,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_factory_industry_site.fid--71209ea8_16708b50071_-6349",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            3.6840656613821707,
                            6.460904425946122
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 6.460904425946122,
                        "longitude": 3.6840656613821707,
                        "global_id": "001a5124-6f66-457f-ac1b-c4f1fde6a61a",
                        "name": "Kadiri Block Industry",
                        "status": "In Use",
                        "ward_code": "LASEOA18",
                        "ward_name": "Sangotedo",
                        "lga_code": "25008",
                        "lga_name": "Eti Osa",
                        "state_code": "LA",
                        "state_name": "Lagos"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/factory-industry-sites/?size=1&page=2"
            }
           }""")
@resource('factory-industry-sites', layer_name='sv_fc_poi_factory_industry_site')
class FactoryIndustrySiteResource:
    pass

@model("""type: object
properties:
    dumpsite_category:
		type: string
		description: Dumpsite Classification
	dumpsite_name:
		type: string
		description: Name of the dumpsite
	dumpsite_ownership:
		type: string
		description: Who manage the dumpsite
	dumpsite_type:
		type: string
		description: The type of dumpsite
	editor:
		type: string
		description: Name of the editor 
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: int
		description: Numeric Unique Idenitifer
	secondary_editor:
		type: string
		description: Name of the second editor 
	source:
		type: string
		description: Source of the data
	timestamp:
		type: string
		description: Latest time the data was edited/updated
	wardcode:
		type: string
		description: Unique identiier for the lowest administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 6485,
            "features": [
                {
                "type": "Feature",
                "id": "fc_poi_dump_site.fid--71209ea8_1670cd863b4_-47c6",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                    8.3313272,
                    4.9860717
                    ]
                },
                "geometry_name": "geom",
                "properties": {
                    "id": 20138,
                    "dumpsite_name": "Wapi Dumpsite",
                    "dumpsite_type": "Official",
                    "dumpsite_ownership": null,
                    "dumpsite_category": "Organic Dumpsite",
                    "wardcode": "CRSCAL03",
                    "timestamp": "12:45:29Z",
                    "source": "GRID",
                    "editor": "Racheal.Olarewaju",
                    "secondary_editor": null,
                    "global_id": "ff377abc-384f-4f64-98ab-a672332ac9e5"
                }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/post-offices/?size=1&page=2"
            }
           }""")
@resource('dump-sites', layer_name='sv_fc_poi_dump_site')
class DumpSiteResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of substation
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 1240,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_poi_electricity_substation.fid--71209ea8_16708b50071_-6351",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            7.973426667,
                            6.396693333
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 6.396693333,
                        "longitude": 7.973426667,
                        "global_id": "00299c3c-995a-4877-ae23-cb38aff7a984",
                        "name": "Electricity Transformer Ndiagu Okpe",
                        "ward_code": "EBSHKW28",
                        "ward_name": "Umuagara",
                        "lga_code": "11012",
                        "lga_name": "Ohaukwu",
                        "state_code": "EB",
                        "state_name": "Ebonyi"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/electricity-substations/?size=1&page=2"
            }
           }""")
@resource('electricity-substations', layer_name='sv_fc_poi_electricity_substation')
class ElectricitySubstationResource:
    pass


@model("""type: object
properties:
    agency_contact:
		type: number
		description: Contact of agency managing the camp
	agency_name:
		type: string
		description: Name of agency managing the camp
	boys_pop_1_to_5:
		type: int
		description: Population for boys between 1 - 5 years
	boys_pop_6_to_17:
		type: int
		description: Population for boys between 6 - 17 years
	boys_pop_under_1:
		type: int
		description: Population for boys under 1 year
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	girls_pop_1_to_5:
		type: int
		description: Population for girls between 1 - 5 years
	girls_pop_6_to_17:
		type: int
		description: Population for girls between 6 - 17 years
	girls_pop_under_1:
		type: int
		description: Population for girls under 1 year
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: string
		description: Numeric Unique Idenitifer
	idp_amenities_food:
		type: string
		description: Access to food
	idp_amenities_health_facility:
		type: string
		description: Access to health facility
	idp_amenities_housing:
		type: string
		description: Access to housing
	idp_amenities_medicine:
		type: string
		description: Regular access to medication
	idp_amenities_portable_water:
		type: string
		description: Access to portable water
	idp_health_facility_provider:
		type: string
		description: Access to health facility providers
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	men_pop_18_to_59:
		type: int
		description: Replaced by men_pop_18_59 & women_pop_18_59
	men_pop_above_60:
		type: int
		description: Replaced by men_pop_above60 & women_pop_above60
	name:
		type: string
		description: Name of the IDP camp
	population_source:
		type: string
		description: Source of the population estimate
	settlement_name:
		type: string
		description: Name of the settlement
	site_opening_date:
		type: string
		description: Opening Date the IDP camp
	site_status:
		type: string
		description: Status of the IDP camp
	site_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	total_household:
		type: int
		description: Number of households
	total_population:
		type: int
		description: Total population of the IDP camp
	type_of_sma:
		type: string
		description: Type
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria
	women_pop_18_to_59:
		type: int
		description: Population for women between 18 - 59 years
	women_pop_above_60:
		type: int
		description: Population for women above 60 years""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 858,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_nigeria_idp_survey.fid--71209ea8_16708b50071_-634a",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            11.30343,
                            9.82906
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 9.82906,
                        "longitude": 11.30343,
                        "name": "Millionaira Quarters",
                        "id": null,
                        "population_source": "IOM DTM RD16 May 2017",
                        "total_population": null,
                        "global_id": "00fb8c2a-4fb5-4cd7-999d-a2887b787d02",
                        "settlement_name": "Millionaira Quarters",
                        "site_type": "Host Communities",
                        "site_status": null,
                        "site_opening_date": null,
                        "type_of_sma": null,
                        "agency_name": null,
                        "agency_contact": null,
                        "idp_amenities_housing": null,
                        "idp_amenities_food": null,
                        "boys_pop_under_1": null,
                        "girls_pop_under_1": null,
                        "boys_pop_1_to_5": null,
                        "girls_pop_1_to_5": null,
                        "boys_pop_6_to_17": null,
                        "girls_pop_6_to_17": null,
                        "men_pop_18_to_59": null,
                        "women_pop_18_to_59": null,
                        "men_pop_above_60": null,
                        "women_pop_above_60": null,
                        "total_household": null,
                        "idp_amenities_medicine": null,
                        "idp_amenities_health_facility": null,
                        "idp_health_facility_provider": null,
                        "idp_amenities_portable_water": null,
                        "ward_code": "GMSKLT05",
                        "ward_name": "Kaltungo West",
                        "lga_code": "16007",
                        "lga_name": "Kaltungo",
                        "state_code": "GO",
                        "state_name": "Gombe"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::404000"
                }
            },
            "pager": {
                "next": "http://localhost:5000/nigeria-idp-surveys/?size=1&page=2"
            }
           }""")
@resource('nigeria-idp-surveys', layer_name='sv_fc_nigeria_idp_survey')
class NigeriaIDPSurveyResource:
    pass


@model("""type: object
properties:
    ambulance:
		type: string
		description: Access to ambulance service
	fire_personel:
		type: number
		description: Avaliability of fire perssonel
	fire_station:
		type: string
		description: Access to fire srvice
	fire_vehicle:
		type: number
		description: Avaliability of fire vehcile
	functional_fire_vehicle:
		type: number
		description: Functional staus of fire vehcile
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of the emergency services
	police_station:
		type: string
		description: Avaliability of police station
	service_type:
		type: string
		description: service type
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 71,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fe_emergency_services.fid--71209ea8_16708b50071_-634f",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            4.677668333,
                            8.026973333
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 8.026973333,
                        "longitude": 4.677668333,
                        "global_id": "05fc67d4-b909-4a60-bde6-1fa0cd7046ef",
                        "name": "Department Of Fire Service Okuku",
                        "police_station": null,
                        "ambulance": null,
                        "fire_station": null,
                        "fire_vehicle": null,
                        "fire_personel": null,
                        "service_type": "Fire Station",
                        "functional_fire_vehicle": null,
                        "ward_code": "OSSODN09",
                        "ward_name": "Oba/ojomo",
                        "lga_code": "30025",
                        "lga_name": "Odo Otin",
                        "state_code": "OS",
                        "state_name": "Osun"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/emergency-services/?size=1&page=2"
            }
           }""")
@resource('emergency-services', layer_name='sv_fe_emergency_services')
class EmergencyServiceResource:
    pass


@model("""type: object
properties:
    alternate_name:
		type: string
		description: Alternative name for the school
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identiier for the third administrative level in Nigeria
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name for the school
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 268460,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_settlementpt.fid--71209ea8_16708b50071_-6357",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            4.519138509743584,
                            11.419383456135733
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 11.419383456135733,
                        "longitude": 4.519138509743584,
                        "global_id": "000061a2-2761-4181-81e4-135eb3893c11",
                        "name": "Dandabin Makera Iliya Mai Feke Site",
                        "alternate_name": null,
                        "ward_code": "51301",
                        "ward_name": "Koko Magaji",
                        "lga_code": "513",
                        "lga_name": "Koko-Besse",
                        "state_code": "KB",
                        "state_name": "Kebbi"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/settlement-points/?size=1&page=2"
            }
           }""")
@resource('settlement-points', layer_name='sv_fc_settlementpt')
class SettlementPointResource:
    pass


@model("""type: object
properties:
	capital_city:
		type: string
		description: Name of the capital for the state
	geographic_zone:
		type: string
		description: Name of the zone inwhich the state falls
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 37,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_boundary_states.fid--71209ea8_16708b50071_-6346",
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [
                                        7.030075072803454,
                                        9.257713318511168
                                    ],
                                    [
                                        7.015266894741865,
                                        9.268970490160049
                                    ],
                                    [
                                        6.788054466359057,
                                        9.270166396971685
                                    ],
                                    [
                                        6.786707401443781,
                                        9.15533542594788
                                    ],
                                    [
                                        6.785022879299189,
                                        9.011721931367283
                                    ]
                                ]
                            ]
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "MULTIPOLYGON",
                        "state_code": "FC",
                        "state_name": "Fct, Abuja",
                        "capital_city": "Abuja",
                        "global_id": "0e73256c-2793-44cc-ab1b-7289f145b866",
                        "geographic_zone": "NCZ"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/boundary-states/?size=1&page=2"
            }
           }""")
@resource('boundary-states', layer_name='sv_boundary_states')
class BoundaryStateResource:
    pass


@model("""type: object
properties:
	amap_code:
		type: string
		description: WHO Unique identifier for local Government Area
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 774,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_boundary_lgas.fid--71209ea8_16708b50071_-6352",
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [
                                        5.889581202854941,
                                        5.672451019429851
                                    ],
                                    [
                                        5.899827002817175,
                                        5.662134171420284
                                    ],
                                    [
                                        5.90394401561479,
                                        5.65384721778974
                                    ],
                                    [
                                        5.910789013266144,
                                        5.643500804759993
                                    ],
                                    [
                                        5.918334007393066,
                                        5.629001140908262
                                    ],
                                    [
                                        5.908166884484311,
                                        5.612124920441101
                                    ]
                                ]
                            ]
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "MULTIPOLYGON",
                        "amap_code": "NIE DTS KPE",
                        "lga_code": "10013",
                        "lga_name": "Okpe",
                        "state_code": "DE",
                        "global_id": "00cbf90b-93e1-4abb-a471-d3ff1924340f",
                        "state_name": "Delta"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/boundary-lgas/?size=1&page=2"
            }
           }""")
@resource('boundary-lgas', layer_name='sv_boundary_lgas')
class BoundaryLGAResource:
    pass


@model("""type: object
properties:
    amapcode:
		type: string
		description: WHO Unique identifier for ward
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	status:
		type: string
		description: Completene  staus of the ward
	urban:
		type: string
		description: ward status (Is the ward urban or rural)
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 6903,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_boundary_wards.fid--71209ea8_16708b50071_-6348",
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [
                                        8.242117851332802,
                                        12.826141565139855
                                    ],
                                    [
                                        8.230117279178945,
                                        12.826155354149273
                                    ],
                                    [
                                        8.210958039161179,
                                        12.817520348282038
                                    ],
                                    [
                                        8.200746591222952,
                                        12.816431035541884
                                    ],
                                    [
                                        8.192468933598686,
                                        12.815703330047477
                                    ],
                                    [
                                        8.187890755488036,
                                        12.814417683173906
                                    ],
                                    [
                                        8.18228435367873,
                                        12.812468136849253
                                    ]
                                ]
                            ]
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "MULTIPOLYGON",
                        "amapcode": "NIE KTS DTS DAA",
                        "global_id": "003d4dfc-7820-4569-a89d-34b982d7795c",
                        "urban": "No",
                        "status": "Validated",
                        "ward_code": "41101",
                        "ward_name": "Dan Aunai",
                        "lga_code": "411",
                        "lga_name": "Dutsi",
                        "state_code": "KT",
                        "state_name": "Katsina"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/boundary-wards/?size=1&page=2"
            }
           }""")
@resource('boundary-wards', layer_name='sv_boundary_wards')
class BoundaryWardResource:
    pass


@model("""type: object
properties:
    calculated_name:
		type: string
		description: Generated name for the hamlet areas
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: string
		description: Numeric Unique Idenitifer
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_distance:
		type: number
		description: Distance of settlement to the Local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	locked:
		type: string
		description: In-use status of the dataset
	major_road_distance:
		type: number
		description: Distance of settlement to the major road
	name:
		type: string
		description: Name of the hanlets area
	nb_denominator:
		type: int
		description: Area Denominator
	object_id:
		type: string
		description: Object unique Identifier
	source:
		type: string
		description: Source of the data
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	tertiary_road_distance:
		type: number
		description: Distance of settlement to the tertiary road
	timestamp:
		type: string
		description: Latest time the data was edited/updated
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_distance:
		type: number
		description: Distance of settlement to the ward 
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 212210,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fe_hamletareas.fid--71209ea8_16708b50071_-6350",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    11.588989643375157,
                                    11.001620149285202
                                ],
                                [
                                    11.588876092298051,
                                    11.001602380273141
                                ],
                                [
                                    11.588761636220283,
                                    11.0015916912659
                                ]
                            ]
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "id": "4786546",
                        "name": "HA_13",
                        "ward_code": "70811",
                        "source": null,
                        "timestamp": null,
                        "global_id": "0000281b-8070-4c4c-bd09-809336c2f9b2",
                        "locked": null,
                        "object_id": "HA_70811_4786546",
                        "calculated_name": "HA_13",
                        "nb_denominator": null,
                        "ward_distance": 0,
                        "lga_distance": 8020.6018133,
                        "major_road_distance": 51151.45714806,
                        "tertiary_road_distance": 4390.65652678,
                        "geometry_type": "POLYGON",
                        "ward_name": "Njibulwa",
                        "lga_code": "708",
                        "lga_name": "Gulani",
                        "state_code": "YO",
                        "state_name": "Yobe"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/hamlet-areas/?size=1&page=2"
            }
           }""")
@resource('hamlet-areas', layer_name='sv_fe_hamletareas')
class HamletAreaResource:
    pass


@model("""type: object
properties:
    calculated_name:
		type: string
		description: Generated name for the small settlement areas
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: string
		description: Numeric Unique Idenitifer
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_distance:
		type: number
		description: Distance of settlement to the Local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	major_road_distance:
		type: number
		description: Distance of settlement to the major road
	name:
		type: string
		description: Name of the small settlement areas
	nb_denominator:
		type: int
		description: Area Denominator
	object_id:
		type: string
		description: Object unique Identifier
	source:
		type: string
		description: Source of the data
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	tertiary_road_distance:
		type: number
		description: Distance of settlement to the tertiary road
	timestamp:
		type: string
		description: Latest time the data was edited/updated
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_distance:
		type: number
		description: Distance of settlement to the ward 
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria
	weight:
		type: number
		description: weight""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 37628,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fe_smlsettlementareas.fid--71209ea8_16708b50071_-6345",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    3.499224797760178,
                                    6.961281899065284
                                ],
                                [
                                    3.4992837588002317,
                                    6.961319373090703
                                ],
                                [
                                    3.4993462638427104,
                                    6.961350591111909
                                ],
                                [
                                    3.499411649887122,
                                    6.961375221128662
                                ],
                                [
                                    3.499479223933008,
                                    6.961393003140756
                                ],
                                [
                                    3.4995482699799254,
                                    6.961403749148076
                                ],
                                [
                                    3.4996180550273834,
                                    6.9614073431504835
                                ]
                            ]
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "id": "975149",
                        "name": "SSA_40",
                        "ward_code": "OGSOBE12",
                        "source": "EHA-NURADDEEN",
                        "timestamp": "2016-04-14T14:23:47Z",
                        "global_id": "0006ab8b-d8cf-45a7-afdb-85be263cdfe0",
                        "object_id": "SSA_OGSOBE12_975149",
                        "calculated_name": "SSA_40",
                        "nb_denominator": 1,
                        "weight": 3,
                        "ward_distance": 1030.19101369,
                        "lga_distance": 9107.33800686,
                        "major_road_distance": 386958.70868558,
                        "tertiary_road_distance": 376937.27876658,
                        "geometry_type": "POLYGON",
                        "ward_name": "Owode",
                        "lga_code": "28015",
                        "lga_name": "Obafemi Owode",
                        "state_code": "OG",
                        "state_name": "Ogun"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/small-settlement-areas/?size=1&page=2"
            }
           }""")
@resource('small-settlement-areas', layer_name='sv_fe_smlsettlementareas')
class SmallSettlementAreaResource:
    pass


@model("""type: object
properties:
    calculated_name:
		type: string
		description: Generated name for the builtuparea
	geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: string
		description: Numeric Unique Idenitifer
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_distance:
		type: number
		description: Distance of settlement to the Local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	major_road_distance:
		type: number
		description: Distance of settlement to the major road
	name:
		type: string
		description: Name of the Settlement (builtup areas)
	nb_denominator:
		type: int
		description: Area Denominator
	object_id:
		type: string
		description: Object unique Identifier
	source:
		type: string
		description: Source of the data
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	tertiary_road_distance:
		type: number
		description: Distance of settlement to the tertiary road
	timestamp:
		type: string
		description: Latest time the data was edited/updated
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_distance:
		type: number
		description: Distance of settlement to the ward 
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria
	weight:
		type: number
		description: weight""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 11933,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fe_builtuparea.fid--71209ea8_16708b50071_-6354",
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [
                                        12.923061895814556,
                                        10.87689257253868
                                    ],
                                    [
                                        12.922498595431819,
                                        10.877942915252333
                                    ],
                                    [
                                        12.921814076966768,
                                        10.878699158766153
                                    ],
                                    [
                                        12.921001213414456,
                                        10.879175312089728
                                    ],
                                    [
                                        12.920870489325637,
                                        10.880750812160159
                                    ]
                                ]
                            ]
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "id": "316774",
                        "name": "Kuburmbula Kwikanda",
                        "ward_code": "10604",
                        "source": "EHA-SAMUEL",
                        "timestamp": "2014-10-30T11:49:47Z",
                        "global_id": "00154b77-b482-424d-b66e-6895b8805615",
                        "object_id": "BUA_10604_316774",
                        "calculated_name": "Kuburmbula Kwikanda",
                        "nb_denominator": 164,
                        "weight": 164,
                        "ward_distance": 2995.10174317,
                        "lga_distance": 8181.62083419,
                        "major_road_distance": 99608.68050502,
                        "tertiary_road_distance": 95016.61559065,
                        "geometry_type": "MULTIPOLYGON",
                        "ward_name": "Kuburmbulla",
                        "lga_code": "106",
                        "lga_name": "Chibok",
                        "state_code": "BR",
                        "state_name": "Borno"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/builtup-areas/?size=1&page=2"
            }
           }""")
@resource('builtup-areas', layer_name='sv_fe_builtuparea')
class BuiltupAreaResource:
    pass

@model("""type: object
properties:
    global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: int
		description: Numeric Unique Idenitifer
	name:
		type: string
		description: Name of the road
	source:
		type: string
		description: Source of the data
	timestamp:
		type: string
		description: Latest time the data was edited/updated""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 5426,
            "features": [
                {
                "type": "Feature",
                "id": "fe_roads_major.fid--71209ea8_1670cd863b4_-47c5",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                    [
                        3.655747989623592,
                        11.855384549064524
                    ],
                    [
                        3.657486496767433,
                        11.85820625629799
                    ],
                    [
                        3.6593100419183315,
                        11.861241176549072
                    ],
                    [
                        3.659868047964494,
                        11.86216985762593
                    ],
                    [
                        3.6623779451721816,
                        11.86628691796659
                    ],
                    [
                        3.6654012324223118,
                        11.871380823388051
                    ]
                    ]
                },
                "geometry_name": "geom",
                "properties": {
                    "name": null,
                    "source": "",
                    "timestamp": "2012-08-01T18:16:19Z",
                    "global_id": "de8778ee-c8b9-4f40-a65f-1cfc21e718c3",
                    "id": 3
                }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/builtup-areas/?size=1&page=2"
            }
           }""")
@resource('major-roads', layer_name='sv_fe_roads_major')
class MajorRoadResource:
    pass


@model("""type: object
properties:
    global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: int
		description: Numeric Unique Idenitifer
	name:
		type: string
		description: Name of the road
	source:
		type: string
		description: Source of the data
	timestamp:
		type: string
		description: Latest time the data was edited/updated""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 5426,
            "features": [
                {
                "type": "Feature",
                "id": "fe_roads_tertiary.fid--71209ea8_1670cd863b4_-47c5",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                    [
                        3.655747989623592,
                        11.855384549064524
                    ],
                    [
                        3.657486496767433,
                        11.85820625629799
                    ],
                    [
                        3.6593100419183315,
                        11.861241176549072
                    ],
                    [
                        3.659868047964494,
                        11.86216985762593
                    ],
                    [
                        3.6623779451721816,
                        11.86628691796659
                    ],
                    [
                        3.6654012324223118,
                        11.871380823388051
                    ]
                    ]
                },
                "geometry_name": "geom",
                "properties": {
                    "name": null,
                    "source": "",
                    "timestamp": "2012-08-01T18:16:19Z",
                    "global_id": "de8778ee-c8b9-4f40-a65f-1cfc21e718c3",
                    "id": 3
                }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/builtup-areas/?size=1&page=2"
            }
           }""")
@resource('tertiary-roads', layer_name='sv_fe_roads_tertiary')
class TertiaryRoadResource:
    pass


@model("""type: object
properties:
    global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: int
		description: Numeric Unique Idenitifer
	name:
		type: string
		description: Name of the road
	source:
		type: string
		description: Source of the data
	timestamp:
		type: string
		description: Latest time the data was edited/updated""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 5426,
            "features": [
                {
                "type": "Feature",
                "id": "fe_roads_residential.fid--71209ea8_1670cd863b4_-47c5",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                    [
                        3.655747989623592,
                        11.855384549064524
                    ],
                    [
                        3.657486496767433,
                        11.85820625629799
                    ],
                    [
                        3.6593100419183315,
                        11.861241176549072
                    ],
                    [
                        3.659868047964494,
                        11.86216985762593
                    ],
                    [
                        3.6623779451721816,
                        11.86628691796659
                    ],
                    [
                        3.6654012324223118,
                        11.871380823388051
                    ]
                    ]
                },
                "geometry_name": "geom",
                "properties": {
                    "name": null,
                    "source": "",
                    "timestamp": "2012-08-01T18:16:19Z",
                    "global_id": "de8778ee-c8b9-4f40-a65f-1cfc21e718c3",
                    "id": 3
                }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/builtup-areas/?size=1&page=2"
            }
           }""")
@resource('residential-roads', layer_name='sv_fe_roads_residential')
class ResidentialRoadResource:
    pass


@model("""type: object
properties:
    global_id:
		type: int
		description: Global Unique Identifier for the dataset
	id:
		type: int
		description: Numeric Unique Idenitifer
	name:
		type: string
		description: Name of the road
	source:
		type: string
		description: Source of the data
	timestamp:
		type: string
		description: Latest time the data was edited/updated""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 5426,
            "features": [
                {
                "type": "Feature",
                "id": "fe_roads_track.fid--71209ea8_1670cd863b4_-47c5",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                    [
                        3.655747989623592,
                        11.855384549064524
                    ],
                    [
                        3.657486496767433,
                        11.85820625629799
                    ],
                    [
                        3.6593100419183315,
                        11.861241176549072
                    ],
                    [
                        3.659868047964494,
                        11.86216985762593
                    ],
                    [
                        3.6623779451721816,
                        11.86628691796659
                    ],
                    [
                        3.6654012324223118,
                        11.871380823388051
                    ]
                    ]
                },
                "geometry_name": "geom",
                "properties": {
                    "name": null,
                    "source": "",
                    "timestamp": "2012-08-01T18:16:19Z",
                    "global_id": "de8778ee-c8b9-4f40-a65f-1cfc21e718c3",
                    "id": 3
                }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/builtup-areas/?size=1&page=2"
            }
           }""")
@resource('track-roads', layer_name='sv_fe_roads_track')
class TrackRoadResource:
    pass


@model("""type: object
properties:
    geometry_type:
		type: string
		description: the structure of spatial objects in terms of points, lines, polygons, polylines
	global_id:
		type: int
		description: Global Unique Identifier for the dataset
	latitude:
		type: number
		description: geolocation of the site (Y)
	lga_code:
		type: string
		description: Unique identifier for local Government Area
	lga_name:
		type: string
		description: Name of the third administrative level in Nigeria
	longitude:
		type: number
		description: geolocation of the site (X)
	name:
		type: string
		description: Name of the village head
	state_code:
		type: string
		description: Unique identiier for the second administrative level in Nigeria
	state_name:
		type: string
		description: Name of the second administrative level in Nigeria
	ward_code:
		type: string
		description: Unique identiier for the fourth administrative level in Nigeria
	ward_name:
		type: string
		description: Name of the fourth administrative level in Nigeria""",
        """{
            "type": "FeatureCollection",
            "totalFeatures": 19848,
            "features": [
                {
                    "type": "Feature",
                    "id": "sv_fc_villagehead.fid--71209ea8_16708b50071_-6347",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            8.879999998880123,
                            12.00659999957611
                        ]
                    },
                    "geometry_name": "geom",
                    "properties": {
                        "geometry_type": "POINT",
                        "latitude": 12.00659999957611,
                        "longitude": 8.879999998880123,
                        "global_id": "00043708-f33f-453b-aa59-51df47ffffe2",
                        "name": "VillageHead House 23 Joda",
                        "ward_code": "KN1303",
                        "ward_name": "Joda",
                        "lga_code": "20016",
                        "lga_name": "Gabasawa",
                        "state_code": "KN",
                        "state_name": "Kano"
                    }
                }
            ],
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                }
            },
            "pager": {
                "next": "http://localhost:5000/village-heads/?size=1&page=2"
            }
           }""")
@resource('village-heads', layer_name='sv_fc_villagehead')
class VillageHeaResource:
    pass
