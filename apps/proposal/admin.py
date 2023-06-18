from django.contrib import admin


from apps.proposal.models.fields import FieldsModel
from .models.proposal import ProposalModel, ProposalFieldAssignment


class ProposalFieldAssignmentInline(admin.TabularInline):
    model = ProposalFieldAssignment
    extra = 0
    can_delete = True


@admin.register(ProposalModel)
class ProposeModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title','proposal_situation',)
    fields = ('title', 'description',)
    inlines = [ProposalFieldAssignmentInline]


@admin.register(FieldsModel)
class FieldsModelAdmin(admin.ModelAdmin):
    list_display = ('label',)
    fields = ('label',)
