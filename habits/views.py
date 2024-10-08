from rest_framework.permissions import IsAuthenticated

from habits.paginations import HabitPagination
from habits.serializers import HabitSerializer
from rest_framework.viewsets import ModelViewSet
from users.permissions import IsOwner

from habits.models import Habit


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "destroy"]:
            self.permission_classes = (IsOwner,)
        elif self.action == "list":
            self.permission_classes = (IsAuthenticated,)
        elif self.action == "retrieve":
            self.permission_classes = (IsOwner | IsAuthenticated,)
        return super().get_permissions()

    def get_queryset(self):
        if self.action == "list":
            return Habit.objects.filter(is_public=True) | Habit.objects.filter(
                owner=self.request.user
            )
        return super().get_queryset()
