from django.db import models


class AnswersModel(models.Model):


    proposal = models.ForeignKey('proposal.ProposalModel', on_delete=models.DO_NOTHING, null=True, default=None, related_name='answers')
    field = models.ForeignKey('proposal.FieldsModel', on_delete=models.DO_NOTHING, related_name='answers', null=True, default=None)
    value = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"
        db_table = 'answers'

    def __str__(self):
        return self.value

