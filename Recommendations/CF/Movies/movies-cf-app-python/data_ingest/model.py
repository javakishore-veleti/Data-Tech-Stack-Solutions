from datetime import datetime
from application.settings import db


class IngestEntry(db.Model):
    __tablename__ = 'ingest_entry'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    ingest_file = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime)

    def __int__(self, title=None, ingest_file=None, created_at=None):
        self.title = title
        self.ingest_file = ingest_file
        self.created_at = created_at

    def __repr__(self):
        return '<IngestEntry id:{} title:{} ingest_file:{} />'.format(self.id, self.title, self.ingest_file)
