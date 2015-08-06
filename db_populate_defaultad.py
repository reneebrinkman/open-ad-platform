#!.venv/bin/python

import config
from app import models, db

a = models.Advertisement(
    ad_name='ad space available for purchase',
    ad_url=config.SITE_URL,
    textad_content='Your business here, your product here, your ad here.  Click here for more details.'
)

db.session.add(a)
db.session.commit()
