class DoubleGisMixin(object):
    """Mixin to another class to provide access to a User's ``Score``."""

    @property
    def get_location(self):
        if self.geolocation:
            result = []
            if ';' in str(self.geolocation):
                for i in str(self.geolocation).split(';'):
                    result.append({'lat': i.split(',')[0], 'lng': i.split(',')[1]})
                return result
            result.append({'lat': str(self.geolocation).split(',')[0], 'lng': str(self.geolocation).split(',')[1]})
            return result
