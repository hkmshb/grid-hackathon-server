import pytest
from grid3_hackserver.service import get_services, resource, Service


class TestService:
    def test_created_servcies_are_auto_registered(self):
        assert get_services() == []
        dummy_service = Service(
            'dummy',
            layer_name='sv_fc_dummy'
        )

        services = get_services()
        assert services != []
        assert len(services) == 1
        assert services[0] is dummy_service

    def test_get_service_can_filter_by_specified_names(self):
        dummy_services = [
            Service('dummy-1', layer_name='sv_fc_dummy-1'),
            Service('dummy-2', layer_name='sv_fc_dummy-2'),
        ]
        services = get_services()
        assert services and len(services) == 2

        services = get_services(names=['dummy-1'])
        assert services and len(services) == 1
        assert services[0].name == 'dummy-1'


class TestResourceUtilityFuncs:

    def _define_resource_with_name(self):
        @resource('dummy-resource', layer_name='sv_dummy_resource')
        class DummyResource:
            pass

    def _define_resource_without_name(self):
        @resource(layer_name='sv_dummy_layer')
        class DummyLayer:
            pass

        @resource(layer_name='sv_dummy_layer_resource')
        class DummyLayer2Resource:
            pass

    def test_decorator_able_to_register_service_for_resource(self):
        services = get_services()
        assert not services

        self._define_resource_with_name()
        services = get_services()
        assert services and len(services) == 1
        assert services[0].name == 'dummy-resource'

    def test_decorator_autogen_name_for_service_if_not_provided(self):
        services = get_services()
        assert not services

        self._define_resource_without_name()
        services = get_services()

        assert services and len(services) == 2
        assert services[0].name == 'dummylayer'

        # 'Resource' stripped from class names when used for service name
        assert services[1].name == 'dummylayer2'