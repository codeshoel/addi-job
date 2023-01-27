from django.db import models



class Organization(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Category(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Job(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    date_published = models.DateField(auto_now_add=True)
    job_start_date = models.DateField(auto_now_add=False, blank=True, null=True)
    no_of_hire = models.PositiveIntegerField(default=1)
    job_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    organizations_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    no_of_applicants = models.PositiveIntegerField(default=0)


    def __str__(self):
        self.name





