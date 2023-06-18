from django.db import models
from django.utils.text import slugify


from apps.proposal.models.fields import FieldsModel


class ProposalModel(models.Model):

    SITUATION_CHOICES = (
        ('Em análise','Em análise'),
        ('Aprovada','Aprovada'),
        ('Negada','Negada'),
    )    
    
    title = models.CharField(max_length=800)
    slug = models.SlugField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    field = models.ManyToManyField(FieldsModel, related_name='pillars', through='ProposalFieldAssignment')
    proposal_situation = models.CharField(max_length=50, default='Em análise', choices=SITUATION_CHOICES)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ProposalModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"
        db_table = 'proposal'

    def __str__(self):
        return self.title

class ProposalFieldAssignment(models.Model):
    proposal = models.ForeignKey(ProposalModel, on_delete=models.CASCADE, related_name='field_assignments')
    field = models.ForeignKey(FieldsModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Atribuição de questão"
        verbose_name_plural = "Atribuições de questões"
        db_table = 'proposal_field_assignment'
       

    def __str__(self):
        return f"{self.proposal.title} - {self.field.label}"
    
