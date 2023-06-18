import random


from celery import shared_task


from apps.proposal.models.proposal import ProposalModel


@shared_task
def start_queue(id):
    obj_proposal = ProposalModel.objects.filter(id=id).first()
    if obj_proposal:
        status = random.choice(["Aprovada", "Negada"])
        obj_proposal.proposal_situation = status
        obj_proposal.save()
  
