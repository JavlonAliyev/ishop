from rest_framework.generics import RetrieveAPIView

from account.serialazers import ProfileSerializer


class MeView(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user