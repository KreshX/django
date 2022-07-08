from django import forms

class FeedbackForm(forms.Form):
	name = forms.CharField()
	# surname = forms.CharField()
	# feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20}))
	rating = forms.IntegerField(min_value=1, max_value=10)