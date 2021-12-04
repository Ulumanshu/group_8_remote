import json
import xml.etree.ElementTree as et


class Song:

    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def serialize(self, serializer):
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)

        return serializer.to_str()


class JsonSerializer:
    _instances = []

    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)

    @classmethod
    def __new__(cls, *args, **kwargs):
        print(cls._instances)
        if len(cls._instances) >= 3:
            x = 'More than %s exists!' % len(cls._instances)
            raise Exception(x)
        new_object = object.__new__(cls)
        cls._instances.append(new_object)
        return new_object


class XmlSerializer:
    _instances = []

    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')

    @classmethod
    def __new__(cls, *args, **kwargs):
        print(cls._instances)
        if len(cls._instances) >= 3:
            x = 'More than %s exists!' % len(cls._instances)
            raise Exception(x)
        new_object = object.__new__(cls)
        cls._instances.append(new_object)
        return new_object


class SerializerFactory:

    @staticmethod
    def get_serializer(format):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            raise ValueError(format)


# Inicijuojam daina su duomenim
song = Song('1', 'Water of Love', 'Dire Straits')

######################## FACTORY #############################################################################
# Sukuriame serialaizeriu fabrika (kai kreipsimes i  jo get_serializer() metoda gausim serialaizerio instance)
factory = SerializerFactory()

# Pasidarom tiek serialaizerio instancu kiek reikia formatu
serializer = factory.get_serializer('JSON')
serializer_xml = factory.get_serializer('XML')
##############################################################################################################

# Dainos serialaiz metodui reikia serialaizerio klases kuri moka paversti daina i reikiama formata
print(song.serialize(serializer))
print(song.serialize(serializer_xml))

# Minitask padaryti factory objektus max 3 instancai kad butu, jei bus kuriamas 4tas, kad mestu klaida.

serializer2 = factory.get_serializer('JSON')
serializer_xml2 = factory.get_serializer('XML')

serializer3 = factory.get_serializer('JSON')
serializer_xml3 = factory.get_serializer('XML')

serializer4 = factory.get_serializer('JSON')

