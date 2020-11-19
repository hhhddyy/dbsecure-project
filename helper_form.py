from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import widgets, SubmitField, SelectMultipleField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(4, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
class auditform(FlaskForm):
    my_choices = [('1', 'auditing sending out data'), ('2', 'audit inserting data'), ('3','audit delete on data' ),
                  ('4', 'auditing creating table'),('5', 'save TNS lister to local files'),('6', 'auditing changing of privilges'),
                  ('7','auditing anyone anyone logging in or out'),
                  ('8','auditing changes to user profiles'),
                  ('9','anyone masquerading as a DBA')]

    choices=MultiCheckboxField(choices=my_choices)
    submit = SubmitField('confirm')
class maskform_user(FlaskForm):
    mask_choices = [("2", "mask out the middle 6 digits of the bank account for any user")
        ,
                    ("1", "Discard the CVV number for the credit card and do not store it")
        ,
                    ("3", "random shuffle the bank account")]
    choices = MultiCheckboxField(choices=mask_choices)
    submit = SubmitField('confirm')
class maskform_food(FlaskForm):
    mask_choices = [("1", "don't store the order address")
        ,
                    ("2", "mask all address and no one can view it in front end")
        ,
                    ("3", "shuffle the order histort so that user and history is mismatching")
                    ]
    choices = MultiCheckboxField(choices=mask_choices)
    submit = SubmitField('confirm')
class maskform_test(FlaskForm):
    mask_choices=[]
    choices = MultiCheckboxField(choices=mask_choices)
    submit = SubmitField('confirm')
class queryform_user(FlaskForm):
    mask_choices = [("2", "only the manager user in admin table can view user information")
        ,
                    ("1", ". Only those corresponding sales managers can view the whole user data under his area")
        ,
                    ("3", "allow user to view others information to make friends"),
                    ("4","block every one from viewing the payment table"),
                    ("5","only the privileged users with an accounting role can view the payment account")]
    choices = MultiCheckboxField(choices=mask_choices)
    submit = SubmitField('confirm')
class queryform_food(FlaskForm):
    mask_choices = [("1", "only the privileged users with an administrative role can view order history")
        ,
                    ("2", "user can view others history to find food")
        ,
                    ("3", "user can view its own food history")
                    ]
    choices = MultiCheckboxField(choices=mask_choices)
    submit = SubmitField('confirm')
class queryform_test(FlaskForm):
    mask_choices=[]
    choices = MultiCheckboxField(choices=mask_choices)
    submit = SubmitField('confirm')