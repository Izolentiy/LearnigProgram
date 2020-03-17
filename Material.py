class BaseMaterial:
    def __init__(self):
        self.name = None
        self.author = None
        self.level = None
        self.description = None
        self.links = None

        self.keys = ['NAME', 'AUTHOR', 'LEVEL', 'DESCRIPTION', 'LINKS']
        self.values = [self.name, self.author, self.level, self.description, self.links]

        self.properties = dict(zip(self.keys, self.values))


class Book(BaseMaterial):
    type = "BOOKS"

    def __init__(self):
        super().__init__()
        self.type = Book.type

        self.page_count = None
        self.keys.append('PAGES')
        self.properties['PAGES'] = self.page_count


class Lecture(BaseMaterial):
    type = "LECTURES"

    def __init__(self):
        super().__init__()
        self.type = Lecture.type

        self.length = None
        self.keys.append('LENGTH')
        self.properties['LENGTH'] = self.length


class WebResource(BaseMaterial):
    type = "WEB RESOURCES"

    def __init__(self):
        super().__init__()
        self.type = WebResource.type


def create_material(material_type):
    if material_type == Book.type:
        return Book()
    elif material_type == Lecture.type:
        return Lecture()
    elif material_type == WebResource.type:
        return WebResource()
    else:
        print('invalid type')


def get_material_keys():
    return ['NAME', 'AUTHOR', 'LEVEL', 'DESCRIPTION', 'LINKS']  # Return default keys set
