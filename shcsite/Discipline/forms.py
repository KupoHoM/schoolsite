# from django import forms
# from django.forms import ModelForm
# from .models import Discipline
# from natsort import natsorted
#
#
# class ProductImageForm(forms.ModelForm):
#     # this will return only first saved image on save()
#     file = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), required=True)
#
#     class Meta:
#         model = Discipline
#         fields = ['file', ]
#
#     def save(self, *args, **kwargs):
#         # multiple file upload
#         # NB: does not respect 'commit' kwarg
#         file_list = natsorted(self.files.getlist('{}-file'.format(self.prefix)), key=lambda file: file.name)
#
#         self.instance.file = file_list[0]
#         for file in file_list[1:]:
#             Discipline.objects.create(
#                 # product=self.cleaned_data['product'],
#                 file=file,
#                 # position=self.cleaned_data['position'],
#             )
#
#         return super().save(*args, **kwargs)
