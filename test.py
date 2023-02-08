# mixins.CreateModelMixin, //class inheritance.

  # lookup_field = 'pk'

    # def get_queryset(self):
    #     qs = Job.objects.all()
    #     query = self.request.GET.get("q")
    #     if query is not None:
    #         print(query)
    #         qs = qs.filter(Q(title__icontains=query) | Q(date_published__iexact=query)).distinct()
    #     return qs

    # def perform_create(self, serializer):
    #     serializer.save()

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)