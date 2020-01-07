import eventlet

from st2reactor.sensor.base import Sensor

class Sensor1(Sensor):
    def __init__(self, sensor_service, config):
        super(Sensor1, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        pass

    def run(self):
        while not self._stop:
            self._logger.debug('HelloSensor dispatching trigger...')
            count = self.sensor_service.get_value('vm_action.count') or 0
            payload = {'greeting': 'Yo, StackStorm!', 'count': int(count) + 1}
            self.sensor_service.dispatch(trigger='vm_action.event1', payload=payload)
            self.sensor_service.set_value('vm_action.count', payload['count'])
            eventlet.sleep(60)
        pass

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass