from app import db


class DecisionTree(db.Model):
    __tablename__ = 'decision_trees'

    id = db.Column(db.Integer, primary_key=True)
    tree = db.Column(db.JSON(none_as_null=True))

    def __init__(self, tree):
        self.tree = tree

    def serialize(self):
        return {
            'id': self.id,
            'tree': self.tree
        }