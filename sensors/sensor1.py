import eventlet

from st2reactor.sensor.base import Sensor


class HelloSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(HelloSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        pass

    def run(self):        
        self._logger.debug('HelloSensor dispatching trigger...')
        count = self.sensor_service.get_value('st2_utils.count') or 0
        payload = {'greeting': '1.1.1.1,2.2.2.2', 'count': int(count) + 1}
        self.sensor_service.dispatch(trigger='st2_utils.event1', payload=payload)
        self.sensor_service.set_value('st2_utils.count', payload['count'])
            
    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass