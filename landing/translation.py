# coding: utf-8

from modeltranslation.translator import register, TranslationOptions
from .models import Header , WhyWe, TextWhyWe , BlockForStudents , PopularСourses , ConfigFooter
from popup.models import ConfigContactForm , PopUpThanksConsulting , ConfigRegistrationForm ,PopUpThanksEventRegister , PopUpThanksRegister
from courses.models import Author , Course
from event.models import Lector , Event , ConfigurationEventsPopUp

@register(Header)
class HeaderTranslationOptions(TranslationOptions):

	fields = ('header_text', 'btn_learn', 'btn_presentation')

@register(WhyWe)
class WhyWeTranslationOptions(TranslationOptions):
	fields = ('text' , )

@register(TextWhyWe)
class TextWhyWeranslationOptions(TranslationOptions):

	fields  = ('text' , )

@register(ConfigContactForm)
class ConfigContactFormTranslationOptions(TranslationOptions):
	
	fields  = ('header' , 'text' , 'button')

@register(PopUpThanksConsulting)
class PopUpThanksConsultingTranslationOptions(TranslationOptions):

	fields = ('text' , )

@register(Author)
class AuthorTranslationOptions(TranslationOptions):

	fields = ('name' , 'surname'  , 'position')

@register(Course)
class CourseTranslationOptions(TranslationOptions):

	fields = ('name_ru' , 'description'  , 'duration' , 'shedule_btn_text' , 'learn_btn_text')


@register(ConfigRegistrationForm)
class ConfigRegistrationFormTranslationOptions(TranslationOptions):

	fields = ('header' , 'text'  , 'button')

@register(Lector)
class LectorTranslationOptions(TranslationOptions):

	fields = ('name' , 'surname'  , 'position')


@register(Event)
class EventTranslationOptions(TranslationOptions):

	fields = ('theme' , 'where'  , 'description')


@register(ConfigurationEventsPopUp)
class ConfigurationEventsPopUpTranslationOptions(TranslationOptions):

	fields = ('text_where' , 'text_when'  , 'name_form' , 'text_lector' , 'text_form' , 'btn' )

@register(PopUpThanksEventRegister)
class PopUpThanksEventRegisterTranslationOptions(TranslationOptions):

	fields = ('text',)

@register(PopUpThanksRegister)
class PopUpThanksRegisterTranslationOptions(TranslationOptions):

	fields = ('text',)
@register(BlockForStudents)
class BlockForStudentsTranslationOptions(TranslationOptions):

	fields = ('text',)


@register(PopularСourses)
class PopularСoursesTranslationOptions(TranslationOptions):

	fields = ('first_course','two_course' , 'three_course' , 'four_course')

@register(ConfigFooter)
class ConfigFooterTranslationOptions(TranslationOptions):

	fields = ('copyright',)

