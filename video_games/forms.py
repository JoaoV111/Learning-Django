from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
# class CommentsForm(forms.ModelForm):

# 	class Meta:
# 		model = Console.comments_set
# 		fields = ('comment_txt', 'score')
# 		labels = {
# 				  'comment_txt': ('Comentário'),
#             	  'score': ('Nota'),
#         		  }
# 		widgets = {
#             	   'comment_txt': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
#         			}

class CommentsForm(forms.Form):
	score = forms.ChoiceField(required=False, choices=[(0, '0'), (1, '1'),
							   (2, '2'), (3, '3'),
							   (4, '4'), (5, '5')], label='Nota')
	comment_txt = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}),
				      			    label='Comentário')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
					    'score',
					    'comment_txt',
					    Submit('submit', 'Submit', css_class='button white')
					    )

