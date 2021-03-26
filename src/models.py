import mongoengine


class PokiPic(mongoengine.Document):
    image = mongoengine.fields.ImageField()
    format = mongoengine.StringField(required=True)

