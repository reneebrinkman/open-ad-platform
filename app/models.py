from app import db

class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_ad = db.Column(db.SmallInteger, default=False)
    ad_name = db.Column(db.String(120), index=True, unique=True)
    textad_content = db.Column(db.String(512))
    imagead_filename = db.Column(db.String(120))
    ad_url = db.Column(db.String(255))

    def __repr__(self):
        return '<Advertisement: {}>'.format(self.ad_name)

    def render(self):
        ad = {'name': self.ad_name, 'url': self.ad_url}
        if self.image_ad:
            ad['ad'] = self.imagead_filename
        else:
            ad['ad'] = self.textad_content
        return ad
