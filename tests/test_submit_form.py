from selene import have, command, by
from selene.support.shared import browser
import os

class Gender:
    male = 'Male'
    female = 'Female'
    other = 'Other'

class Hobbies:
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Subjects:
    computer_science = 'Computer Science'
    english = 'English'

class student:
    name = "enchik"
    surname = "enchikov"
    email = "ivanov@gmail.com"
    mobile_number = "8800555353"
    birth_day = "27"
    birth_month = "6"
    birth_year = "1992"
    subjects = "English"
    current_address = "Novosibirsk"
    state = "Rajasthan"
    city = "Jaiselmer"


def test_registration_form():
    browser.open('/automation-practice-form')


    # Act
    browser.element('#firstName').type(student.name)
    browser.element('#lastName').type(student.surname)
    browser.element('#userEmail').type(student.email)
    gender_group = browser.element('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text(Gender.male)).click()

    browser.element('#userNumber').type(student.mobile_number)

    browser.element('#dateOfBirthInput').click()
    browser.element(f'.react-datepicker__year-select [value="{student.birth_year}"]').click()
    browser.element(f'.react-datepicker__month-select [value="{student.birth_month}"]').click()
    browser.element(f'.react-datepicker__month .react-datepicker__week .react-datepicker__day--0{student.birth_day}').click()

    browser.element('#subjectsInput').type(Subjects.english).press_enter()

    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text(Hobbies.music)).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath("../resources/original.jpg"))

    browser.element('#currentAddress').type(student.current_address)

    browser.element('#state input').type(student.state).press_tab()
    browser.element('#city input').type(student.city).press_tab()

    browser.element('#submit').perform(command.js.click)

    browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
    browser.all("table tbody tr").should(have.exact_texts(
        'Student Name enchik enchikov',
        'Student Email ivanov@gmail.com',
        'Gender Male',
        'Mobile 8800555353',
        'Date of Birth 27 July,1992',
        'Subjects English',
        'Hobbies Music',
        'Picture original.jpg',
        'Address Novosibirsk',
        'State and City Rajasthan Jaiselmer'
    ))

