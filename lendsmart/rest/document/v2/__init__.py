# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from lendsmart.base.version import Version
from lendsmart.rest.document.v2.artifact import ArtifactList


class V2(Version):

    def __init__(self, domain):
        """
        Initialize the V2 version of Prediction

        :returns: V2 version of Prediction
        :rtype: lendsmart.rest.prediction.v2.V2.V2
        """
        super(V2, self).__init__(domain)
        self.version = 'v2'
        self._artifact = None

    @property
    def artifact(self):
        """
        :rtype: lendsmart.rest.document.v2.artifact.ArtifactList
        """
        if self._artifact is None:
            self._artifact = ArtifactList(self)
        return self._artifact

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<lendsmart.Document.V2>'